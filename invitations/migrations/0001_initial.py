# Generated by Django 3.0.2 on 2021-04-08 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('message', models.TextField()),
                ('m_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]