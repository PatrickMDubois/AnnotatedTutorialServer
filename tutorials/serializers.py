from rest_framework import serializers
from .models import Tutorial, Step, Note,Interface, Contributor


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

class InterfaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interface


class ContributorSerializer(serializers.ModelSerializer):
    current_tutorial = TutorialSerializer()
    tutorial_one = TutorialSerializer()
    tutorial_two = TutorialSerializer()
    tutorial_three = TutorialSerializer()
    interface_one = InterfaceSerializer()
    interface_two = InterfaceSerializer()
    interface_three = InterfaceSerializer()
    current_interface = InterfaceSerializer()

    class Meta:
        model = Contributor
