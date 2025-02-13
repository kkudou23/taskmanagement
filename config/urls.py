from django.contrib import admin
from django.urls import path, include
from task.views import custom_permission_denied_view, custom_page_not_found_view

urlpatterns = [
    path('', include('task.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]

handler403 = 'task.views.custom_permission_denied_view'
handler404 = 'task.views.custom_page_not_found_view'