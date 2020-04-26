# Generated by Django 2.2.10 on 2020-04-26 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200426_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('path', models.CharField(max_length=250)),
                ('method', models.CharField(max_length=50)),
                ('r_time', models.CharField(max_length=50)),
                ('user_id', models.IntegerField()),
            ],
        ),
    ]