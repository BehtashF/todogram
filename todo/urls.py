from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'todo'
urlpatterns = [
    path('create-new-task/', views.create_task, name='create_task'),
    path('update/<int:id>/', views.update_task, name='update_task'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('trash/', views.trash_tasks, name='trash_tasks'),
    path('trash/restore/<int:id>/', views.restore_task, name='restore_task'),
    path('trash/remove/<int:id>/', views.complete_remove, name='complete_remove'),
    path('archive/', views.archive_tasks, name='archive_tasks'),
    path('to-archive/<int:id>/', views.archive_task, name='archive_task'),
    path('archive/restore/<int:id>/', views.archive_restore_tasks, name='archive_restore_tasks'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)