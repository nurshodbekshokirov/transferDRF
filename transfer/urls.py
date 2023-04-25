
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from asosiy.views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Netflix API",
      default_version='v1',
      description="O'quv maqsadlarida foydalanish uchun Netflix API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact("Nurshodbek Shokirov,<nurshodbekshokirov@gmail.com>"),

   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('club/<int:pk>/', CLubAPIVIEW.as_view()),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('clubs/', ClublarAPIVIEW.as_view()),
    path('players/', PlayersAPIVIEW.as_view()),
    path('transfer/',TransferAPIVIEW.as_view()),
    path('mavsumlar/',Hozirgi_mavsumsAPIVIEW.as_view()),
    path('mavsum/<str:soz>/',Mavsumga_oidAPIVIEW.as_view()),
    path('u20age/',u20ageAPIVIEW.as_view()),
    path('stats/',statsAPIVIEW.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
