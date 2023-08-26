import markdown
import random

from random import choice
from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def conversion(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)


def name(request, title):
    html = conversion(title)
    if html == None:
        return render(request, "encyclopedia/error.html", {
            "message": "This entry does not exist"
        })
    else:
        return render(request, "encyclopedia/name.html", {
            "title": title,
            "content": html
        })


def search(request):
    if request.method == "POST":
        search = request.POST['q']
        html = conversion(search)
        if html is not None:
            return render(request, "encyclopedia/name.html", {
                "title": search,
                "content": html
            })
        else:
            allvalue = util.list_entries()
            recommendation = []
            for name in allvalue:
                if search.lower() in name.lower():
                    recommendation.append(name)
            return render(request, "encyclopedia/search.html", {
                "recommendation": recommendation
            })


def newpage(request):
    if request.method == "GET":
        return render(request, "encyclopedia/newpage.html")
    else:
        title = request.POST['title']
        content = request.POST['content']
        titleexist = util.get_entry(title)
        if titleexist is not None:
            return render(request, "encyclopedia/error.html", {
                "message": "Entry already exist"
            })
        else:
            util.save_entry(title, content)
            html = conversion(title)
            return render(request, "encyclopedia/name.html", {
                "title": title,
                "content": html
            })


def edit(request):
    if request.method == 'POST':
        title = request.POST['entry_title']
        content = util.get_entry(title)
    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "content": content
    })


def saveedit(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        html = conversion(title)
        return render(request, "encyclopedia/name.html", {
            "title": title,
            "content": html
        })


def ran(request):
    allentries = util.list_entries()
    ranentries = random.choice(allentries)
    html = conversion(ranentries)
    return render(request, "encyclopedia/name.html", {
        "title": ranentries,
        "content": html
    })
