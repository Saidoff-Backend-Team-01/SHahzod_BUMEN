from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
)

urlpatterns += {
    path('subject/', include('subject.urls')),
}

# if 'rosetta' in settings.INSTALLED_APPS:
#     urlpatterns = [
#         re_path('rosetta/', include('rosetta.urls')),
#     ]
