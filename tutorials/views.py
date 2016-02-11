from json import loads
from .models import Tutorials, Steps, Notes
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def tutorial(request, tutorial_id):
    try:
        t = Tutorials.objects.get(pk=tutorial_id)
        serializer = TweetNestedSerializer(t)
        return Response(serializer.data)
    except Tutorials.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)