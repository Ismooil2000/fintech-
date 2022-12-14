# Generated by Django 4.1 on 2022-10-17 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachermodel',
            name='rating',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teachermodel',
            name='teacher_level',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
