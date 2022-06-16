from django.urls import include, path

from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register("user", UserViewSet, basename="User")
router.register("permissions", LGPDPermissionsViewSet, basename="LGPDPermissions")
router.register("formattention", FormAttentionViewSet, basename="FormAttention")
router.register("formpersonality", FormPersonalityViewSet, basename="FormPersonality")
router.register("formlearning", FormLearningViewSet, basename="FormLearning")


urlpatterns = [
    path("", include(router.urls)),
]
