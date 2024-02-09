from django.http import JsonResponse, HttpResponse
import json

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class PingApiView(APIView):
    def get(self, request):
        return Response({"result": "pong"})

class CatShelvesAPIView(APIView):
    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('start', openapi.IN_QUERY, type=openapi.TYPE_STRING),
        openapi.Parameter('end', openapi.IN_QUERY, type=openapi.TYPE_STRING),
    ])
    def get(self, request):
        start = int(request.query_params.get('start'))
        end = int(request.query_params.get('end'))

        # Write the code for Challenge 1 here

        return Response(-1)

class RestaurantOrderAPIView(APIView):
    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'order': openapi.Schema(type=openapi.TYPE_STRING),
        },
        required=['item', 'quantity'],
    ))
    def post(self, request):
        order = request.data['order']

        # Write the code for Challenge 2 here

        return Response("")

class SupermarketQueueAPIView(APIView):
    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'customers': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_NUMBER)),
            'selfCheckoutPoints': openapi.Schema(type=openapi.TYPE_NUMBER),
        },
        required=['item', 'quantity'],
    ))
    def post(self, request):
        customers = request.data['customers']
        selfCheckoutPoints = request.data['selfCheckoutPoints'] 

        # Write the code for Challenge 3 here

        return Response(-1)
