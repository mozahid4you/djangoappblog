from . models import BlogModel
from  django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .forms import PostForm,UpdateForm

class HomeList(ListView):
    paginate_by = 4
    template_name = 'home.html'
    model = BlogModel
    ordering = ['-dt']


class Blogdetail(DetailView):
    model = BlogModel
    template_name='blogdetail.html'

class Addpost(CreateView):
    model = BlogModel
    template_name = 'add.html'
    form_class = PostForm
    success_url = reverse_lazy('home')

class Updatepost(UpdateView):
    model = BlogModel
    template_name = 'updateblog.html'
    form_class = UpdateForm
    success_url = reverse_lazy('home')

class Deletepost(DeleteView):
    model = BlogModel
    template_name = 'delete.html'
    success_url = reverse_lazy('home')







