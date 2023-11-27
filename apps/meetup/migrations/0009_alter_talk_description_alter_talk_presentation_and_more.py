# Generated by Django 4.2 on 2023-04-11 11:00

from django.db import migrations, models
import picklefield.fields


class Migration(migrations.Migration):
    dependencies = [('meetup', '0008_alter_event_manual_on_air_alter_event_status_and_more')]

    operations = [
        migrations.AlterField(
            model_name='talk',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='presentation',
            field=models.URLField(blank=True, null=True, verbose_name='Адрес презентации'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='presentation_data',
            field=picklefield.fields.PickledObjectField(
                blank=True, editable=False, null=True, verbose_name='Meta-данные презентации'
            ),
        ),
        migrations.AlterField(
            model_name='talk', name='video', field=models.URLField(blank=True, null=True, verbose_name='Адрес видео')
        ),
        migrations.AlterField(
            model_name='talk',
            name='video_data',
            field=picklefield.fields.PickledObjectField(
                blank=True, editable=False, null=True, verbose_name='Meta-данные видео'
            ),
        ),
    ]