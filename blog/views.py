from django.shortcuts import render
from .forms import BlogPostForm
from .models import BlogPost

def blogcreate(request):
    form = BlogPostForm(request.POST or None)
    if form.is_valid():
        form.save()
        BlogPostForm()
    template_name= 'blog/create.html'
    context = {'form': form}
    return render (request, template_name, context)

def blog_list(request):
    queryset = BlogPost.objects.all()
    template_name = 'blog/list.html'
    context = {'object': queryset} 
    return render(request, template_name, context)

    



