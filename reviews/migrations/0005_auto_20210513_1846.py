# Generated by Django 3.2 on 2021-05-13 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_delete_reviews'),
        ('reviews', '0004_rename_review_body_review_review_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='reviews',
        ),
        migrations.AddField(
            model_name='review',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product'),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_content',
            field=models.TextField(blank='', null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.CharField(default='User not found', max_length=254),
        ),
    ]
