from django.urls import path, include
from . import views

app_name = 'test_app'

urlpatterns =  []

urlpatterns += [ path('api/', include('test_app.api.urls'), name='test_app-api') ]



from django.urls import path


from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
urlpatterns += [
    path('blog/', BlogListView.as_view(), name='blog-list'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('blog/create/', BlogCreateView.as_view(), name='blog-create'),
    path('blog/<int:pk>/update/', BlogUpdateView.as_view(), name='blog-update'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog-delete'),
]

from django.urls import path


from .views import CommentListView, CommentDetailView, CommentCreateView, CommentUpdateView, CommentDeleteView
urlpatterns += [
    path('comment/', CommentListView.as_view(), name='comment-list'),
    path('comment/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('comment/create/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]