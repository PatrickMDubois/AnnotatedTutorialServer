from .models import Tutorial
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TutorialSerializer
from .serializers import NoteSerializer


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
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)