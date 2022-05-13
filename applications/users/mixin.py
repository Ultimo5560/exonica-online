from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
#
from .models import User


def check_ocupations_user(ocupations, user_ocupations):
    #

    if (ocupations == User.ADMINISTRADOR or ocupations == user_ocupations):
        
        return True
    else:
        return False


class ClientePermisoMixin(LoginRequiredMixin):
    login_url = reverse_lazy('store_app:pub_articulos')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        #
        if not check_ocupations_user(request.user.ocupations, User.CLIENTE):
            # no tiene autorizacion
            return HttpResponseRedirect(
                reverse(
                    'store_app:pub_articulos'
                )
            )

        return super().dispatch(request, *args, **kwargs)


class AdminPermisoMixin(LoginRequiredMixin):
    login_url = reverse_lazy('store_app:pub_articulos')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        #
        if not check_ocupations_user(request.user.ocupations, User.ADMINISTRADOR):
            # no tiene autorizacion
            return HttpResponseRedirect(
                reverse(
                    'store_app:pub_articulos'
                )
            )
        return super().dispatch(request, *args, **kwargs)