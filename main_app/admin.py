from django.contrib import admin
from main_app.models import Product, Order, UserProfile

admin.site.site_header = "Shobakin Admin"


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ("name", "category", "quantity")
    list_filter = ["category"]
    search_fields = ["name"]


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ("product", "created_by", "order_quantity", "date")
    list_filter = ["date"]
    search_fields = ["product"]


class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = ("user", "physical_address", "mobile")
    list_filter = ["user"]
    search_fields = ["user"]


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(UserProfile, UserProfileAdmin)



# Register your models here.
