from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    myname = "Toan ne!"
    taisan = ['Tien', 'may tinh', 'maybay','cuc ki nhieu tien ']
    context = {"name": myname, "taisan": taisan}
    return render(request, "polls/index.html", context)
