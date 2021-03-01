from django.http import HttpResponseRedirect
from django.shortcuts import render
from list_app.models import status_choices, List


def index_view(request):
    lists = List.objects.all()
    return render(request, 'index.html', context={'lists': lists})


def index_view_list(request, id):
    list = List.objects.get(id=id)
    return render(request, 'list_view.html', {'list': list})


def list_create(request):
    if request.method == "GET":
        return render(request, 'list_create.html', {'status': status_choices})
    elif request.method == "POST":
        list_text = request.POST.get("text")
        status = request.POST.get("select")
        description = request.POST.get("des")
        created_at = request.POST.get("date")

        lists = List.objects.create(
            list=list_text,
            status=status,
            description=description,
            created_at=created_at
        )
        return render(request, 'list_create.html', {'lists': lists})
