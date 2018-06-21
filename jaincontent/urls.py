from django.conf.urls import url
from .views import  RegisterView, CategoryView,SubCategoryView, ItemView, LastUpdateItemView,CategoryBackupView,\
    SubCategoryBackupView,ItemBackupView, NewsView, ViharUpdateView, AalekhView, VideoView, PhotoView, FlashNewsView

urlpatterns = [

   url(r'^get_categories/', CategoryView.as_view(), name='get_categories'),
   url(r'^get_subcategories/$', SubCategoryView.as_view(), name='get_sub_categories'),
   url(r'^get_items/$', ItemView.as_view(), name='get_items'),
   url(r'^get_news/$', NewsView.as_view(), name='get_news'),
   url(r'^get_flash_news/$', FlashNewsView.as_view(), name='get_flash_news'),
   url(r'^get_vihar_updates/$', ViharUpdateView.as_view(), name='get_vihar_updates'),

   url(r'^get_aalekh/$', AalekhView.as_view(), name='get_aalekh'),
   url(r'^get_videos/$', VideoView.as_view(), name='get_videos'),
   url(r'^get_photos/$', PhotoView.as_view(), name='get_photos'),

   url(r'^get_categories_backup/', CategoryBackupView.as_view(), name='get_categories_backup'),
   url(r'^get_subcategories_backup/$', SubCategoryBackupView.as_view(), name='get_sub_categories_backup'),
   url(r'^get_items_backup/$', ItemBackupView.as_view(), name='get_items_backup'),
   url(r'^get_last_update_time/', LastUpdateItemView.as_view(), name='get_last_update_time'),

   # url(r'^register_news/', ItemView.as_view(), name='register_news'),
   # url(r'^register_alekh/', ItemView.as_view(), name='register_alekh'),
   # url(r'^update_pravas_sthal/', ItemView.as_view(), name='update_pravas_sthal'),
   url(r'^register_item/', ItemView.as_view(), name='register_item'),
   url(r'^register_subcategory/', SubCategoryView.as_view(), name='register_subcategory'),
   url(r'^category/', CategoryView.as_view(), name='category'),
   url(r'^register/', RegisterView.as_view(), name='register'),
]
