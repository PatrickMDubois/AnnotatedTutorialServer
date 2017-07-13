from .models import Tutorial, Contributor,Note
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TutorialSerializer, NoteSerializer, ContributorSerializer


@api_view(['GET'])
def tutorial(request, tutorial_id):
    try:
        t = Tutorial.objects.get(pk=tutorial_id)
        serializer = TutorialSerializer(t)
        return Response(serializer.data)
    except Tutorial.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def tutorials(request):

    t = Tutorial.objects.filter()
    serializer = TutorialSerializer(t, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def notes(request):
    serializer = NoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def change_note(request, note_id):
    try:

        n = Note.objects.get(pk=note_id)
    except Note.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = NoteSerializer(n, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def contributor(request, contributor_name):

    try:
        a = Contributor.objects.get(name__iexact=contributor_name)
        serializer = ContributorSerializer(a)
        return Response(serializer.data)
    except Contributor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

