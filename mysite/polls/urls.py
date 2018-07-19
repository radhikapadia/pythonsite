from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('addnew/',views.addnew,name='addnew'),
    path('editques/<int:question_id>/',views.edit_ques,name='edit_ques'),
    path('deleteques/',views.delete_ques,name='delete_ques'),
    path('thanks/',views.index,name='thanks'),
]
