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