from django.conf.urls import url

from .views import index
from .views import ProductsView
urlpatterns = [
    url(r'^$',  index, name="dashboard"),
    url(r'^product/', ProductsView.as_view(), name="productpage")
]
