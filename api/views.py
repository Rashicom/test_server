from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import redis

from .serializers import Roomserializer, CustomPagination, StudentsSerializer, UrlSerializer
from .models import room, students, Route, Ip, RouteThrough, Shops, room_teachers, Url

import json
import time
from django.forms import model_to_dict
from django.conf import settings
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
import logging
from django.core.cache import cache
import random
import string
import logging
import pdfkit

logger = logging.getLogger("my-log")

class test(APIView):
    def get(self, request):
        
        return render(
            request,
            "payment.html"
        )


class CreatePDF(APIView):
    def get(self, request):
        
        config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
        rslt = pdfkit.from_url('http://127.0.0.1:8000/api/test/', 'media/tuttu.pdf', configuration=config)
        print("pdf creation : ", rslt)
        return Response(status=200)