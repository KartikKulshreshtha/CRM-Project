# Generated by Django 4.0 on 2022-01-08 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0006_alter_order_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]