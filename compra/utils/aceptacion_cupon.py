from compra.models import Compra, UsuarioCupon
from cupon.models import Cupon
from django.db.models import Sum

from django.db.models import Sum
from django.core.mail import send_mail
from django.db.models import F

def get_cupon(email):
    # Suma los litros vendidos para el correo dado
    litros = Compra.objects.filter(email=email).aggregate(total_litros=Sum('litros_vendidos'))['total_litros']

    if litros:
        # Busca un cupón que cumpla con la condición
        cupon = Cupon.objects.filter(litros__lte=litros).order_by('-litros').first()  # El cupón con más litros posible
        if cupon:
            if not UsuarioCupon.objects.filter(email=email, cupon=cupon).first():
                # Envía un correo con la información del cupón
                '''
                send_mail(
                    'Cupón asignado',
                    f'Felicidades, has recibido el cupón: {cupon.nombre}.',
                    'noreply@miempresa.com',  # Cambia por tu correo
                    [email],
                    fail_silently=False,
                )
                '''

                # Asigna el cupón al usuario en otro modelo
                UsuarioCupon.objects.create(email=email, cupon=cupon)
                

                print(f"Cupón asignado: {cupon.nombre} para el usuario {email}")
                return True
    return False


