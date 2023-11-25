from django.views import View
from django.shortcuts import render
from rest_framework import generics

from Authentication.models import User
from .forms import UserUpdateForm
from .serializers import UserSerializer
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required


@method_decorator(permission_required('is_superuser'), name='dispatch')
class PanelView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'panel/admin_panel.html', {'users': users})


@method_decorator(permission_required('is_superuser'), name='dispatch')
class UserUpdateView(View):
    def get(self, request, pk):
        user = User.objects.get(id=pk)
        form = UserUpdateForm(instance=user)
        return render(request, 'panel/edit_page.html', {'form': form, 'pk': pk})


@method_decorator(permission_required('is_superuser'), name='dispatch')
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
