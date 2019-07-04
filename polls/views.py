from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

from django.urls import reverse_lazy
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, choice_id):
    selected_choice = get_object_or_404(Choice, id=choice_id)
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('detail', args=(selected_choice.question.id,)))

#Another views
class AddQuestion(generic.CreateView):
    model = Question
    fields = ['question_text']
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.pub_date = timezone.now()
        return super().form_valid(form)

class DeleteQuestion(generic.DeleteView):
    model = Question
    success_url = reverse_lazy('index')

class AddChoice(generic.CreateView):
    model = Choice
    fields = ['choice_text']
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.question = get_object_or_404(Question, id=self.kwargs['question_id'])
        return super().form_valid(form)

class DeleteChoice(generic.DeleteView):
    model = Choice
    success_url = reverse_lazy('index')
