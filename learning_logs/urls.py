"""Определение схемы URL для learning_logs"""

from django.urls import path
from . import views
#from .views import DeleteEntryView

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Topics page
    path('topics/', views.topics, name='topics'),
    # Страница с подробной информацией по отдельной теме
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Страница создания новой темы
    path('new_topic/', views.new_topic, name='new_topic'),
    # Страница для добавление новой записи в тему
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Страница для редактирования записи
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    # Удаление записи
    path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
    # Удаление записи встроенным методом
    # path('delete_entry/<int:pk>/', DeleteEntryView.as_view(success_url='/topics/'), name='delete_entry'),
]
