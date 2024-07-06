from rest_framework import routers  
from SWIMP.api import EjemploViewSet
router = routers.DefaultRouter()

router.register('api/ejemplo', EjemploViewSet, 'ejemplo')

urlpatterns = router.urls
