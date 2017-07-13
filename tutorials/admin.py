from django.contrib import admin
from .models import Tutorial, Step, Note, Interface, Contributor

admin.site.register(Tutorial)
admin.site.register(Step)
admin.site.register(Note)
admin.site.register(Interface)
admin.site.register(Contributor)
