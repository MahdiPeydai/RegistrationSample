from django.urls import path

from .views import *


urlpatterns = [
    path('', PanelView.as_view(), name='panel'),
    path('user/<int:pk>/edit', UserUpdateView.as_view(), name='user_edit'),
    path('API/user/<int:pk>/', UserDetail.as_view(), name='user_detail')
]
