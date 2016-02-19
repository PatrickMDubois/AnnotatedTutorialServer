from django.db import models


class Tutorial(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Step(models.Model):
    tutorial_id = models.ForeignKey(Tutorial, related_name='steps')
    html = models.TextField(default=None, null=True)

    def __str__(self):
        return self.html


class Note(models.Model):
    step_id = models.ForeignKey(Step, related_name='notes')
    category = models.CharField(max_length=50)
    software = models.CharField(max_length=50, blank=True)
    content = models.TextField(default=None, null=True)

    def __str__(self):
        return self.content
