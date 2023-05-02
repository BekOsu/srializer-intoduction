from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('', include('snippets.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

]
