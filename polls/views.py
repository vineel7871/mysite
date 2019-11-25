from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from polls.models import Question, Choice
from django.urls import reverse


# Created view here using template.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context,request))


def detail(request, question_id):
    # return HttpResponse("You are looking at question %s"%question_id)
    # try:
    #     question_requested = Question.objects.get(pk=question_id)
    #     question_choices = question_requested.choice_set.all()
    # except Exception as e:
    #     return HttpResponse("question with this id not found")
    question = get_object_or_404(Question, pk=question_id)
    question_choices = question.choice_set.all()
    context = {
        "question": question
    }
    return HttpResponse(render(request, "polls/details.html", context))


def results(request, question_id):
    # return HttpResponse("You are looking at results of question %s"%question_id)
    question = get_object_or_404(Question, pk=question_id)
    return HttpResponse(render(request, "polls/results.html", {"question": question}))


def vote(request, question_id):
    # return HttpResponse("You are looking to vote for question %s"%question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        question_choices = question.choice_set.all()
        return render(request, 'polls/details.html', {
            "question": question,
            "error_message": "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))