# Generated by Django 3.0.7 on 2020-06-12 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Language'),
        ),
        migrations.AddField(
            model_name='language',
            name='language',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]
