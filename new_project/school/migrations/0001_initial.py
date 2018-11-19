# Generated by Django 2.1.2 on 2018-10-13 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gurdian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gurdian_id', models.IntegerField(unique=True)),
                ('gurdian_name', models.CharField(max_length=50)),
                ('gurdian_gender', models.CharField(choices=[('m', 'male'), ('f', 'female')], max_length=50)),
                ('gurdian_age', models.IntegerField()),
                ('gurdian_phone', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudenInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=50)),
                ('roll', models.IntegerField(unique=True)),
                ('std_class', models.IntegerField()),
                ('gender', models.CharField(choices=[('m', 'male'), ('f', 'female')], max_length=50)),
                ('age', models.IntegerField()),
                ('guard', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='school.Gurdian')),
            ],
        ),
    ]
