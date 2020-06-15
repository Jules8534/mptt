from django.shortcuts import render
from genre.models import FileObject
from genre.forms import FileAddForm
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
#Received help from Matt and Peter for HTML


def index(request):
    html = 'homepage.html'
    data = FileObject.objects.all()
    return render(request, html, {"data": data})

def add_file(request):
    form = None
    if request.method == "POST":
        form = FileAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_file = File.objects.create(
                name=data["name"],
                parent=data["parent"]
            )
        return HttpResponseRedirect(reverse('homepage'))
    else:
        form = FileAddForm()
    return render(request, "add_file.html", {"form": form})

