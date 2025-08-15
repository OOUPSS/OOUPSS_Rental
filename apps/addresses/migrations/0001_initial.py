import apps.addresses.models.address_models
import apps.choices.land
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('land', models.CharField(choices=apps.choices.land.Lands.choices, max_length=25)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=100)),
                ('house_number', models.CharField(max_length=10)),
                ('postal_code', models.CharField(max_length=5, validators=[apps.addresses.models.address_models.validate_postal_code])),
            ],
        ),
    ]
