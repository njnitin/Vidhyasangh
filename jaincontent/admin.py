from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Employee, Category, SubCategory


class EmployeeAdmin(admin.ModelAdmin):
    model = Employee
    list_display = ('employee_id', 'first_name', 'last_name', 'password', 'is_admin')
admin.site.register(Employee, EmployeeAdmin)



class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('emp_id', 'name', 'is_dashboard', 'is_side_menu', 'is_subcategory', 'type', 'logo', 'is_deleted')
admin.site.register(Category, CategoryAdmin)


class SubCategoryAdmin(admin.ModelAdmin):
    model = SubCategory
    list_display = ('emp_id', 'category_id', 'name', 'type', 'logo', 'is_deleted')

admin.site.register(SubCategory, SubCategoryAdmin)
