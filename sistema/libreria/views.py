from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Libro, Autor
from .forms import LibroForm
import json
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

# urls para libros
def libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/index.html', {'libros': libros})

def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    autor = Autor.objects.all()
    if formulario.is_valid():
       formulario.save()
       return redirect('libros')
    return render(request, 'libros/crear.html', {'formulario': formulario, 'autor': autor})
    
def editar(request, id):
    libro = Libro.objects.get(id=id)
    autor = Autor.objects.all()
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        libro.save()
        return redirect('libros')
    return render(request, 'libros/editar.html', {'formulario': formulario, 'autor': autor})

def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')



class AutorApi(View):
    #se ejecuta cada vez que se haga una petición
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if(id > 0):
            autores = list(Autor.objects.filter(id=id).values())
            if len(autores) > 0:
                autor = autores[0]
                datos={'message':"Success",'Autor':autor}  
            else:
                datos={'message': "Autor not found"}
            return JsonResponse(datos) 
           
        else:          
           autores = list(Autor.objects.values())
           if len(autores) > 0:
               datos={'message':"Success",'Autores':autores}
           else:
                datos={'message': "Autores not found"}
           return JsonResponse(datos) 
      
    def post(self, request):
        datos={'message':"Success"}
        jd = json.loads(request.body)
        Autor.objects.create(nombre=jd['nombre'], nacimiento=jd['nacimiento'])
        return JsonResponse(datos)
    
    def put(self, request, id):
        jd = json.loads(request.body)
        autores = list(Autor.objects.filter(id=id).values())
        if len(autores) > 0:
           autor = Autor.objects.get(id=id)
           autor.nombre=jd['nombre']
           autor.nacimiento=jd['nacimiento']
           autor.save()
           datos={'message':"Success"}
               
        else:
             datos={'message': "Autor not found"}     
        return JsonResponse(datos)
    
    def delete(self, request, id):
        autores = list(Autor.objects.filter(id=id).values())
        if len(autores) > 0:
           Autor.objects.filter(id=id).delete()
           datos={'message':"Success"}
        else:
            datos={'message': "Autor not found"}
        return JsonResponse(datos)