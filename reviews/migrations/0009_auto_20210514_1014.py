# Generated by Django 3.2 on 2021-05-14 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('products', '0011_delete_reviews'),
        ('reviews', '0008_alter_reviews_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reviews',
            new_name='Review',
        ),
        migrations.AlterModelOptions(
            name='review',
            options={},
        ),
    ]
