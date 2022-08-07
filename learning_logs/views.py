from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.

def index(request):
    """ Домашняя страница приложения Learning Log"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Выводит список тем"""
    topics = Topic.objects.order_by('date_added')
    context = {"topics": topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Вывод всех записей одной темы"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """Определение новой темы"""
    if request.method != 'POST':
        # Если данные не отправляются - создается пустая форма
        form = TopicForm()
    else:
        # Отправка данных POST; обработка данных
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    # Вывод пустой или недействительной формы
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    """Добавление новой записи в определенной теме"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # Если данные не отправляются, создается пустая форма
        form = EntryForm()
    else:
        # При отправке данных методом POST происходит обработка данных
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # Вывод пустой или недействительной формы
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


def edit_entry(request, entry_id):
    """Редактирование существующей записи"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method != 'POST':
        # Исходный запрос; форма заполняется данными текузей записи
        form = EntryForm(instance=entry)
    else:
        # Отправка данных POST; обработать данные
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
