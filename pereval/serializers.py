import base64

from .models import *
from rest_framework import serializers


class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = [
            'email',
            'fam',
            'name',
            'otc',
            'phone',
        ]
        extra_kwargs = {
            'email': {
                'validators': []
            }
        }


class CoordsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coords
        fields = [
            'latitude',
            'longitude',
            'height',
        ]


class LevelSerialaizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Add
        fields = [
            'winter',
            'summer',
            'autumn',
            'spring',
        ]


class MyBinaryField(serializers.Field):
    def to_internal_value(self, obj):
        return base64.b64decode(obj)

    def to_representation(self, value):
        return base64.b64encode(value)


class ImagesSerializer(serializers.HyperlinkedModelSerializer):
    data = MyBinaryField()

    class Meta:
        model = Images
        fields = [
            'data',
            'title',
        ]


class AddSerializer(serializers.HyperlinkedModelSerializer):
    user = UsersSerializer()
    coords = CoordsSerializer()
    level = LevelSerialaizer(many=False)
    images = ImagesSerializer(many=True)
    status = serializers.CharField(read_only=True)




    def create(self, validated_data):
        user_data = validated_data.pop('user')
        coord_data = validated_data.pop('coords')
        image_data = validated_data.pop('images')

        coords = Coords.objects.create(**coord_data)
        email = user_data.get('email')
        try:
            user = Users.objects.get(email=email)
        except:
            user = Users.objects.create(**user_data)
        add = Add.objects.create(user=user, coords=coords, **validated_data)
        for img in image_data:
            Images.objects.create(pereval=add, **img)
        return add

    class Meta:
        model = Add
        depth = 1
        fields = [
            'beauty_title',
            'title',
            'other_titles',
            'connect',
            'add_time',
            'user',
            'coords',
            'level',
            'images',
            'status',
        ]
