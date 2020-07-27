# Generated by Django 2.2.10 on 2020-03-13 19:11

import autoslug.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("budgetportal", "0046_auto_20200309_1546"),
    ]

    operations = [
        migrations.AlterField(
            model_name="department",
            name="name",
            field=models.CharField(
                help_text="The department name must precisely match the text used in the Appropriation Bill. All datasets must be normalised to match this name. Beware that changing this name might cause a mismatch with already-published datasets which might need to be update to match this.",
                max_length=200,
            ),
        ),
        migrations.AlterField(
            model_name="department",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                always_update=True, editable=True, max_length=200, populate_from="name"
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="province",
            field=models.CharField(
                choices=[
                    ("Eastern Cape", "Eastern Cape"),
                    ("Free State", "Free State"),
                    ("Gauteng", "Gauteng"),
                    ("KwaZulu-Natal", "KwaZulu-Natal"),
                    ("Limpopo", "Limpopo"),
                    ("Mpumalanga", "Mpumalanga"),
                    ("Northern Cape", "Northern Cape"),
                    ("North West", "North West"),
                    ("Western Cape", "Western Cape"),
                ],
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="status",
            field=models.CharField(
                choices=[("upcoming", "upcoming"), ("past", "past")],
                default="upcoming",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="type",
            field=models.CharField(
                choices=[
                    ("hackathon", "hackathon"),
                    ("dataquest", "dataquest"),
                    ("cid", "cid"),
                    ("gift-dataquest", "gift-dataquest"),
                ],
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="government",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                always_update=True, editable=False, max_length=200, populate_from="name"
            ),
        ),
        migrations.AlterField(
            model_name="govtfunction",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                always_update=True,
                editable=False,
                max_length=200,
                populate_from="name",
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="programme",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                always_update=True, editable=False, max_length=200, populate_from="name"
            ),
        ),
        migrations.AlterField(
            model_name="sphere",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                always_update=True, editable=False, max_length=200, populate_from="name"
            ),
        ),
        migrations.AlterField(
            model_name="videolanguage",
            name="video",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="budgetportal.Video",
            ),
        ),
    ]
