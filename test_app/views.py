from django.shortcuts import render

# Create your views here.



from .models import Blog


class BlogMixin:
    model = Blog

from django.contrib.auth.mixins import PermissionRequiredMixin

from django.views.generic.list import ListView

class BlogListView(BlogMixin, PermissionRequiredMixin, ListView):
    permission_required = [ 'test_app.view_blog' ]
    


from django.views.generic.detail import DetailView

class BlogDetailView(BlogMixin, PermissionRequiredMixin, DetailView):
    permission_required = [ 'test_app.view_blog' ]
    


from .forms import BlogForm
from django.urls import reverse
from django.urls import reverse_lazy

class BlogFormMixin(BlogMixin):
    form_class = BlogForm

from django.contrib.auth.mixins import PermissionRequiredMixin


from django.views.generic.edit import CreateView


class BlogCreateView(BlogFormMixin, PermissionRequiredMixin, CreateView):
    permission_required = [ 'test_app.add_blog' ]

    def get_success_url(self):
        return reverse('test_app:blog-detail', kwargs={'pk':self.object.pk})


from django.contrib.auth.mixins import PermissionRequiredMixin


from django.views.generic.edit import UpdateView


class BlogUpdateView(BlogFormMixin, PermissionRequiredMixin, UpdateView):
    permission_required = [ 'test_app.change_blog' ]

    def get_success_url(self):
        return reverse('test_app:blog-detail', kwargs={'pk':self.object.pk})


from django.contrib.auth.mixins import PermissionRequiredMixin


from django.views.generic.edit import DeleteView


class BlogDeleteView(BlogFormMixin, PermissionRequiredMixin, DeleteView):
    permission_required = [ 'test_app.delete_blog' ]
    success_url = reverse_lazy('test_app:blog-list')



