

from rest_framework.routers import DefaultRouter


urlpatterns =  []

router = DefaultRouter()


from .views import BlogViewset

router.register(r'blog', BlogViewset, basename='blog-api')



from .views import CommentViewset

router.register(r'comment', CommentViewset, basename='comment-api')


urlpatterns += router.urls
