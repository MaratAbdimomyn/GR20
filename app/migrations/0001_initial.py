# Generated by Django 4.2.4 on 2023-08-29 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Champions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('champions_name', models.CharField(max_length=40)),
                ('champions_team', models.CharField(max_length=40)),
                ('champions_year', models.DateField()),
            ],
        ),
    ]