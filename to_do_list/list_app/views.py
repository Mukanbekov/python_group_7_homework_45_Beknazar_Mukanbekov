from django.http import HttpResponseRedirect
from django.shortcuts import render
from list_app.models import status_choices, List


def index_view(request):
    lists = List.objects.all()
    for list1 in lists:
        date = list1.created_at
    return render(request, 'index.html', context={'lists': lists})


def list_create(request):
    if request.method == "GET":
        return render(request, 'list_create.html', {'status': status_choices})
    elif request.method == "POST":
        list_text = request.POST.get("text")
        status = request.POST.get("select")
        created_at = request.POST.get("date")

        lists = List.objects.create(
            list=list_text,
            status=status,
            created_at=created_at
        )
        return render(request, 'list_create.html', {'lists': lists})
