from rest_framework import routers
from .api import UsersViewSet

router = routers.DefaultRouter()
router.register('api/user', UsersViewSet, 'user')

urlpatterns = router.urls
