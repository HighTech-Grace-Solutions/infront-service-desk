# Generated by Django 3.0.10 on 2020-10-06 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0002_technician_last_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='company_link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.Company'),
        ),
    ]