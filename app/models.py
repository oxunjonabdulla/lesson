from django.db import models

class Lesson(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class HomeworkFile(models.Model):
    FILE_TYPES = (
        ('image', 'Image'),
        ('audio', 'Audio'),
    )

    lesson = models.ForeignKey(Lesson, related_name='files', on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10, choices=FILE_TYPES)
    file = models.FileField(upload_to='homeworks/')
    audio_title = models.CharField(max_length=200, blank=True)
    homework_number = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.lesson.title} - {self.file_type}"
