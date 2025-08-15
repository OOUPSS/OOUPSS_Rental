import apps.choices.type_apartment
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('rooms', models.SmallIntegerField()),
                ('apartment_type', models.CharField(choices=apps.choices.type_apartment.ApartmentTypes.choices, default=apps.choices.type_apartment.ApartmentTypes['APARTMENT'], max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='apartments', to='addresses.address')),
            ],
        ),
    ]
