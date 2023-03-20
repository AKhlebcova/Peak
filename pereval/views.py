from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError, APIException
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from pereval.serializers import *
from pereval.models import *






class UsersViewset(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    # def create(self, request, *args, **kwargs):
    #     print('1111!!')
    #     return super().create(request, *args, **kwargs)


class CoordsViewset(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer


class AddViewset(viewsets.ModelViewSet):
    queryset = Add.objects.all()
    serializer_class = AddSerializer

    def get_queryset(self):
        queryset = Add.objects.all()
        email = self.request.query_params.get('user__email', None)
        if email is not None:
            queryset = queryset.filter(user__email=email)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            # raise APIException(detail='ssss')
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            response_data = {'status': 200, 'message': 'Отправлено успешно', 'id': serializer.instance.id}
            headers = self.get_success_headers(serializer.data)
            return Response(response_data, status=status.HTTP_200_OK, headers=headers)
        except APIException as exc:
            response_data = {'status': exc.status_code, 'message': exc.detail, 'id': None}
            return Response(response_data, status=exc.status_code)

    def partial_update(self, request, pk=None):
        object_status = self.get_object().status
        if object_status == 'new':
            user = Users(**request.data.get('user'))
            if user == self.get_object().user:
                self.update(request)
                response_data = {'state': '1'}
                return Response(response_data)
            else:
                response_data = {'state': '0', 'message': 'невозможно изменить данные о пользователе'}
                return Response(response_data)
        else:
            response_data = {'state': '0', 'message': 'изменять можно толь в статусе new'}
            return Response(response_data)






class ImagesViewset(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


from django.shortcuts import render

# Create your views here.
