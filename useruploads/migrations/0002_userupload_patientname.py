# Generated by Django 2.2.12 on 2020-05-09 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useruploads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userupload',
            name='patientname',
            field=models.CharField(default=' ', max_length=255),
        ),
    ]
