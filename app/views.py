
from django.shortcuts import render, get_object_or_404
from .models import Lesson

def home(request):
    lessons = Lesson.objects.all()
    return render(request, 'app/home.html', {'lessons': lessons})

def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    return render(request, 'app/lesson_detail.html', {'lesson': lesson})
