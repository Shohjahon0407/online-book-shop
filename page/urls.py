from django.urls import path

from accaunts.utils import send_sample_mail
from page.views import get_info, add_book, detail_book, delete

urlpatterns = [
    path('', get_info, name='objects'),
    path('add-book/', add_book, name='add_book'),
    path('detail/<int:pk>/', detail_book, name='detail'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('send-mail/',  send_sample_mail, name='email'),
]