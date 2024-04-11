# Generated by Django 5.0.4 on 2024-04-11 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['best_seller', 'title'], 'verbose_name': 'Book', 'verbose_name_plural': 'Books'},
        ),
        migrations.AlterField(
            model_name='book',
            name='age_group',
            field=models.CharField(max_length=50, verbose_name='Age Group'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=100, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='best_seller',
            field=models.BooleanField(default=False, verbose_name='Best Seller'),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(max_length=50, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='covers/', verbose_name='Cover'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='book',
            name='stock',
            field=models.IntegerField(verbose_name='Stock'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
    ]
