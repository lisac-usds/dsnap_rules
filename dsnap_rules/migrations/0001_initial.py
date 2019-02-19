from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('disaster_request_no', models.CharField(max_length=20,
                                                         unique=True)),
                ('title', models.CharField(max_length=50)),
                ('benefit_begin_date', models.DateField()),
                ('benefit_end_date', models.DateField()),
                ('state_or_territory', models.CharField(max_length=2)),
                ('is_residency_required', models.BooleanField()),
                ('uses_DSED', models.BooleanField()),
            ],
            options={
                'db_table': 'disaster',
            },
        ),
    ]
