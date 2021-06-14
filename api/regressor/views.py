from django.shortcuts import render

# Create your views here.
from .apps import RegressorConfig

from django.http import JsonResponse
from rest_framework.views import APIView

class call_model(APIView):
    def get(self,request):
        if request.method == 'GET':
            numberOfClaims = request.GET.get('numberofclaims')
            prediction = RegressorConfig.regressor.predict([[numberOfClaims]])
            prediction = prediction.tolist()
            response = {'total_money' : str(prediction[0])}
            return JsonResponse(response)