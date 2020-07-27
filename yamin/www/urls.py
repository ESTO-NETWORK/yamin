from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView
from www import views
from www.views import IndexView

app_name = 'www'
urlpatterns = [
    path('', IndexView.as_view(), name='www'),
    path('get_split_korean', IndexView.as_view()),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
