
from django.urls import path
from . import views
from logsin.settings import DEBUG,STATIC_URL,STATIC_ROOT,MEDIA_ROOT,MEDIA_URL
from django.conf.urls.static import static


urlpatterns = [
    path('home',views.home,name='home'),
    path('uploadform',views.uploadform,name="uploadform"),
    path('update/<int:book_id>',views.update_book,name='update'),
    path('delete/<int:book_id>',views.delete_book,name='delete'),
]

if DEBUG:
    urlpatterns += static(STATIC_URL,document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL,document_root=MEDIA_ROOT)
