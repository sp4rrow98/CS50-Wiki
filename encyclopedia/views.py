from logging import exception
from django.forms.widgets import Widget
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.contrib import messages
from django.urls import reverse
from . import views
import random

from . import util

from markdown2 import Markdown, markdown

markdowner = Markdown()

class Search(forms.Form):
    item = forms.CharField(widget=forms.TextInput(attrs={'class' : 'myfieldclass', 'placeholder': 'Search'}))

class Post(forms.Form):
    title = forms.CharField(widget = forms.Textarea, label='')
    textarea = forms.CharField(widget = forms.Textarea, label='')

class Edit(forms.Form):
    textarea = forms.CharField(widget = forms.Textarea, label='')
    

def index(request):
    entries = util.list_entries()
    searched = []
    if request.method == "POST":
        form = Search(request.POST)
        if form.is_valid():
            search = form.cleaned_data["item"]
            for i in entries:
                if search in entries:
                    page = util.get_entry(search)
                    page_converted = markdowner.convert(page)
                    context = {
                        'page': page_converted,
                        'title': search,
                        'form': Search()
                    }
                    return render(request, "encyclopedia/entry.html", context)
                if search.lower() in i.lower():
                    searched.append(i)
                    context = {
                        'searched': searched,
                        'form': Search()
                    }
                    return render(request, "encyclopedia/search.html", context)
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": Search()
    })
    

def entry(request, entry):
    entryPage = util.get_entry(entry)
    if entryPage is None:
        message = messages.warning(request, 'There is not a page with this name.')
        return render(request, 'encyclopedia/error.html', {
            'entryTitle': entry,
            'message': message,
            'form': Search()
        })
    else:
        return render(request, 'encyclopedia/entry.html',{
            'entry': markdowner.convert(entryPage),
            'title': entry,
            'form': Search()
        })

def new(request):
    if request.method == 'POST':
        # Get the form
        form = Post(request.POST)
        if form.is_valid():
            # Clean the form
            title = form.cleaned_data['title']
            lower_title = form.cleaned_data['title'].lower()
            text = form.cleaned_data['textarea']
            entries = util.list_entries()
            # Check for existing entry
            for entry in entries:
                if lower_title == entry.lower():
                    message = messages.warning(request, "There is already a page with this name.")
                    context = {
                        'message': message,
                        "form": Search(),
                        "post": Post()
                    }
                    return render(request, 'encyclopedia/new.html',context)
            # Create and redirect to new entry
                else:
                    util.save_entry(title,text)
                    return HttpResponseRedirect(reverse("entry", args=[title]))
    else: 
        return render(request, 'encyclopedia/new.html', {
            "form": Search(),
            "post": Post()
        })

def error(request):
    return render(request, 'encyclopedia/error.html')


def edit(request, title):
    if request.method == "GET":
        page = util.get_entry(title)
        # page_converted = markdowner.convert(page)
        context = {
            'form': Search(),
            'edit': Edit({'textarea': page}),
            'title': title
        }
        return render(request, "encyclopedia/edit.html", context)
    else:
        form = Edit(request.POST)
        entries = util.list_entries()
        if form.is_valid():     
            text = form.cleaned_data["textarea"]   
            if title in entries:
                util.save_entry(title, text)
                return HttpResponseRedirect(reverse("entry", args=[title]))

def random_page(request):
    entries  = util.list_entries()
    randomize = random.randint(0, len(entries) - 1)
    random_page = entries[randomize]
    return HttpResponseRedirect(reverse("entry", args=[random_page]))