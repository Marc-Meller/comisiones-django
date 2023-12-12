from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import blogPost
from .forms import blogPostModelForm
# Create your views here.


# CRUD # CREATE READ UPDATE DELETE
def blog_post_list_view (request):
    qs = blogPost.objects.all().published()
    if request.user.is_authenticated:
        my_qs = blogPost.objects.filter(user=request.user)
        qs = (qs | my_qs).distinct()  
    template_name = 'blog/list.html'
    context = {"object_list": qs}
    return render(request, template_name, context)


@staff_member_required
def blog_post_create_view (request):
    form = blogPostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = blogPostModelForm()
    template_name = 'form.html'
    context = {"form": form}
    return render(request, template_name, context)

def blog_post_detail_view (request, slug):
    obj = get_object_or_404(blogPost, slug=slug)
    template_name = 'blog/details.html'
    context = {"object": obj}
    return render(request, template_name, context)

@staff_member_required
def blog_post_update_view(request, slug):
    obj = get_object_or_404(blogPost, slug=slug)
    
    if request.method == 'POST':
        form = blogPostModelForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            existing_publish_date = obj.publish_date
            new_date = form.cleaned_data['publish_date']
            obj.publish_date = timezone.datetime.combine(new_date, existing_publish_date.time())
            obj.save()
    else:
        form = blogPostModelForm(instance=obj)  # Carga el formulario con los datos existentes
    
    template_name = 'form.html'
    context = {'title': f"Update {obj.title}", "form": form}
    return render(request, template_name, context)


@staff_member_required
def blog_post_delete_view (request,slug):
    obj = get_object_or_404(blogPost, slug=slug)
    template_name = 'blog/delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect("/blog")
    context = {"object": obj}
    return render(request, template_name, context)