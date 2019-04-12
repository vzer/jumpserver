# Generated by Django 2.1.7 on 2019-04-08 03:36

from django.db import migrations, models
import uuid


def add_default_actions(apps, schema_editor):
    from ..models import Action
    group_model = apps.get_model("perms", "Action")
    db_alias = schema_editor.connection.alias
    for action, _ in Action.NAME_CHOICES:
        group_model.objects.using(db_alias).create(name=action)


class Migration(migrations.Migration):

    dependencies = [
        ('perms', '0002_auto_20171228_0025_squashed_0009_auto_20180903_1132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(choices=[('all', 'All'), ('connect', 'Connect'), ('upload_file', 'Upload file'), ('download_file', 'Download file')], max_length=128, unique=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Action',
            },
        ),
        migrations.AddField(
            model_name='assetpermission',
            name='actions',
            field=models.ManyToManyField(blank=True, related_name='permissions', to='perms.Action', verbose_name='Action'),
        ),
        migrations.RunPython(add_default_actions),
    ]