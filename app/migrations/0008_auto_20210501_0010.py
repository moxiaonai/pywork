# Generated by Django 3.1.7 on 2021-04-30 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210430_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='psy_type',
            field=models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='psy_type', to='app.category'),
        ),
    ]
