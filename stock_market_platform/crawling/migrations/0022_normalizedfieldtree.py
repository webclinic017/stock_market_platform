# Generated by Django 3.0.5 on 2022-02-11 07:05

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('crawling', '0021_auto_20211226_1132'),
    ]

    operations = [
        migrations.CreateModel(
            name='NormalizedFieldTree',
            fields=[
                ('field_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('humanized_name', models.CharField(blank=True, max_length=256, null=True)),
                ('statement_type', models.CharField(choices=[('income_statement', 'Income Statement'), ('balance_sheet', 'Balance Sheet'), ('cash_flow', 'Cash Flow'), ('other', 'Other')], default='income_statement', max_length=256)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='crawling.NormalizedFieldTree')),
            ],
            options={
                'unique_together': {('name', 'statement_type')},
            },
        ),
    ]
