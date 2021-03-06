# Generated by Django 2.0.3 on 2018-04-01 14:35

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_auto_20170629_1342'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['-id'], 'verbose_name': '标签', 'verbose_name_plural': '标签'},
        ),
        migrations.AddField(
            model_name='post',
            name='cover',
            field=imagekit.models.fields.ProcessedImageField(default='', upload_to='cover', verbose_name='封面'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
