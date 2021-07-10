from django.shortcuts import render, redirect  
from .forms import TransitionsForm, ReactionsForm, MusicForm
from .models import Transitions, Reactions, Music
from django.core import serializers
from django.http import HttpResponse
import json

# Create your views here.  
# ----- Transitions -----
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
    return render(request,'transitions/index.html',{'form':form})  

def showTransitions(request):
    transitions = Transitions.objects.all()
    return render(request,"transitions/show.html",{'transitions':transitions})  

def editTransition(request, id):  
    transition = Transitions.objects.get(id=id)
    request.FILES['filename'] = transition.filename
    request.FILES['thumbnail'] = transition.thumbnail
    return render(request,'transitions/edit.html', {'transition':transition})  

def updateTransition(request, id):  
    transition = Transitions.objects.get(id=id)  
    form = TransitionsForm(request.POST, request.FILES, instance = transition)  
    if form.is_valid():  
        form.save()  
        return redirect("/transitions")  
    return render(request, 'transitions/edit.html', {'transition': transition})  

def destroyTransition(request, id):  
    transition = Transitions.objects.get(id=id)  
    transition.delete()  
    return redirect("/transitions")

def downloadJsonTransitions(request):
    try:
        transitions = Transitions.objects.all()
        data = serializers.serialize("json", transitions)

        j = json.loads(data)

        for element in j:
            element['id'] = element['pk']
            element['priority'] = float(element['fields']['priority'])
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
# ---------------------
# ----- Reactions -----
def reactions(request):  
    if request.method == "POST":  
        form = ReactionsForm(request.POST, request.FILES)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/reactions')  
            except:  
                pass  
    else:  
        form = ReactionsForm()  
    return render(request,'reactions/index.html',{'form':form})  

def showReactions(request):
    reactions = Reactions.objects.all()
    return render(request,"reactions/show.html",{'reactions':reactions})  

def editReaction(request, id):  
    reaction = Reactions.objects.get(id=id)
    request.FILES['filename'] = reaction.filename
    request.FILES['thumbnail'] = reaction.thumbnail
    return render(request,'reactions/edit.html', {'reaction':reaction})  

def updateReaction(request, id):  
    reaction = Reactions.objects.get(id=id)  
    form = ReactionsForm(request.POST, request.FILES, instance = reaction)  
    if form.is_valid():  
        form.save()  
        return redirect("/reactions")  
    return render(request, 'reactions/edit.html', {'reaction': reaction})  

def destroyReaction(request, id):  
    reaction = Reactions.objects.get(id=id)  
    reaction.delete()  
    return redirect("/reactions")

def downloadJsonReactions(request):
    try:
        reactions = Reactions.objects.all()
        data = serializers.serialize("json", reactions)

        j = json.loads(data)

        for element in j:
            element['id'] = element['pk']
            element['priority'] = float(element['fields']['priority'])
            element['name'] = element['fields']['name']
            element['filename'] = element['fields']['filename']
            element['thumbnail'] = element['fields']['thumbnail']
            element.pop('pk', None)
            element.pop('model', None)
            element.pop('fields', None)

        data={}
        data['reactions'] = j
        data = json.dumps(data)

        response = HttpResponse(data, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename=reactions.json'
        return response
    except Exception:
        raise
# ---------------------
# ------- Music -------
def music(request):  
    if request.method == "POST":  
        form = MusicForm(request.POST, request.FILES)  
        if form.is_valid():  
            try:  
                form.instance.type =  form.instance.type.lower().capitalize()
                form.save()  
                return redirect('/music')  
            except:  
                pass  
    else:  
        form = MusicForm()  
    return render(request,'music/index.html',{'form':form})  

def showMusic(request):
    music = Music.objects.all()
    return render(request,"music/show.html",{'music':music})  

def editMusic(request, id):  
    music = Music.objects.get(id=id)
    request.FILES['filename'] = music.filename
    request.FILES['thumbnail'] = music.thumbnail
    return render(request,'music/edit.html', {'music':music})  

def updateMusic(request, id):  
    reaction = Music.objects.get(id=id)  
    form = MusicForm(request.POST, request.FILES, instance = reaction)  
    if form.is_valid():  
        form.instance.type =  form.instance.type.lower().capitalize()
        form.save()  
        return redirect("/music")  
    return render(request, 'music/edit.html', {'music': music})  

def destroyMusic(request, id):  
    music = Music.objects.get(id=id)  
    music.delete()  
    return redirect("/music")

def downloadJsonMusic(request):
    try:
        music = Music.objects.all()
        data = serializers.serialize("json", music)

        j = json.loads(data)
        types = {}

        for element in j:
            types[element['fields']['type']] = []

        for element in j:
            element['id'] = element['pk']
            element['priority'] = float(element['fields']['priority'])
            element['name'] = element['fields']['name']
            element['filename'] = element['fields']['filename']
            element['thumbnail'] = element['fields']['thumbnail']
            element['type'] = element['fields']['type']

            element.pop('pk', None)
            element.pop('model', None)
            element.pop('fields', None)

            types[element['type']].append(element)

        data={}
        data['music'] = types
        data = json.dumps(data)

        response = HttpResponse(data, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename=music.json'
        return response
    except Exception:
        raise
# ---------------------
# ------- Common ------
def downloadAllAsJSON(request):
    try:
        transitions = Transitions.objects.all()
        reactions = Reactions.objects.all()
        music = Music.objects.all()

        transitionData = json.loads(serializers.serialize("json", transitions))
        reactionsData = json.loads(serializers.serialize("json", reactions))
        musicData = json.loads(serializers.serialize("json", music))

        data = {}

        #transitions

        for element in transitionData:
            element['id'] = element['pk']
            element['priority'] = float(element['fields']['priority'])
            element['name'] = element['fields']['name']
            element['filename'] = element['fields']['filename']
            element['thumbnail'] = element['fields']['thumbnail']
            element.pop('pk', None)
            element.pop('model', None)
            element.pop('fields', None)
        
        data['transitions'] = transitionData

        #reactions

        for element in reactionsData:
            element['id'] = element['pk']
            element['priority'] = float(element['fields']['priority'])
            element['name'] = element['fields']['name']
            element['filename'] = element['fields']['filename']
            element['thumbnail'] = element['fields']['thumbnail']
            element.pop('pk', None)
            element.pop('model', None)
            element.pop('fields', None)
        
        data['reactions'] = reactionsData

        #music

        types = {}

        for element in musicData:
            types[element['fields']['type']] = []

        for element in musicData:
            element['id'] = element['pk']
            element['priority'] = float(element['fields']['priority'])
            element['name'] = element['fields']['name']
            element['filename'] = element['fields']['filename']
            element['thumbnail'] = element['fields']['thumbnail']
            element['type'] = element['fields']['type']

            element.pop('pk', None)
            element.pop('model', None)
            element.pop('fields', None)

            types[element['type']].append(element)

        data['music'] = types

        #merge and download

        data = json.dumps(data)

        response = HttpResponse(data, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename=all_data.json'
        return response
    except Exception:
        raise
