from json import loads
from .models import Tutorial, Step, Note
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TutorialSerializer


@api_view(['GET'])
def tutorial(request, tutorial_id):
    try:
        t = Tutorial.objects.get(pk=tutorial_id)
        serializer = TutorialSerializer(t)
        return Response(serializer.data)
    except Tutorial.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)