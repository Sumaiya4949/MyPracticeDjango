# Generated by Django 2.1.2 on 2018-10-25 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dis_name', models.CharField(max_length=50)),
                ('dis_population', models.IntegerField()),
                ('dis_area', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('div_name', models.CharField(max_length=50)),
                ('div_population', models.IntegerField()),
                ('div_area', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='div',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Division'),
        ),
    ]
