# Generated by Django 3.2 on 2021-05-13 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_delete_reviews'),
        ('reviews', '0005_auto_20210513_1846'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Review',
            new_name='Reviews',
        ),
    ]