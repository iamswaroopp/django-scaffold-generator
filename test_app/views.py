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
    permission_required = [ 'test_app.add_blog',  'test_app.create_blog' ]

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






from .models import Comment


class CommentMixin:
    model = Comment

from django.contrib.auth.mixins import PermissionRequiredMixin

from django.views.generic.list import ListView

class CommentListView(CommentMixin, PermissionRequiredMixin, ListView):
    permission_required = [ 'test_app.view_comment' ]
    


from django.views.generic.detail import DetailView

class CommentDetailView(CommentMixin, PermissionRequiredMixin, DetailView):
    permission_required = [ 'test_app.view_comment' ]
    


from .forms import CommentForm
from django.urls import reverse
from django.urls import reverse_lazy

class CommentFormMixin(CommentMixin):
    form_class = CommentForm

from django.contrib.auth.mixins import PermissionRequiredMixin


from django.views.generic.edit import CreateView


class CommentCreateView(CommentFormMixin, PermissionRequiredMixin, CreateView):
    permission_required = [ 'test_app.add_comment',  'test_app.create_comment' ]

    def get_success_url(self):
        return reverse('test_app:comment-detail', kwargs={'pk':self.object.pk})


from django.contrib.auth.mixins import PermissionRequiredMixin


from django.views.generic.edit import UpdateView


class CommentUpdateView(CommentFormMixin, PermissionRequiredMixin, UpdateView):
    permission_required = [ 'test_app.change_comment' ]

    def get_success_url(self):
        return reverse('test_app:comment-detail', kwargs={'pk':self.object.pk})


from django.contrib.auth.mixins import PermissionRequiredMixin


from django.views.generic.edit import DeleteView


class CommentDeleteView(CommentFormMixin, PermissionRequiredMixin, DeleteView):
    permission_required = [ 'test_app.delete_comment' ]
    success_url = reverse_lazy('test_app:comment-list')



