from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question


# Create your views here.


def index(request):
    myname = "Toan ne!"
    taisan = ['Tien', 'may tinh', 'maybay', 'cuc ki nhieu tien ']
    context = {"name": myname, "taisan": taisan}
    return render(request, "polls/index.html", context)


def viewlist(request):
    # list_question = get_object_or_404(Question)
    list_question = Question.objects.all()

    context = {"dsquest": list_question}
    return render(request, "polls/question_list.html", context)


def detailView(request, question_id):
    q = Question.objects.get(pk=question_id)
    return render(request, "polls/detail_question.html", {"qs": q})


def vote(request, question_id):
    q = Question.objects.get(pk=question_id)
    try:
        data = request.POST["choice"]

        c = q.choice_set.get(pk=data)
    except:
        HttpResponse("loi khong co con cac gi")
    c.vote = c.vote + 1
    c.save()
    return render(request, "polls/result.html", {"q": q, "r": c})
