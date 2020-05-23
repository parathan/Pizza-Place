from django.urls import include, path
from . import views
from rest_framework import routers

router = router.DefaultRouter()
router.register(r'Regular', views.RegularViewSet)
router.register(r'Sicilian', views.SicilianViewSet)
router.register(r'Toppings', views.ToppingsViewSet)
router.register(r'Subs', views.SubsViewSet)
router.register(r'SubToppings', views.SubToppingsViewSet)
router.register(r'Pasta', views.PastaViewSet)
router.register(r'Salads', views.SaladsViewSet)
router.register(r'Platters', views.PlattersViewSet)

urlpatterns = [
    path("", include(router.url)),
    path("api-auth/", include('rest_framework.urls', namespace = 'rest_framework')),
]
