from .models import Payment, PaymentDetail, CarShop


def procesar_venta(self, **params_venta):
    # recupera la lista de productos en carrtio
    productos_en_car = CarShop.objects.entradas_user(self.request.user)
    if productos_en_car.count() > 0:
        
        # crea el objeto venta
        if params_venta['payment_method'] == Payment.PAYPAL:
            venta = Payment.objects.create(
                amount=params_venta['amount'],
                succesful=True,
                payment_method=params_venta['payment_method'],
                user=params_venta['user'],
                status=params_venta['status'],
                raw_response=params_venta['raw_response'],
            )
        else:
            venta = Payment.objects.create(
                amount=params_venta['amount'],
                succesful=True,
                payment_method=params_venta['payment_method'],
                user=params_venta['user'],
                raw_response=params_venta['raw_response'],
                comprobante_pago=params_venta['comprobante_pago'],
                status=params_venta['status'],
            )
        #
        payments_detalles = []
        for producto_car in productos_en_car:
            if producto_car.instalacion == False:
                precio_inst = 0
            elif producto_car.instalacion == True:
                if producto_car.user.estado == 'Sonora':
                    precio_inst = producto_car.product.precio_inst
                else:
                    precio_inst = producto_car.product.precio_inst_fuera
            payment_detalle = PaymentDetail(
                product=producto_car.product,
                sale=venta,
                count=producto_car.count,
                price_sale=producto_car.product.precio,
                instalacion=producto_car.instalacion,
                costo_instalacion=precio_inst,
            )
            payments_detalles.append(payment_detalle)

        venta.save()
        PaymentDetail.objects.bulk_create(payments_detalles)
        # completada la venta, eliminamos productos delc arrito
        productos_en_car.all().delete()
        return venta
    else:
        return None
