from django.shortcuts import redirect
from django.db.utils import OperationalError
from .models import Index_Section

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def starter_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        if not Index_Section.objects.filter(page_name='index').exists():
            return redirect('get-started')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def initialized_starter(view_func):
    def wrapper_func(request, *args, **kwargs):
        if Index_Section.objects.filter(page_name='index').exists():
            return redirect('index')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func