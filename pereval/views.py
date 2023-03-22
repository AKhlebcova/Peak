from django.utils.decorators import method_decorator
from drf_yasg import openapi

from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status, mixins
from rest_framework.exceptions import ValidationError, APIException
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from pereval.serializers import *
from pereval.models import *

user_email = openapi.Parameter('user__email', in_=openapi.IN_QUERY,
                               description='Возвращает выборку перевалов, добавленных определенным пользователем по email',
                               required=False, type=openapi.TYPE_STRING)
schema_submit = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'status': openapi.Schema(
            type=openapi.TYPE_INTEGER
        ),
        'message': openapi.Schema(
            type=openapi.TYPE_STRING
        ),
        'id': openapi.Schema(
            type=openapi.TYPE_INTEGER
        )
    }
)
schema_update = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'state': openapi.Schema(
            type=openapi.TYPE_INTEGER
        ),
        'message': openapi.Schema(
            type=openapi.TYPE_STRING
        )
    }
)


class MyViewSet(mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.ListModelMixin,
                GenericViewSet):
    pass


@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description='Возвращает описание всех добавленных перевалов', manual_parameters=[user_email],
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_description='Возвращает всю информацию об объекте, в том числе статус модерации по её id'
))
class AddViewset(MyViewSet):
    queryset = Add.objects.all()
    serializer_class = AddSerializer

    def _update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def get_queryset(self):
        queryset = Add.objects.all()
        email = self.request.query_params.get('user__email', None)
        if email is not None:
            queryset = queryset.filter(user__email=email)
        return queryset

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: schema_submit,
            status.HTTP_400_BAD_REQUEST: schema_submit,
            status.HTTP_500_INTERNAL_SERVER_ERROR: schema_submit,
        })
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

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: schema_update,
            status.HTTP_400_BAD_REQUEST: schema_update
        })
    def partial_update(self, request, pk=None):
        object_status = self.get_object().status
        if object_status == 'new':
            user = Users(**request.data.get('user'))
            if user == self.get_object().user:
                self._update(request)
                response_data = {'state': '1'}
                return Response(response_data)
            else:
                response_data = {'state': '0', 'message': 'невозможно изменить данные о пользователе'}
                return Response(response_data)
        else:
            response_data = {'state': '0', 'message': 'изменять можно толь в статусе new'}
            return Response(response_data)

# class UsersViewset(viewsets.ModelViewSet):
#     queryset = Users.objects.all()
#     serializer_class = UsersSerializer
#
#
# class CoordsViewset(viewsets.ModelViewSet):
#     queryset = Coords.objects.all()
#     serializer_class = CoordsSerializer


# class ImagesViewset(viewsets.ModelViewSet):
#     queryset = Images.objects.all()
#     serializer_class = ImagesSerializer


# Create your views here.
