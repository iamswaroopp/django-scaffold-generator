

from rest_framework.routers import DefaultRouter


urlpatterns =  []

router = DefaultRouter()


from .views import BlogViewset

router.register(r'blog', BlogViewset)
urlpatterns += router.urls
