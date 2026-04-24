from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Project, ProjectMembership, Task, TaskComment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ProjectSerializer(serializers.ModelSerializer):
    creator = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Project
        fields = '__all__'

    def validate(self, data):
        return data


class ProjectMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMembership
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Task
        fields = '__all__'

    def validate(self, data):
        request = self.context['request']
        project = data.get('project')
        assignee = data.get('assignee')

        if project and request.user not in project.participants.all():
            raise serializers.ValidationError("Вы не участник проекта")

        if assignee and assignee not in project.participants.all():
            raise serializers.ValidationError("Исполнитель должен быть участником проекта")

        return data


class TaskCommentSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = TaskComment
        fields = '__all__'

    def validate(self, data):
        request = self.context['request']
        task = data.get('task')

        if task and request.user not in task.project.participants.all():
            raise serializers.ValidationError("Нет доступа к задаче")

        return data