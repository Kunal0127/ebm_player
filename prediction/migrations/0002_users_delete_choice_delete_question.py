# Generated by Django 4.0.3 on 2022-04-10 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=250)),
                ('firstName', models.CharField(blank=True, max_length=200)),
                ('password', models.CharField(blank=True, max_length=200)),
                ('Confirm_password', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
