from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView, CreateView, TemplateView, UpdateView, DeleteView, DetailView
from .functions import detalle_resumen_ventas
from applications.store_exonica.models import AboutExonica, FormContact, Payment
from .models import CategoriaArticulos, Articulos, Anuncios
from .forms import FormAbout, FormAnuncios, FormCategoria, FormArticulos, FormPaymentEditHome
from applications.users.mixin import AdminPermisoMixin

# Create your views here.

class quienSomosView(AdminPermisoMixin, LoginRequiredMixin, TemplateView):
    template_name = "admin/about_exonica.html"
    
    def get_context_data(self, **kwargs):
        context = super(quienSomosView, self).get_context_data(**kwargs)
        # Contexto de portada
        context["aboutExo"] = AboutExonica.objects.all()
        context["formAbout"] = FormAbout
        return context


class quienesSomosUpdateView(AdminPermisoMixin, LoginRequiredMixin, UpdateView):
    model = AboutExonica
    template_name = "admin/update_about_exo.html"
    success_url = reverse_lazy('app_admin:about_exo')
    form_class = FormAbout


class listarPayments(AdminPermisoMixin, LoginRequiredMixin, TemplateView):
    template_name = "admin/listaPayments.html"
    context_object_name = 'listarpayments'
    paginate_by = '5'
    ordering = '-created'
    permission_required = 'applications.admin_exonica'
    login_url = reverse_lazy('user_app:login')

    def get_context_data(self, **kwargs):
        context = super(listarPayments, self).get_context_data(**kwargs)
        context["payment"] = detalle_resumen_ventas(
            self.request.GET.get("categoria", ''),
        )
        return context


class PaymentDeleteView(AdminPermisoMixin, LoginRequiredMixin, DeleteView):
    model = Payment
    template_name = "admin/eliminar_payment.html"
    success_url = reverse_lazy('app_admin:payments_listar')
    login_url = reverse_lazy('user_app:login')
    permission_required = 'applications.admin_exonica'


class DatosPaymentUpdateView(AdminPermisoMixin, LoginRequiredMixin, UpdateView):
    model = Payment
    template_name = "admin/editarStatus.html"
    form_class = FormPaymentEditHome
    success_url = reverse_lazy('app_admin:payments_listar')


class CategoriaArticulosCreateView(AdminPermisoMixin, LoginRequiredMixin, CreateView):
    model = CategoriaArticulos
    template_name = "admin/crearCategoria.html"
    context_object_name = 'crearcategoria'
    success_url = reverse_lazy('app_admin:categoria_listar')
    login_url = reverse_lazy('user_app:login')
    permission_required = 'applications.admin_exonica'
    form_class = FormCategoria

    def form_valid(self, form):
        cat = CategoriaArticulos(
            short_name=form.cleaned_data['short_name'],
            name=form.cleaned_data['name'],
        )
        cat.save
        
        return super(CategoriaArticulosCreateView, self).form_valid(form)


class ArticulosCreateView(AdminPermisoMixin, LoginRequiredMixin, CreateView):
    model = Articulos
    template_name = "admin/articulosVenta.html"
    success_url = reverse_lazy('app_admin:articulos_listar')
    login_url = reverse_lazy('user_app:login')
    permission_required = 'applications.admin_exonica'
    form_class = FormArticulos

    def form_valid(self, form):
        art = Articulos(
            user=form.cleaned_data['user'],
            title=form.cleaned_data['title'],
            precio=form.cleaned_data['precio'],
            categoria=form.cleaned_data['categoria'],
            imagen=form.cleaned_data['imagen'],
            descripcion=form.cleaned_data['descripcion'],
            public=form.cleaned_data['public'],
            in_home=form.cleaned_data['in_home'],
        )
        art.save
        
        return super(ArticulosCreateView, self).form_valid(form)


class AnunciosCreateView(AdminPermisoMixin, LoginRequiredMixin, CreateView):
    model = Anuncios
    template_name = "admin/anuncios_in_home.html"
    success_url = reverse_lazy('store_app:pub_articulos')
    login_url = reverse_lazy('user_app:login')
    permission_required = 'applications.admin_exonica'
    form_class = FormAnuncios

    def form_valid(self, form):
        art = Anuncios(
            user=form.cleaned_data['user'],
            title=form.cleaned_data['title'],
            mensaje=form.cleaned_data['mensaje'],
            imagen=form.cleaned_data['imagen'],
            public=form.cleaned_data['public'],
            portada=form.cleaned_data['portada'],
        )
        art.save
        
        return super(AnunciosCreateView, self).form_valid(form)


