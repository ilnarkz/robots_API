from datetime import datetime

from django.db.models import Q
from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView

from robots.models import Order


class RobotsAPIView(APIView):

    def get(self, request):
        orders = Order.objects.all().values()
        return Response({'robots': list(orders)})

    def post(self, request):
        if Order.objects.filter(Q(model=request.data['model']) & Q(version=request.data['version'])):
            return Response({'error': 'Эта модель и версия робота уже существует в системе'})
        new_robot = Order.objects.create(
            serial=f"{request.data['model']}-{request.data['version']}",
            model=request.data['model'],
            version=request.data['version'],
            created=datetime.now()
        )
        return Response({'robot': model_to_dict(new_robot)})
