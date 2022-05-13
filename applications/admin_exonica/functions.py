from django.db.models import Prefetch, F, FloatField, ExpressionWrapper
from applications.store_exonica.models import Payment, PaymentDetail



def detalle_resumen_ventas(categoria):
    # funcion que recupera ventas no anuladas en rango de fechas
    # Y, el detalle de venta de cada venta
    
    if categoria:
        ventas = Payment.objects.buscar_pedido(categoria)
        consulta = ventas.prefetch_related(
            Prefetch(
                'detail_payment', 
                queryset=PaymentDetail.objects.filter(sale__id__in=ventas).annotate(
                    subtotal=ExpressionWrapper(
                        F('price_sale')*F('count')+F('costo_instalacion'),
                        output_field=FloatField()
                    )
                )
            )
        )
    else:
        ventas = Payment.objects.all()[:15]
        consulta = ventas.prefetch_related(
            Prefetch(
                'detail_payment', 
                queryset=PaymentDetail.objects.filter(sale__id__in=ventas).annotate(
                    subtotal=ExpressionWrapper(
                        F('price_sale')*F('count')+F('costo_instalacion'),
                        output_field=FloatField()
                    )
                )
            )
        )
        

    return consulta