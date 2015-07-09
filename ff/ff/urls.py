# -*- coding: utf-8 -*-
from django.conf.urls import include, url, patterns


from django.contrib import admin
from item.views import *

# from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rules/$', rules),
    url(r'^forgotpass/$', forgotpass),
    url(r'^nocode/$', nocode),
    url(r'^about/$', about),
    url(r'^signup/$', signup),
    url(r'^price/$', price),
    url(r'^thanks/$', thanks),
    url(r'^nogoods/$', nogoods),
    url(r'^cash/$', cash),
    url(r'^order_save/$', order_save),
    url(r'^review/$', review),
    url(r'^invite/$', invite),
    url(r'^faq/$', faq),
    url(r'^order/$', order),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', index),
    ]

# if settings.DEBUG:
# 	urlpatterns += static(settings.STATIC_URL,
# 		document_root=settings.STATIC_ROOT)
# 	urlpatterns += static(settings.MEDIA_URL,
# 		document_root=settings.MEDIA_ROOT)

# Что делать
# 1. Cтраница входа+
# 2. Страница "Вступить в клуб"+
# 3. Страница "Нет клубного кода"+
# 4. Страница "Правила"+
# 5. Страница "О клубе"
# 5-1. Страница "Забыли пароль"+

# 5. Cтраница "Цены"
# 6. Страница "Заказ"
# 7. Страница "Спасибо за заказ"
# 8. Страница "Нет того, что нужно?"

# 9. Cтраница "Накопления" и "Cashback"
# 10. Страница "Оставьте отзыв о клубе"
# 11. Страница "Приглашений"
# 12. Страница "FAQ"


# 13. Email "Приглашение"
# 14. Email "Cashback"