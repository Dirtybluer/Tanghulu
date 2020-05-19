from django.urls import path
from comment import views

urlpatterns = [
    path('create/', views.create),
    path('read_by_activity/', views.read_by_activity),
    path('read_by_user/', views.read_by_user),
    path('update/', views.update),
    path('delete/', views.delete),
    path('reply_create/', views.reply_create),
    path('reply_read/', views.reply_read),
    path('reply_update/', views.reply_update),
    path('reply_delete/', views.reply_delete),
    path('like/', views.like),
    path('reply_like/', views.reply_like),
]
