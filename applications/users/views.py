from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.views.generic import (
    View,
    ListView,
    UpdateView,
    DeleteView
)
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import FormView
from .forms import UserRegisterForm, UserLoginForm, UserUpdateForm, UserUpdatePerfilForm
from .models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from applications.users.mixin import AdminPermisoMixin


class UserRegisterView(FormView):
    template_name = "users/registerUser.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy('user_app:login')
    
    def form_valid(self, form):
        User.objects.create_user(
            form.cleaned_data['email'],
            form.cleaned_data['password_1'],
            ## ExtraFields
            nombre = form.cleaned_data['nombre'],
            apellidos = form.cleaned_data['apellidos'],
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento'],
            celular = form.cleaned_data['celular'],
            genero = form.cleaned_data['genero'],
            ciudad = form.cleaned_data['ciudad'],
            estado = form.cleaned_data['estado'],
            direccion_envio = form.cleaned_data['direccion_envio']
        )
        return super(UserRegisterView, self).form_valid(form)


class loginUser(FormView):
    template_name = "users/loginUser.html"
    form_class = UserLoginForm
    success_url = reverse_lazy('store_app:pub_articulos')

    def form_valid(self, form):
        email = authenticate(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        login(self.request, email)
        return super(loginUser, self).form_valid(form)

class logoutUser(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'store_app:pub_articulos'
            )
        )


class UserListView(AdminPermisoMixin, LoginRequiredMixin, ListView):
    model = User
    template_name = "admin/list_user.html"
    context_object_name = 'listarusuarios'
    paginate_by = '5'
    ordering = 'nombre'
    login_url = reverse_lazy('user_app:login')
    permission_required = 'applications.admin_exonica'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "admin/editar_usuario.html"
    form_class = UserUpdateForm
    success_url = reverse_lazy('user_app:userList')
    login_url = reverse_lazy('user_app:login')
    permission_required = 'applications.admin_exonica'


class UserDeleteView(DeleteView):
    model = User
    template_name = "admin/eliminar_usuario.html"
    context_object_name = 'usuariodelete'
    success_url = reverse_lazy('user_app:userList')
    permission_required = 'applications.admin_exonica'

class UserUpdateForUser(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "users/editar_perfil.html"
    form_class = UserUpdatePerfilForm
    success_url = reverse_lazy('user_app:perfil_usuario')
    login_url = reverse_lazy('user_app:login')


    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        return self.request.user


class UserPerfil(LoginRequiredMixin, TemplateView):
    template_name = "users/mi_perfil.html"
    login_url = reverse_lazy('user_app:login')


    def get_context_data(self, **kwargs):
        context = super(UserPerfil, self).get_context_data(**kwargs)
        # Contexto de portada
        context["miPerfil"] = self.request.user
        return context