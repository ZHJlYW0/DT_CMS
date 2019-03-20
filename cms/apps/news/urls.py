from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from news import views
from news.views import NewsView

urlpatterns = [

    url(r'^news/categories$', views.NewsCategoryView.as_view())

]

router = DefaultRouter()
router.register(r'news', NewsView, base_name='news')
urlpatterns += router.urls


