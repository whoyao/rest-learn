# Generated by Django 2.0.7 on 2018-07-24 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('user', models.CharField(max_length=100)),
                ('award', models.TextField()),
                ('address', models.TextField()),
                ('status', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('time',),
            },
        ),
    ]
