from rest_framework import serializers
from .models import Tutorial, Step, Note


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note


class StepSerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True)

    class Meta:
        model = Step


class TutorialSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True)
    notes = NoteSerializer(many=True)

    class Meta:
        model = Tutorial
