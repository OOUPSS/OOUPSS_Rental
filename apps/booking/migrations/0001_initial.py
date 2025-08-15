import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apartments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('is_approved_by_landlord', models.BooleanField(default=False)),
                ('is_canceled', models.BooleanField(default=False)),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='apartments.apartment')),
            ],
        ),
    ]
