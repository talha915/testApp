# Generated by Django 2.1.2 on 2018-10-29 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_student_std_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_name', models.CharField(max_length=30)),
                ('std_address', models.CharField(max_length=250)),
                ('std_age', models.IntegerField()),
            ],
        ),
    ]
