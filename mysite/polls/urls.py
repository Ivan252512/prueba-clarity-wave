from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:choice_id>/vote/', views.vote, name='vote'),

    #Another views
    path('add_question/', views.AddQuestion.as_view(), name='add_question'),
    path('<int:question_id>/add_choice/', views.AddChoice.as_view(), name='add_choice'),
    path('<int:pk>/delete_question/', views.DeleteQuestion.as_view(), name='delete_question'),
    path('<int:pk>/delete_choice/', views.DeleteChoice.as_view(), name='delete_choice'),
]