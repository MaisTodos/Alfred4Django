from django.contrib import admin
from receipts.models import Item, Receipt


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    pass


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass
