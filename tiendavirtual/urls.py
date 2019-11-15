from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^productos/$', views.ProductListView.as_view(), name='productos'),
	url(r'^producto/(?P<pk>\d+)$', views.ProductDetailView.as_view(), name='product-detail'),
]

"""views.product_detail_view, name='product-detail'),"""
