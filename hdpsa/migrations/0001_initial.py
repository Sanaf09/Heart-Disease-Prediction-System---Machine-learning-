# Generated by Django 2.2.12 on 2020-04-24 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('did', models.AutoField(primary_key=True, serialize=False)),
                ('dname', models.CharField(max_length=255)),
                ('demail', models.EmailField(max_length=254)),
                ('dcontact', models.CharField(max_length=10)),
                ('dspeciality', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('bid', models.AutoField(primary_key=True, serialize=False)),
                ('btitle', models.CharField(max_length=255)),
                ('bauthor', models.CharField(max_length=255)),
                ('bdate', models.DateField()),
                ('bdescription', models.TextField()),
                ('categories', models.ManyToManyField(blank=True, to='hdpsa.Category')),
            ],
        ),
    ]
