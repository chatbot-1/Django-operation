# Generated by Django 4.2.3 on 2023-08-15 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_alter_regular_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regular_blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('cover', models.ImageField(upload_to='new_blog')),
            ],
        ),
        migrations.DeleteModel(
            name='Regular',
        ),
    ]