from rest_framework import serializers
from .models import Tutorial, Step, Note, Contributor


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note


class NestedNoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note

NestedNoteSerializer._declared_fields['replies'] = NestedNoteSerializer(many=True)


class StepSerializer(serializers.ModelSerializer):
    notes = NestedNoteSerializer(many=True)

    class Meta:
        model = Step


class TutorialSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True)
    notes = NestedNoteSerializer(many=True)

    class Meta:
        model = Tutorial


class ContributorSerializer(serializers.ModelSerializer):
    current_tutorial = TutorialSerializer()

    class Meta:
        model = Contributor
