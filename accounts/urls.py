from django.urls import path
from .views import UserViewSet
from rest_framework.routers import SimpleRouter


# setting up router
router = SimpleRouter()
# registering the routers
router.register(r'users', UserViewSet, basename="users")
urlpatterns = router.urls