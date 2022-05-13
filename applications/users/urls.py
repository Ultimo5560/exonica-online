from django.urls import path

from . import views

app_name = "user_app"

urlpatterns = [
    path(
        'userRegister', 
        views.UserRegisterView.as_view(), 
        name='Register'
    ),
    path(
        'userList', 
        views.UserListView.as_view(), 
        name='userList'
    ),
    path(
        'userEdit/<pk>/', 
        views.UserUpdateView.as_view(), 
        name='userEdit'
    ),
      path(
        'usuario-eliminar/<pk>/', 
        views.UserDeleteView.as_view(), 
        name='usuario_eliminar'
    ),
    path(
        'userLogin', 
        views.loginUser.as_view(), 
        name='login'
    ),
    path(
        'userLogout', 
        views.logoutUser.as_view(), 
        name='logout'
    ),
    path(
        'perfil-usuario', 
        views.UserPerfil.as_view(), 
        name='perfil_usuario'
    ),
    path(
        'editar-perfil-usuario', 
        views.UserUpdateForUser.as_view(), 
        name='editar_perfil_usuario'
    ),
]