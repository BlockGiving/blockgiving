from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login, authenticate, logout


class IndexView(APIView):

    def get(self, request):

        return render(request, 'html/index.html')
