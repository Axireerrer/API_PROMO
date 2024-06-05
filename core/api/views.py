from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_403_FORBIDDEN
from django.db import DatabaseError
from rest_framework.exceptions import NotFound

from api.models import Advert
from api.serializers import AdvertSerializer


# API для выдачи информации в JSON об объявлении с переданным параметром ID
class AdvertAPI(APIView):

    def get(self, request, some_pk):
        user = self.request.user
        if user.is_authenticated:
            try:
                advert = Advert.objects.get(advert_id=some_pk)
                serializer = AdvertSerializer(advert)
                return Response(serializer.data, status=HTTP_200_OK)
            except [ObjectDoesNotExist, DatabaseError, NotFound] as e:
                return Response({'Error': f'It was called an exception {e}'}, status=HTTP_403_FORBIDDEN)
        elif user is None:
            return Response(status=HTTP_403_FORBIDDEN)
        else:
            return Response(status=HTTP_403_FORBIDDEN)
