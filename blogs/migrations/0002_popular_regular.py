# Generated by Django 4.2.3 on 2023-08-03 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Popular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ranking', models.IntegerField()),
                ('topic', models.CharField(max_length=50)),
                ('heading', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('postDate', models.DateField(auto_now_add=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Regular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50)),
                ('heading', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('postDate', models.DateField(auto_now_add=True)),
                ('content', models.TextField()),
            ],
        ),
    ]
