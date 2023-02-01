from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView

from customers.models import Customer
from orders.models import Order


class OrdersAPIView(APIView):

    def get(self, request):
        orders = Order.objects.all().values()
        return Response({'orders': list(orders)})

    def post(self, request):
        customer, created = Customer.objects.get_or_create(email=request.data['customer'])
        new_order = Order.objects.create(
            robot_serial=request.data['robot_serial'],
            customer=customer
        )
        return Response({'robot': model_to_dict(new_order)})
