from django.db import models
from django.utils import timezone
from django.conf import settings


class Contest(models.Model):
    name = models.CharField(max_length=256, default="")
    contest_type = models.CharField(max_length=20, default="")
    start = models.DateTimeField('date-published')
    length = models.DurationField()
    description = models.TextField(default="")
    status = models.CharField(max_length=20, default="active")
    participant = models.IntegerField()

    def __str__(self):
        return self.name

    def get_status(self):
        subtime = self.start - timezone.now()
        print(subtime.seconds)
        if subtime.seconds > 0:
            return "Before start {:.2f}".format(subtime.seconds / 3600) + " hours"
        else:
            subtime = timezone.now() - self.start
            print(subtime)
            if subtime < self.length:
                return "After end {}".format(subtime)
            return "Final standings"


class Exercise(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    code = models.CharField(max_length=10, default="")
    name = models.CharField(max_length=50, default="")
    solved = models.IntegerField()
    time_limit = models.IntegerField()
    memory_limit = models.IntegerField()
    description = models.TextField(default="")
    input = models.TextField(default="")
    output = models.TextField(default="")

    def __str__(self):
        return self.name

    @property
    def number_of_comments(self):
        return ExerciseComment.objects.filter(Exercise_post_connected=self).count()


class ExerciseComment(models.Model):
    Exercise_post_connected = models.ForeignKey(Exercise, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, editable=False,
                               blank=True)
    content = models.TextField(default="", null=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.author) + ', ' + self.Exercise_post_connected.description[:40]
