from django.shortcuts import render, redirect  
from .forms import TransitionsForm  
from .models import Transitions  
from django.core import serializers
from django.http import HttpResponse
import json

# Create your views here.  
def transitions(request):  
    if request.method == "POST":  
        form = TransitionsForm(request.POST, request.FILES)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/transitions')  
            except:  
                pass  
    else:  
        form = TransitionsForm()  
    return render(request,'index.html',{'form':form})  

def show(request):
    transitions = Transitions.objects.all()
    return render(request,"show.html",{'transitions':transitions})  

def edit(request, id):  
    transition = Transitions.objects.get(id=id)
    request.FILES['filename'] = transition.filename
    request.FILES['thumbnail'] = transition.thumbnail
    return render(request,'edit.html', {'transition':transition})  

def update(request, id):  
    transition = Transitions.objects.get(id=id)  
    form = TransitionsForm(request.POST, request.FILES, instance = transition)  
    if form.is_valid():  
        form.save()  
        return redirect("/transitions")  
    return render(request, 'edit.html', {'transition': transition})  

def destroy(request, id):  
    transition = Transitions.objects.get(id=id)  
    transition.delete()  
    return redirect("/transitions")

def downloadJson(request):
    try:
        transitions = Transitions.objects.all()
        data = serializers.serialize("json", transitions)

        j = json.loads(data)

        for element in j:
            element['id'] = element['pk']
            element['priority'] = element['fields']['priority']
            element['name'] = element['fields']['name']
            element['filename'] = element['fields']['filename']
            element['thumbnail'] = element['fields']['thumbnail']
            element.pop('pk', None)
            element.pop('model', None)
            element.pop('fields', None)

        data={}
        data['transitions'] = j
        data = json.dumps(data)

        response = HttpResponse(data, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename=transitions.json'
        return response
    except Exception:
        raise