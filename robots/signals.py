from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

import orders
import robots
from R4C import settings


@receiver(post_save, sender=robots.models.Order)
def create_robot(sender, instance, created, **kwargs):
    serial = f"{instance.model}-{instance.version}"
    delayed_orders = orders.models.Order.objects.filter(robot_serial=serial)
    if created and delayed_orders:
        for order in delayed_orders:
            email = order.customer.email
            msg = f'''
                Добрый день!
                Недавно вы интересовались нашим роботом модели {order.robot_serial[:2]}, версии {order.robot_serial[-2:]}. 
                Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами'''
            send_mail('Order', msg, settings.DEFAULT_FROM_EMAIL, [email])
