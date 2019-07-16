# Generated by Django 2.2.2 on 2019-06-24 12:38

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FormSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('Delhi', 'Delhi'), ('Tricity', 'Tricity')], max_length=100)),
                ('city', models.CharField(choices=[('Delhi', 'Delhi'), ('Tricity', 'Tricity')], max_length=100)),
                ('sales', models.CharField(default='0', max_length=100)),
                ('mind_o', models.CharField(max_length=100)),
                ('body_o', models.CharField(max_length=100)),
                ('skin_o', models.CharField(max_length=100)),
                ('multipack_o', models.CharField(max_length=100)),
                ('mind_c', models.CharField(max_length=100)),
                ('body_c', models.CharField(max_length=100)),
                ('skin_c', models.CharField(max_length=100)),
                ('multipack_c', models.CharField(max_length=100)),
                ('jumbo_combos', models.CharField(max_length=100)),
                ('created_on', models.DateField(default=datetime.date.today, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('typeOfUser', models.CharField(choices=[('intern', 'intern'), ('admin', 'admin')], default='intern', max_length=10)),
                ('auth_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ImageSubmisson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='submission_images/')),
                ('form_submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.FormSubmission')),
            ],
        ),
        migrations.AddField(
            model_name='formsubmission',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User'),
        ),
    ]
