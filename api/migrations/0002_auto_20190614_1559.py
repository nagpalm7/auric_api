# Generated by Django 2.2.2 on 2019-06-14 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['name']},
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='typeOfUser',
            field=models.CharField(choices=[('intern', 'intern'), ('admin', 'admin')], default='intern', max_length=10),
        ),
    ]
