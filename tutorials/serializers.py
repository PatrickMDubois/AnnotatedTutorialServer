from rest_framework import serializers
from .models import Tutorial, Step, Note


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note


class NestedNoteSerializer(serializers.ModelSerializer):
    replies = NoteSerializer(many=True)

    class Meta:
        model = Note


class StepSerializer(serializers.ModelSerializer):
    notes = NestedNoteSerializer(many=True)

    class Meta:
        model = Step


class TutorialSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True)
    notes = NestedNoteSerializer(many=True)

    class Meta:
        model = Tutorial
