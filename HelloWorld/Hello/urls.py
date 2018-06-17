from django.conf.urls import url
from Hello import views as indexviews
urlpatterns = [
    url(r'^$', indexviews.index),
]