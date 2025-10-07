from django.shortcuts import render

from .models import Usuario
# Create your views here.
def index(request):

    usuarios = Usuario.objects.all()
    
    return render(request, "index.html", {"usuarios": usuarios})
