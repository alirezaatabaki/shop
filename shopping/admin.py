from django.contrib import admin

from .models import Product, Category


# admin.site.register(Category)
# admin.site.register(Product)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available')
    list_filter = ('available', 'created')
    list_editable = ('price',)
    prepopulated_fields = {'slug': ('name',)}
    # raw_id_fields = ('category',)
    actions = ('make_available',)

    def make_available(self, request, queryset):
        num_updated = queryset.update(available=True)
        self.message_user(request, f' از کالاها آپدیت به‌روزرسانی شدند{num_updated} تعداد ')

    make_available.short_description = 'موجود کردن کالا'
