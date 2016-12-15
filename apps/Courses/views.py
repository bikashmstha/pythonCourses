from django.shortcuts import render, redirect
from models import Course

# Create your views here.
def index(request):
	context = {
	"courses": Course.objects.all()
	}
	return render(request, 'Courses/index.html', context)

def addcourse(request):
	Course.objects.create(name=request.POST['name'], description=request.POST['description'])
	return redirect('/')

def show(request, id):
	context = {
	"course": Course.objects.get(id=id)
	}
	return render(request, 'Courses/show.html', context)

def delete(request, id):
	Course.objects.get(id=id).delete()
	return redirect('/')