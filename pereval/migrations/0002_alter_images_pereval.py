# Generated by Django 4.1.7 on 2023-03-19 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='pereval',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='pereval.add', verbose_name='Перевал'),
        ),
    ]