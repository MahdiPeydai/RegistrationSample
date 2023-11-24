from django.views import View
from django.shortcuts import render

from rest_framework import generics
from Authentication.models import User
from .serializers import UserSerializer
from .permissions import IsAdmin


class PanelView(View):
    def get(self, request):
        return render(request, 'panel/admin_panel.html')


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]
