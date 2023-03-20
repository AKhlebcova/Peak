from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    email = models.EmailField(max_length=20, unique=True, verbose_name='E-mail')
    fam = models.CharField(max_length=20, verbose_name='Фамилия')
    name = models.CharField(max_length=20, verbose_name='Имя')
    otc = models.CharField(max_length=20, verbose_name='Отчество')
    phone = models.CharField(max_length=25, verbose_name='Номер телефона')




    def __str__(self):
        return f'{self.fam} {self.name} {self.otc}'

    def __eq__(self, other):
        return self.email == other.email and self.fam == other.fam and self.name == other.name and self.otc == other.otc and self.phone == other.phone




class Coords(models.Model):
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    height = models.PositiveIntegerField(verbose_name='Высота')

    def __str__(self):
        return f'{self.latitude}, {self.longitude}: {self.height}'

    def __eq__(self, other):
        return self.height == other.height and self.longitude == other.longitude and self.latitude == other.latitude



class Add(models.Model):
    MODERATION = [
        ('new', 'новая запись'),
        ('pending', 'взято в работу'),
        ('accepted', 'успешная модерация'),
        ('rejected', 'информация отклонена'),

    ]

    user = models.ForeignKey('Users', on_delete=models.CASCADE, verbose_name='Пользователь')
    coords = models.ForeignKey('Coords', on_delete=models.CASCADE, verbose_name='Координаты')
    beauty_title = models.CharField(max_length=20, blank=True, null=True)
    title = models.CharField(max_length=60, verbose_name='Название')
    other_titles = models.CharField(max_length=60, blank=True, null=True, verbose_name='Дополнительное название')
    connect = models.CharField(max_length=60, blank=True, null=True, verbose_name='Что соединяет (долины)')
    add_time = models.DateTimeField(verbose_name='Дата регистрации')
    winter = models.CharField(max_length=2, verbose_name='Категория трудности в зимний период', blank=True,
                                    null=True)
    summer = models.CharField(max_length=2, verbose_name='Категория трудности в летний период', blank=True,
                                    null=True)
    autumn = models.CharField(max_length=2, verbose_name='Категория трудности в осенний период', blank=True,
                                    null=True)
    spring = models.CharField(max_length=2, verbose_name='Категория трудности в весенний период', blank=True,
                                    null=True)
    status = models.CharField(max_length=8, choices=MODERATION, default='new')

    def get_images(self):
        return self.images_set.all()


    @property
    def level(self):
        return {
            'summer': self.summer,
            'winter': self.winter,
            'autumn': self.autumn,
            'spring': self.spring,
        }

    @level.setter
    def level(self, dict):
        self.summer = dict['summer']
        self.winter = dict['winter']
        self.autumn = dict['autumn']
        self.spring = dict['spring']








class Images(models.Model):
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    title = models.CharField(max_length=30, verbose_name='Название участка')
    pereval = models.ForeignKey('Add', on_delete=models.CASCADE, verbose_name='Перевал', related_name='images')
    data = models.BinaryField(verbose_name='Изображение')



# Create your models here.
