from django.db import models


class Tutorial(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Step(models.Model):
    tutorial_id = models.ForeignKey(Tutorial, related_name='steps')
    html = models.TextField(default=None, null=True)
    step_number = models.CharField(max_length = 50,blank=True)

    def __str__(self):
        return str(self.tutorial_id) + " " + str(self.step_number)


class Interface(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Contributor(models.Model):
    name = models.CharField(max_length=50)
    current_tutorial = models.ForeignKey(Tutorial, related_name='has_access', null=True, blank=True)
    active = models.BooleanField(default = True)
    tutorial_one = models.ForeignKey(Tutorial, related_name='tutorialOne', null=True, blank=True)
    tutorial_two = models.ForeignKey(Tutorial, related_name='tutorialTwo', null=True, blank=True)
    tutorial_three = models.ForeignKey(Tutorial, related_name='tutorialThree', null=True, blank=True)
    interface_one = models.ForeignKey(Interface, related_name='interfaceOne', null=True, blank=True)
    interface_two = models.ForeignKey(Interface, related_name='interfaceTwo', null=True, blank=True)
    interface_three = models.ForeignKey(Interface, related_name='interfaceThree', null=True, blank=True)
    current_interface = models.ForeignKey(Interface, related_name='interface_access', null=True, blank=True)

    def __str__(self):
        return self.name


class Note(models.Model):
    step_id = models.ManyToManyField(Step, related_name='notes', blank=True)
    tutorial_id = models.ForeignKey(Tutorial, related_name='notes')
    category = models.CharField(max_length=50)
    extra_info = models.CharField(max_length=50, blank=True)
    content = models.TextField(default=None, null=True)
    contributor = models.CharField(max_length=50)
    user_submitted = models.BooleanField(default=True)
    reply_to = models.ForeignKey('self', related_name="replies", null=True, blank=True)
    deleted = models.BooleanField(default=False)
    dateSubmitted = models.CharField(max_length=50, blank=True, default='***')
    contributor_list = models.ManyToManyField(Contributor, default=None, related_name='contributors', blank=True)

    def __str__(self):
        return str(self.content)