from rest_framework import serializers
from .models import Category, Employee, SubCategory

from django.contrib.auth.hashers import make_password




class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields = ['employee_id', 'first_name', 'last_name', 'password']

    def create(self, validated_data):
        emp = Employee.objects.create_user(**validated_data)
        return emp


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields = ['emp_id', 'name', 'is_dashboard', 'is_side_menu','is_subcategory', 'type', 'logo']

    def create(self, validated_data):
        category = Category.objects.create(**validated_data)
        return category


class GetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields = ['id', 'name', 'is_dashboard', 'is_side_menu','is_subcategory', 'type', 'logo']

    


class GetSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=SubCategory
        fields = ['id', 'category_id', 'name', 'type', 'logo']


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=SubCategory
        fields = ['emp_id','category_id', 'name', 'type', 'logo']
 
    def create(self, validated_data):
        subcategory = SubCategory.objects.create(**validated_data)
        return subcategory

