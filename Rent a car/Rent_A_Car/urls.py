from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from Authentication_App.views import UserViewSet
from Owner_App.views import *

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'cars', CarViewSet, basename='cars')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('car/all/', AllCarView.as_view(), name='all_car'),
    path('category/all/', AllCategoryView.as_view(), name='all_category'),
    path('book/', BookingView.as_view(), name='book_car'),
    path('book/list/<car>/', BookingDateListView.as_view(), name='book_list_car'),
    path('bookings/', BookingListView.as_view(), name='book_list_user'),
] + router.urls


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)