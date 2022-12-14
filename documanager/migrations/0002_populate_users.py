# Generated by Django 4.1.2 on 2022-10-05 23:37

from django.db import migrations
from documanager.models import User

def populate_users(apps, schema_editor):

    data = [
        {"name": "Gemma", "password": "Propylon2022"},
        {"name": "Brendan", "password": "Propylon2022"},
        {"name": "Saul", "password": "Propylon2022"}
    ]

    for item in data:
        user = User()
        user.name = item["name"]
        user.password = item["password"]
        user.save()

class Migration(migrations.Migration):

    dependencies = [
        ('documanager', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_users,  migrations.RunPython.noop)
    ]


