from django.conf.urls import url
from django.contrib import admin
from projekt.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/$',register_page),
    url(r'^login/$',login_page),
    url(r'^$', main_page),
    url(r'^logout', logout_page),
    url(r'^card_create/$', card_create),

]
