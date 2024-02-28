# Generated by Django 5.0 on 2024-02-23 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_room_teachers_teacher_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=300)),
                ('remark', models.CharField(blank=True, max_length=500, null=True)),
                ('is_trusted', models.BooleanField(default=False)),
                ('redirects', models.JSONField(blank=True, null=True)),
                ('request_urls', models.JSONField(blank=True, null=True)),
                ('redirects_updated', models.BooleanField(default=False)),
                ('screenshot_updated', models.BooleanField(default=False)),
                ('is_blacklisted_by_tcil', models.BooleanField(blank=True, default=None, null=True)),
                ('is_blacklisted_by_operator', models.BooleanField(blank=True, default=None, null=True)),
            ],
        ),
    ]