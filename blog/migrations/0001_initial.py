# Generated by Django 4.2.5 on 2023-09-07 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='blogs/', verbose_name='Изображение')),
                ('count_views', models.IntegerField(default=0, verbose_name='Количество просмотров')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'ordering': ('heading',),
            },
        ),
    ]
