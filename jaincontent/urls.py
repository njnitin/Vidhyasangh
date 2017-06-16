from django.conf.urls import url
from .views import  RegisterView, CategoryView,SubCategoryView

urlpatterns = [

   url(r'^get_categories/', CategoryView.as_view(), name='get_categories'),
   url(r'^get_subcategories/$', SubCategoryView.as_view(), name='get_sub_categories'),
   url(r'^register_subcategory/', SubCategoryView.as_view(), name='register_subcategory'),
   url(r'^category/', CategoryView.as_view(), name='category'),
    url(r'^register/', RegisterView.as_view(), name='register'),
]
