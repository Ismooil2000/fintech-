# Generated by Django 4.1 on 2022-08-30 06:28

import apps.teachers.models.comments
import apps.teachers.models.teachers
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0002_factsmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('body', models.TextField()),
                ('author_image', models.ImageField(upload_to=apps.teachers.models.comments.upload_location)),
                ('author_name', models.CharField(max_length=55)),
                ('author_speciality', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=apps.teachers.models.teachers.upload_location)),
                ('teacher', models.CharField(max_length=255)),
                ('about', models.TextField()),
                ('experience', models.CharField(max_length=55)),
                ('social_network1', models.URLField(blank=True, max_length=255, null=True)),
                ('social_network2', models.URLField(blank=True, max_length=255, null=True)),
                ('social_network3', models.URLField(blank=True, max_length=255, null=True)),
                ('social_network4', models.URLField(blank=True, max_length=255, null=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='courses', to='courses.coursemodel')),
            ],
        ),
    ]
