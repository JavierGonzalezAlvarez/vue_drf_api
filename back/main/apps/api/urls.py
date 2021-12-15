from django.urls import path, include

from rest_framework import routers

from .views import LoadingPortViewSet, DischargePortViewSet, \
    BookingViewSet, VehicleViewSet


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'loadingport', LoadingPortViewSet)
router.register(r'dischargeport', DischargePortViewSet)
router.register(r'booking', BookingViewSet)
router.register(r'vehicle', VehicleViewSet)

urlpatterns = [
    # re_path('', include(router.urls)),
    # re_path(r'^token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # re_path(r'^token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #re_path(r'', include(router.urls)),

    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
