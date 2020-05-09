# Generated by Django 3.0.6 on 2020-05-08 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pubdate', models.DateField()),
                ('body', models.CharField(max_length=600)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
