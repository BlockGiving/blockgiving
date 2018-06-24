from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login, authenticate, logout

from models import CreateProject


class IndexView(APIView):

    def get(self, request):

        return render(request, 'html/index.html')


class ProjectDetailsView(APIView):

    def get(self, request):

        return render(request, 'html/projectdetails.html')


class CreateProjectView(APIView):

    def post(self, request):

       new_project = CreateProject()

       new_project.project_title = request.POST['projectTitle']
       new_project.domainId = request.POST['domainId']
       new_project.project_brief = request.POST['projectBrief']
       new_project.creator_address = request.POST['creatorAddress']
       new_project.creator_name = request.POST['creatorName']
       new_project.txn_hash = request.POST['txnhash']

       new_project.save()

       return Response(data=200)

class GetProjects(APIView):

    def get(self, request):

        project_details = []

        for i in CreateProject.objects.all():

            project_details.append(
                {
                    'projectTitle' : i.project_title,
                    'domainId' : i.domainId,
                    'projectBrief' : i.project_brief,
                    'creatorAddress' : i.creator_address,
                    'creatorName' : i.creator_name,
                    'txnhash' : i.txn_hash
                }
            )

        return Response(data=project_details)
