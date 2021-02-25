from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .api_urls import router



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('todo/', include('todo.urls', namespace='todo')),
    path('api/', include(router.urls)),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('api-auth', include('rest_framework.urls'))
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
