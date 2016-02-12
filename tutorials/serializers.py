from rest_framework import serializers
from .models import Tutorial, Step, Note


class TutorialSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    retweeted_by = AuthorSerializer(many=True)

    class Meta:
        model = Tutorial