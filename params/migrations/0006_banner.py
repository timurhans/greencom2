# Generated by Django 2.1.7 on 2020-06-19 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('params', '0005_colecaob2b_ordem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordem', models.IntegerField(unique=True)),
                ('url', models.CharField(max_length=150)),
                ('img', models.ImageField(upload_to='banners/')),
            ],
        ),
    ]
