# Generated by Django 3.0.8 on 2020-08-05 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID1', models.CharField(max_length=50)),
                ('Header11', models.CharField(max_length=50)),
                ('Header21', models.CharField(max_length=50)),
                ('Header31', models.CharField(max_length=50)),
                ('Header41', models.CharField(max_length=50)),
            ],
        ),
    ]
