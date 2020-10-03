from django.urls import path
from to_do import views


app_name = 'to_do'
urlpatterns = [
    path('', views.TodoListView.as_view(), name='todo_list'),
    path('update/<int:year>/<int:month>/<int:day>/<slug:slug>', views.TodoUpdateView.as_view(), name='todo_update'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>', views.TodoDetailView.as_view(), name='todo_detail'),
    path('New', views.TodoCreateView.as_view(), name='todo_create'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/active', views.TodoUpdateView.as_view(), name='active_update'),

]