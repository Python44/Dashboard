# Generated by Django 3.0.8 on 2020-08-05 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APPL1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maintable',
            old_name='Header11',
            new_name='Alias',
        ),
        migrations.RenameField(
            model_name='maintable',
            old_name='Header21',
            new_name='Alias2',
        ),
        migrations.RenameField(
            model_name='maintable',
            old_name='Header31',
            new_name='Status',
        ),
        migrations.RemoveField(
            model_name='maintable',
            name='Header41',
        ),
        migrations.RemoveField(
            model_name='maintable',
            name='ID1',
        ),
        migrations.AddField(
            model_name='maintable',
            name='Name',
            field=models.CharField(choices=[('Boom 1', ''), ('Boom 2', ''), ('Boom 3', ''), ('Boom 4', ''), ('Boom 5', '')], default='------', max_length=6),
        ),
        migrations.AddField(
            model_name='maintable',
            name='Planned_Program',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='maintable',
            name='Program',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='maintable',
            name='R_Data',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='maintable',
            name='R_Data2',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='maintable',
            name='R_Time',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='maintable',
            name='R_Time2',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='maintable',
            name='Sheduled_Program2',
            field=models.IntegerField(default='0'),
        ),
    ]
