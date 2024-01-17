from django.contrib import admin
from .models import CarDriver, Account, InsurancePeriod


class CarDriverInline(admin.StackedInline):
    model = CarDriver
    extra = 1


class AccountAdmin(admin.ModelAdmin):
    inlines = [CarDriverInline]
    list_display = ('id', 'full_name', 'telegram_id', 'person_type', 'created_at')
    readonly_fields = ('created_at',)


admin.site.register(CarDriver)
admin.site.register(InsurancePeriod)
admin.site.register(Account, AccountAdmin)
