from django.db import models

REGION_CHOICES = (
    (0, 'Tashkent'),
    (1, 'Other')
)

PERSON_TYPE = (
    (0, 'PHYSICAL_PERSON'),
    (1, 'LEGAL_ENTITY')
)

CITIZENSHIP = (
    (0, 'Uzbek'),
    (1, 'Other')
)

CAR_TYPES = (
    (0, 'LIGHT_CAR'),
    (1, 'TRUCK'),
    (2, 'BUS_AND_MICROBUS'),
    (3, 'OTHER'),
)


class InsurancePeriod(models.Model):
    period = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.period}"


class Account(models.Model):
    telegram_id = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=100, unique=True, null=True, blank=True)
    citizenship = models.IntegerField(choices=CITIZENSHIP, default=0)
    full_name = models.CharField(max_length=225)
    phone_number = models.CharField(max_length=15, unique=True)
    person_type = models.IntegerField(choices=PERSON_TYPE, default=0)
    car_type = models.IntegerField(choices=CAR_TYPES, default=0)
    region = models.IntegerField(choices=REGION_CHOICES, default=0)
    insurance_period = models.ForeignKey(InsurancePeriod, on_delete=models.SET_NULL, null=True, blank=True)
    is_privilege = models.BooleanField(default=False, verbose_name='Imtiyoz')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.full_name}"


class CarDriver(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='car_drivers', to_field='telegram_id', )
    technical_passport = models.ImageField(upload_to='tex_passports', verbose_name="Tex Passport (Front)")
    passport = models.ImageField(upload_to='passports', verbose_name="Driver Passport")
    is_owner = models.BooleanField(default=False, verbose_name="Owner")

    def __str__(self):
        return f"{self.user}"
