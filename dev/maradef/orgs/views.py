from django.shortcuts import render
from .models import Organization

# Create your views here.
def space(request):
    return render(request, 'space.html',{'space': Organization.objects.all()})