class listarArticulosListView(AdminPermisoMixin, LoginRequiredMixin, ListView):
    model = Articulos
    template_name = "admin/listaArticulos.html"
    context_object_name = 'listararticulos'
    paginate_by = '5'
    ordering = 'title'
    permission_required = 'applications.admin_exonica'
    login_url = reverse_lazy('user_app:login')

    
class listarCategoriasListView(AdminPermisoMixin, LoginRequiredMixin, ListView):
    model = CategoriaArticulos
    template_name = "admin/listaCategoria.html"
    context_object_name = 'listarcategoria'
    paginate_by = '5'
    ordering = 'name'
    login_url = reverse_lazy('user_app:login')
    permission_required = 'applications.admin_exonica'


class listarAnunciosListView(AdminPermisoMixin, LoginRequiredMixin, ListView):
    model = Anuncios
    template_name = "admin/listaAnuncios.html"
    context_object_name = 'listaranuncios'
    paginate_by = '5'
    ordering = 'title'
    login_url = reverse_lazy('user_app:login')
    permission_required = 'applications.admin_exonica'


class CategoriaUpdateView(AdminPermisoMixin, LoginRequiredMixin, UpdateView):
    model = CategoriaArticulos
    template_name = "admin/editar_categoria.html"
    form_class = FormCategoria
    success_url = reverse_lazy('app_admin:categoria_listar')
    login_url = reverse_lazy('user_app:login')
    permission_required = 'applications.admin_exonica'


class AnuncioUpdateView(AdminPermisoMixin, LoginRequiredMixin, UpdateView):
    model = Anuncios
    template_name = "admin/editar_anuncio.html"
    form_class = FormAnuncios
    success_url = reverse_lazy('app_admin:anuncios_listar')
    login_url = reverse_lazy('user_app:login')
    permission_required = 'applications.admin_exonica'


class CategoriaDeleteView(AdminPermisoMixin, LoginRequiredMixin, DeleteView):
    model = CategoriaArticulos
    template_name = "admin/eliminar_categoria.html"
    success_url = reverse_lazy('app_admin:categoria_listar')
    login_url = reverse_lazy('user_app:login')
    permission_required = 'applications.admin_exonica'


class AnunciosDeleteView(AdminPermisoMixin, LoginRequiredMixin, DeleteView):
    model = Anuncios
    template_name = "admin/eliminar_anuncio.html"
    success_url = reverse_lazy('app_admin:anuncios_listar')
    login_url = reverse_lazy('user_app:login')
    permission_required = 'applications.admin_exonica'


class ArticulosUpdateView(AdminPermisoMixin, LoginRequiredMixin, UpdateView):
    model = Articulos
    template_name = "admin/editar_articulo.html"
    form_class = FormArticulos
    success_url = reverse_lazy('app_admin:articulos_listar')
    login_url = reverse_lazy('user_app:login')
    permission_required = 'applications.admin_exonica'


class ArticulosDeleteView(AdminPermisoMixin, LoginRequiredMixin, DeleteView):
    model = Articulos
    template_name = "admin/eliminar_articulo.html"
    success_url = reverse_lazy('app_admin:articulos_listar')
    permission_required = 'applications.admin_exonica'


class listarMensjaesListView(AdminPermisoMixin, LoginRequiredMixin, ListView):
    model = FormContact
    template_name = "admin/listaMensajes.html"
    context_object_name = 'listarmensajes'
    paginate_by = '10'
    ordering = '-created'
    permission_required = 'applications.admin_exonica'
    login_url = reverse_lazy('user_app:login')


class MensajeDeleteView(AdminPermisoMixin, LoginRequiredMixin, DeleteView):
    model = FormContact
    template_name = "admin/eliminar_mensaje.html"
    success_url = reverse_lazy('app_admin:mensajes_listar')
    login_url = reverse_lazy('user_app:login')
    permission_required = 'applications.admin_exonica'


class MensajeDetailView(AdminPermisoMixin, LoginRequiredMixin, DetailView):
    model = FormContact
    template_name = "admin/ver_mensaje.html"
    login_url = reverse_lazy('user_app:login')
    permission_required = 'applications.admin_exonica'

    def get_context_data(self, **kwargs):
        context = super(MensajeDetailView, self).get_context_data(**kwargs)
        return context

class procesarMsjView(AdminPermisoMixin, LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        mensaje = FormContact.objects.get(id=self.kwargs['pk'])
        if mensaje.read == False:
            mensaje.read = True
            mensaje.save()
            return HttpResponseRedirect(
                reverse(
                    'app_admin:mensajes_listar'
                )  
            )
        else:
            mensaje.read = False
            mensaje.save()
            return HttpResponseRedirect(
                reverse(
                    'app_admin:mensajes_listar'
                )  
            )