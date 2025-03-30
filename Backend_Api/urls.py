from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from Api import urls as api_urls
from Api.views import DeepSeekApiView
from Backend_Api import settings

admin.site.site_header = "Chachu Super Store API Admin"

urlpatterns = [
    path("api/", include(api_urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/deepseek-chat/', DeepSeekApiView.as_view(), name='deepseek-chat'),
    path('api/deepseek-chat/<str:pk>/', DeepSeekApiView.as_view(), name='deepseek-chat'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
