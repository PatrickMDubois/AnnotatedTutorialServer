from rest_framework import serializers
from .models import Tutorial, Step, Note


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ('step_id', 'tutorial_id', 'category', 'extra_info', 'content', 'author', 'user_submitted', 'reply_to', 'replies')

NoteSerializer._declared_fields['replies'] = NoteSerializer(many=True)


class StepSerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True)

    class Meta:
        model = Step


class TutorialSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True)
    notes = NoteSerializer(many=True)

    class Meta:
        model = Tutorial
