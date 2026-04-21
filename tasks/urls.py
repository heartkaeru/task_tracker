from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet,
    ProjectViewSet,
    ProjectMembershipViewSet,
    TaskViewSet,
    TaskCommentViewSet,
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'memberships', ProjectMembershipViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'comments', TaskCommentViewSet)

urlpatterns = router.urls