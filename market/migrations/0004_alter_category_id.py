# Generated by Django 5.0.4 on 2024-04-14 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_author_category_remove_book_category_book_cover_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]