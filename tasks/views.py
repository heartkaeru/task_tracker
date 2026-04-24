from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from .models import Project, ProjectMembership, Task, TaskComment
from .serializers import (
    UserSerializer,
    ProjectSerializer,
    ProjectMembershipSerializer,
    TaskSerializer,
    TaskCommentSerializer,
)

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(
            participants=self.request.user
        )

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'priority', 'assignee', 'project', 'deadline']

    def get_queryset(self):
        return Task.objects.filter(
            project__participants=self.request.user
        )

class TaskCommentViewSet(viewsets.ModelViewSet):
    serializer_class = TaskCommentSerializer

    def get_queryset(self):
        return TaskComment.objects.filter(
            task__project__participants=self.request.user
        )

class ProjectMembershipViewSet(viewsets.ModelViewSet):
    queryset = ProjectMembership.objects.all()
    serializer_class = ProjectMembershipSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
