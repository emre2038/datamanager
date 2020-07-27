# Generated by Django 2.2.10 on 2020-03-18 19:43

import wagtail.core.blocks
import wagtail.core.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("budgetportal", "0053_auto_20200318_1938"),
    ]

    operations = [
        migrations.AlterField(
            model_name="guidepage",
            name="body",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "section",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "presentation_class",
                                    wagtail.core.blocks.ChoiceBlock(
                                        choices=[
                                            ("is-default", "Default"),
                                            ("is-invisible", "No background/border"),
                                            ("is-bevel", "Bevel"),
                                        ]
                                    ),
                                ),
                                ("content", wagtail.core.blocks.RichTextBlock()),
                            ]
                        ),
                    ),
                    ("html", wagtail.core.blocks.RawHTMLBlock()),
                    (
                        "chart_embed",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("description", wagtail.core.blocks.RichTextBlock()),
                                ("embed_code", wagtail.core.blocks.RawHTMLBlock()),
                            ]
                        ),
                    ),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="postpage",
            name="body",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "section",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "presentation_class",
                                    wagtail.core.blocks.ChoiceBlock(
                                        choices=[
                                            ("is-default", "Default"),
                                            ("is-invisible", "No background/border"),
                                            ("is-bevel", "Bevel"),
                                        ]
                                    ),
                                ),
                                ("content", wagtail.core.blocks.RichTextBlock()),
                            ]
                        ),
                    ),
                    ("html", wagtail.core.blocks.RawHTMLBlock()),
                ]
            ),
        ),
    ]
