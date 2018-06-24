from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login, authenticate, logout

from models import CreateProject


class IndexView(APIView):

    def get(self, request):

        return render(request, 'html/index.html')


class CreateProject(APIView):

    domainId = models.CharField(max_length=5, null=True, blank=True)
    project_brief = models.TextField(null=True, blank=True)
    creator_address = models.CharField(max_length=100, null=True, blank=True)
    creator_name = models.CharField(max_length=100, null=True, blank=True)

    def post(self, request):

       new_project = CreateProject()

       new_project.project_title = request.POST['projectTitle']
       new_project.project_brief = request.POST['projectBrief']
       new_project.creator_address = request.POST['creatorAddress']
       new_project.creator_name = request.POST['creatorName']
       new_project.txn_hash = request.POST['txnhash']

       new_project.save()

       return Response(data=200)
