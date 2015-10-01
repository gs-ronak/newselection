
from django.conf.urls import include, url
from django.views.generic import TemplateView

urlpatterns = [
	
url(r'^index$', TemplateView.as_view(template_name='news/index.html'), name="home"),

]


