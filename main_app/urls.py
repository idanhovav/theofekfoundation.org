from django.conf.urls import url, include
from main_app import views
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^$', views.index, name='Homepage'),
	url(r'^robots\.txt$', views.robots, name='Robots'),
	url(r'^.well-known/acme-challenge/BecZpEB_hNeWmJUz1TGoLuuRbx32ZW4eN2VBZ62O0w0',
		views.acme),
	url(r'^sitemap\.xml$', TemplateView.as_view(template_name='main_app/sitemap.xml', content_type='text/xml')),
	url(r'^', include('main_app.misurls')),
]