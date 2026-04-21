from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Project, ProjectMembership, Task, TaskComment
from .serializers import (
    UserSerializer,
    ProjectSerializer,
    ProjectMembershipSerializer,
    TaskSerializer,
    TaskCommentSerializer,
)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskCommentViewSet(viewsets.ModelViewSet):
    queryset = TaskComment.objects.all()
    serializer_class = TaskCommentSerializer

class ProjectMembershipViewSet(viewsets.ModelViewSet):
    queryset = ProjectMembership.objects.all()
    serializer_class = ProjectMembershipSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
