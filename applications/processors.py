from applications.store_exonica.models import FormContact, Payment


def num_msj(request):
    numMsj = FormContact.objects.num_msj()
    return {
        'msjnoread':numMsj,
    }

def numCompras(request):
    numCompras = Payment.objects.compras_num()
    return {
        'comprasnum':numCompras,
    }
