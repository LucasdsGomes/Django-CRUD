# Generated by Django 4.2 on 2023-07-10 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_log_alter_funcionario_func'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Log',
        ),
        migrations.AddField(
            model_name='funcionario',
            name='password',
            field=models.CharField(max_length=50, null=True),
        ),
    ]