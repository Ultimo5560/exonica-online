import json
from django.http import JsonResponse
from django.http.response import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.views.generic import View, ListView, CreateView, TemplateView, DeleteView, DetailView
from django.views.generic.edit import FormView
from rest_framework.generics import (
    GenericAPIView,
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CountCarSerializar
from applications.admin_exonica.models import Articulos, Anuncios, CategoriaArticulos
from .forms import Form_contact, VentaForm, Form_payment_trans
from .models import FormContact, Payment, CarShop, AboutExonica
from exonica_online.settings import local
from .functions import procesar_venta

# Create your views here.

class HomePageView(TemplateView):
    template_name = "store/index.html"
    
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        # Contexto de portada
        context["portada"] = Anuncios.objects.anuncios_en_portada()
        # Contexto de articulos en home
        context["articulos_home"] = Articulos.objects.articulos_en_home()
        # Contexto de entradas recientes
        context["articulos_recientes"] = Articulos.objects.articulos_recientes()
        context["aboutExo"] = AboutExonica.objects.all()
        return context

class ContactPageView(TemplateView):
    template_name = "store/inform-contact.html"
    
    def get_context_data(self, **kwargs):
        context = super(ContactPageView, self).get_context_data(**kwargs)
        # Contexto de articulos en home
        context["formContact"] = Form_contact
        return context
    

class aboutExonica(TemplateView):
    template_name = "store/about-exonica.html"
    
    def get_context_data(self, **kwargs):
        context = super(aboutExonica, self).get_context_data(**kwargs)
        # Contexto de portada
        context["aboutExo"] = AboutExonica.objects.all()
        return context

class ArticulosDetailView(DetailView):
    model = Articulos
    template_name = "store/detalle_articulo.html"

    def get_context_data(self, **kwargs):
        context = super(ArticulosDetailView, self).get_context_data(**kwargs)
        # Contexto de articulos en home
        context["formNum"] = VentaForm
        return context


class ArticulosPorCategorias(ListView):
    template_name = "store/categorias_productos.html"
    context_object_name = 'articulos'
    
    def get_context_data(self, **kwargs):
        context = super(ArticulosPorCategorias, self).get_context_data(**kwargs)
        context["categorias"] = CategoriaArticulos.objects.all()
        return context
    

    def get_queryset(self):
        # Consulta de busquedas por palabra clave
        kword = self.request.GET.get("kword", '')
        # Consulta de busquedas por palabra categoria
        categoria = self.request.GET.get("categoria", '')
        resultado = Articulos.objects.buscar_articulos(kword, categoria)
        return resultado


class MensajeCreateView(CreateView):
    success_url = reverse_lazy('store_app:pub_articulos')
    form_class = Form_contact

    def form_valid(self, form):
        msj = FormContact(
            full_name=form.cleaned_data['full_name'],
            email=form.cleaned_data['email'],
            celphone=form.cleaned_data['celphone'],
            message=form.cleaned_data['message'],

        )
        msj.save
        
        return super(MensajeCreateView, self).form_valid(form)


class AddCarView(LoginRequiredMixin, FormView):
    model = CarShop
    form_class = VentaForm
    login_url = reverse_lazy('user_app:login')

    def form_valid(self, form):
        # Recuperamos ID y form con la cantidad
        instal=form.cleaned_data['instalacion']
        count=form.cleaned_data['count']
        objarticulo = Articulos.objects.get(id=self.kwargs['pk'])
        obj, created = CarShop.objects.get_or_create(
            user=self.request.user,
            product = Articulos.objects.get(id=self.kwargs['pk']),
            defaults={
             'instalacion': instal,
                   'count': count,
                'subtotal': (objarticulo.precio)*(count),
            }
        )

        if created:
            if instal == True:
                if obj.user.estado == 'Sonora':
                    obj.subtotal = (objarticulo.precio)*(obj.count)+(objarticulo.precio_inst)
                else:
                    obj.subtotal = (objarticulo.precio)*(obj.count)+(objarticulo.precio_inst_fuera)
                obj.save()
            else:
                obj.subtotal = (objarticulo.precio)*(obj.count)
                obj.save()

        elif not created and instal == True or obj.instalacion == True:
            obj.count = obj.count + count
            obj.instalacion = instal
            if obj.user.estado == 'Sonora':
                obj.subtotal = (objarticulo.precio)*(obj.count)+(objarticulo.precio_inst)
            else:
                obj.subtotal = (objarticulo.precio)*(obj.count)+(objarticulo.precio_inst_fuera)
            obj.save()
        else:
            obj.count = obj.count + count
            operacion = (objarticulo.precio)*count
            obj.subtotal = (obj.subtotal) + operacion
            obj.save()
        
        return HttpResponseRedirect(
            reverse(
                'store_app:car_shop'
            )  
        )


class CarPageView(LoginRequiredMixin, TemplateView):
    template_name = "store/car-shop.html"
    login_url = reverse_lazy('user_app:login')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["productos"] = CarShop.objects.entradas_user(self.request.user)
        context["total_all"] = CarShop.objects.total_cobrar(self.request.user)
        return context


class CarNumApiView(APIView):
    serializer_class = CountCarSerializar

    def get(self, request):
        usuario = self.request.user
        if usuario.is_authenticated:
            result =  CarShop.objects.num_car(self.request.user)
            return Response(result)
        else:
            return Response(0)



class CarShopUpdateViewRest(LoginRequiredMixin, View):
    """ quita en 1 la cantidad en un carshop """

    def post(self, request, *args, **kwargs):
        car = CarShop.objects.get(id=self.kwargs['pk'])
        if car.count > 1:
            car.count = car.count - 1
            car.subtotal = car.subtotal - car.product.precio
            car.save()
        #
        return HttpResponseRedirect(
            reverse(
                'store_app:car_shop'
            )
        )

class CarShopUpdateViewMas(LoginRequiredMixin, View):
    """ suma en 1 la cantidad en un carshop """

    def post(self, request, *args, **kwargs):
        car = CarShop.objects.get(id=self.kwargs['pk'])
        car.count = car.count + 1
        car.subtotal = car.subtotal + car.product.precio
        car.save()
        #
        return HttpResponseRedirect(
            reverse(
                'store_app:car_shop'
            )
        )


class CarDeleteView(LoginRequiredMixin, DeleteView):
    model = CarShop
    success_url = reverse_lazy('store_app:car_shop')


class CarDeleteViewAll(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        CarShop.objects.entradas_user(self.request.user).delete()
        return HttpResponseRedirect(
            reverse(
                'store_app:car_shop'
            )  
        )

class PaymentView(LoginRequiredMixin,TemplateView):
    template_name="store/payment.html"
    
    def get_context_data(self, **kwargs):
        context = super(PaymentView, self).get_context_data(**kwargs)
        context['PAYPAL_CLIENT_ID'] = local.PAYPAL_CLIENT_ID
        context["productos"] = CarShop.objects.entradas_user(self.request.user)
        context['order'] = CarShop.objects.total_cobrar(self.request.user)
        context['CALLBACK_URL'] = self.request.build_absolute_uri(reverse("store_app:gracias_comprar"))
        return context


class PaymentViewTrans(LoginRequiredMixin, CreateView):
    template_name="store/payment-trans.html"
    form_class = Form_payment_trans

    def form_valid(self, form):
        comprobante_pago=form.cleaned_data['comprobante_pago']
        amount = CarShop.objects.total_cobrar(self.request.user)
        procesar_venta(
            self=self,
            user=self.request.user,
            comprobante_pago=comprobante_pago,
            payment_method=Payment.TRANSFERENCIA,
            amount = amount,
            status = Payment.VERYFY,
            raw_response = False
        )
        
        return HttpResponseRedirect(
            reverse(
                'store_app:gracias_comprar'
            )  
        )
    
    def get_context_data(self, **kwargs):
        context = super(PaymentViewTrans, self).get_context_data(**kwargs)
        context["productos"] = CarShop.objects.entradas_user(self.request.user)
        context['order'] = CarShop.objects.total_cobrar(self.request.user)
        context['formPaymentTrans'] = Form_payment_trans
        return context

    
    

class confirmOrderView(LoginRequiredMixin, View):

      def post(self, request, *args, **kwargs):
        #
        body = json.loads(request.body)
        procesar_venta(
            self=self,
            user=self.request.user,
            payment_method=Payment.PAYPAL,
            amount = float(body["purchase_units"][0]["amount"]["value"]),
            status = Payment.ORDERED,
            raw_response = json.dumps(body),
        )
        #
        
        return JsonResponse({"data": "Success"})

class GraciasPorComprarView(LoginRequiredMixin, TemplateView):
    template_name = 'store/thanks.html'
    def get_context_data(self, **kwargs):
        context = super(GraciasPorComprarView, self).get_context_data(**kwargs)
        context['dataOrder'] = Payment.objects.user_last(self.request.user)
        return context

class historialComprasView(LoginRequiredMixin, TemplateView):
    template_name = 'store/historial-compras.html'
    def get_context_data(self, **kwargs):
        context = super(historialComprasView, self).get_context_data(**kwargs)
        context['historialCompras'] = Payment.objects.user_five_last(self.request.user)
        return context