# Generated by Django 3.2 on 2021-05-01 08:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pizzas', '0005_remove_pizza_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='own',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
