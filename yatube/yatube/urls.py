from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("posts.urls")),
    # импорт правил из приложения admin
    path("admin/", admin.site.urls),
]