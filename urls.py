from diango.conf.urls.defoults import *

from django.contrib import admin
admin.autodiscover()

urlpattern = patterns('',
		      (r'^admin/(.*)', admin.site.root),
		      )