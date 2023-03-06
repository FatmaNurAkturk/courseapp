# Generated by Django 4.1.3 on 2023-02-17 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0006_alter_course_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name="course",
            name="category",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="kurslar",
                to="courses.category",
            ),
        ),
        migrations.AlterField(
            model_name="course",
            name="slug",
            field=models.SlugField(blank=True, default="", unique=True),
        ),
    ]