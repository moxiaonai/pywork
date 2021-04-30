# Generated by Django 3.1.7 on 2021-04-27 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210329_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=90, verbose_name='Title')),
                ('content', models.TextField(blank=True, verbose_name='Content')),
                ('psy_type', models.CharField(db_index=True, max_length=11, verbose_name='Psy Type')),
                ('user_id', models.CharField(db_index=True, max_length=11, verbose_name='User Id')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
            ],
            options={
                'ordering': ['create_date'],
            },
        ),
    ]
