from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Question, Answer, AnswerLike
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


def home(request):
    context = {
        'questions': Question.objects.all()
    }
    return render(request, 'quora/home.html', context)


class QuestionListView(ListView):
    model = Question
    template_name = 'quora/home.html'
    context_object_name = 'questions'
    ordering = ['-date_posted']
    paginate_by = 3


class UserQuestionListView(ListView):
    model = Question
    template_name = 'quora/user_questions.html'
    context_object_name = 'questions'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Question.objects.filter(author=user).order_by('-date_posted')


class QuestionDetailView(DetailView):
    model = Question

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = self.object
        user = self.request.user
        if user.is_authenticated:
            liked_answers = AnswerLike.objects.filter(user=user, answer__question=question).values_list('answer__id', flat=True)
        else:
            liked_answers = []
        context['user'] = user
        context['liked_answers'] = liked_answers
        return context


class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class QuestionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Question
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.author:
            return True
        return False


class QuestionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Question
    success_url = reverse_lazy('quora-home')

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.author:
            return True
        return False




@login_required
def answer_question(request, pk):
    question = get_object_or_404(Question, pk=pk)

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            answer = Answer.objects.create(
                content=content, author=request.user, question=question
            )
            answer.save()

    return redirect('question-detail', pk=question.pk)


@login_required
def like_answer(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    user = request.user

    try:
        like = AnswerLike.objects.get(user=user, answer=answer)
        like.delete()
    except AnswerLike.DoesNotExist:
        like = AnswerLike.objects.create(user=user, answer=answer)
        like.save()

    return redirect('question-detail', pk=answer.question.pk)
