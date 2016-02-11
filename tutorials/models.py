from django.db import models


class Tutorials(models.Model):
    tutorial_id = models.CharField(primary_key=True, max_length=50)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Steps(models.Model):
    step_id = models.CharField(primary_key=True, max_length=50)
    tutorial_id = models.ForeignKey(Tutorials, db_column='tutorial_id')
    html = models.TextField(default=None, null=True)

    def __str__(self):
        return self.html


class Notes(models.Model):
    note_id = models.CharField(primary_key=True, max_length=50)
    step_id = models.ForeignKey(Steps, db_column='step_id')
    category = models.CharField(max_length=50)
    software = models.CharField(max_length=50)
    content = models.TextField(default=None, null=True)

    def __str__(self):
        return self.content
