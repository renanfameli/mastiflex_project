from django.contrib import admin
from .models import Category, Fields, Product, CategoryFieldValue, ProductFieldValue, FieldOption


class FieldOptionInline(admin.TabularInline):
    model = FieldOption
    extra = 1


class FieldsAdmin(admin.ModelAdmin):
    inlines = [FieldOptionInline]


class ProductFieldValueInline(admin.TabularInline):
    model = ProductFieldValue
    extra = 1

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "field":
            obj_id = request.resolver_match.kwargs.get("object_id")
            if obj_id:
                product = Product.objects.get(id=obj_id)
                category_fields = CategoryFieldValue.objects.filter(category=product.category)
                kwargs["queryset"] = Fields.objects.filter(id__in=[cf.field.id for cf in category_fields])
            else:
                kwargs["queryset"] = Fields.objects.none()
        elif db_field.name == "option":
            obj_id = request.resolver_match.kwargs.get("object_id")
            if obj_id:
                product = Product.objects.get(id=obj_id)
                category_fields = CategoryFieldValue.objects.filter(category=product.category)
                fields = Fields.objects.filter(id__in=[cf.field.id for cf in category_fields])
                kwargs["queryset"] = FieldOption.objects.filter(field__in=fields)
            else:
                kwargs["queryset"] = FieldOption.objects.none()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class CategoryFieldValueInline(admin.TabularInline):
    model = CategoryFieldValue
    extra = 1

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "field":
            kwargs["queryset"] = Fields.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class CategoryAdmin(admin.ModelAdmin):
    inlines = [CategoryFieldValueInline]


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductFieldValueInline]


admin.site.register(Fields, FieldsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
