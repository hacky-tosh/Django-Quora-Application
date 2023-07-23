from django.urls import path
from . import views
from .views import QuestionListView, QuestionDetailView, QuestionCreateView, QuestionUpdateView, QuestionDeleteView, UserQuestionListView, answer_question, like_answer

urlpatterns = [
    path('', QuestionListView.as_view(), name='quora-home'),
    path('user/<str:username>/', UserQuestionListView.as_view(), name='user-questions'),
    path('question/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
    path('question/new/', QuestionCreateView.as_view(), name='question-create'),
    path('question/<int:pk>/update/', QuestionUpdateView.as_view(), name='question-update'),
    path('question/<int:pk>/delete/', QuestionDeleteView.as_view(), name='question-delete'),
    path('question/<int:pk>/answer/', answer_question, name='question-answer'),
    path('answer/<int:pk>/like/', like_answer, name='answer-like'),
]
