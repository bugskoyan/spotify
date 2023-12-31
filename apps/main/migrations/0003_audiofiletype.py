# Generated by Django 4.2.4 on 2023-09-08 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_song_is_favorite'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioFileType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='название')),
            ],
            options={
                'verbose_name': 'тип расширения аудио-файла',
                'verbose_name_plural': 'типы расширений аудио-файлов',
            },
        ),
    ]
