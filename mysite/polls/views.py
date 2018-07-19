from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Question,Choice
from django.utils import timezone
from .forms import QuesForm,EditQues

def index(request):
    question_list=Question.objects.all()
    context={'question_list': question_list}
    return render(request,'polls/index.html',context)

def detail(request, question_id):
    if request.method=='GET':
        try:
            question = Question.objects.get(pk=question_id)
        except Question.DoesNotExist:
            raise Http404("Question does not exist")
        return render(request, 'polls/detail.html', {'question': question})
    else:
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            # Redisplay the question voting form.
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "You didn't select a choice.",
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect('/polls/')

def editques(request):
    if request.method=='GET':
        return render(request,'polls/addnew.html')
    else:
        print(type(request.POST['ques']))
        try:
            q=Question(question_text=request.POST['ques'],pub_date=timezone.now())
        except:
            return render(request,'/polls/addnew.html',{'error':'Add question'})
        else:
            q.save()
            return HttpResponseRedirect('/polls/')



def addnew(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = QuesForm(request.POST)
        if form.is_valid():
            a=form.cleaned_data['question']
            ch1=form.cleaned_data['Choice_1']
            ch2=form.cleaned_data['Choice_2']
            ch3=form.cleaned_data['Choice_3']
            q=Question.objects.create(question_text=a,pub_date=timezone.now())
            q.choice_set.create(choice_text=ch1, votes=0)
            q.choice_set.create(choice_text=ch2, votes=0)
            q.choice_set.create(choice_text=ch3, votes=0)
            return HttpResponseRedirect('/polls/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = QuesForm()

    return render(request, 'polls/addnew.html', {'form': form})

def edit_ques(request,question_id):
    if request.method=='GET':
        q=Question.objects.get(id=question_id)
        data={'question_edit':q.question_text}
        form=EditQues(initial=data)
        return render(request,'polls/editques.html',{'form':form})
    else:
        form=EditQues(request.POST)
        if form.is_valid():
            a=form.cleaned_data['question_edit']
            q=Question.objects.get(id=question_id)
            q.question_text=a
            q.save()
            return HttpResponseRedirect('/polls')
        else:
            return HttpResponseRedirect('/polls/addnew.html')

def delete_ques(request):
    id_number = request.GET.get('id_number', None)
    Question.objects.filter(pk=id_number).delete()
    data = {
        'is_deleted':True
    }
    return JsonResponse(data)
