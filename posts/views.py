from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from posts.models import Post
from .forms import PostForm, PostFormEdit, PostFormNotEdit


# Create your views here.
def post_details(request, post_id: int):
    post = Post.objects.get(pk=post_id)
    context = {}
    if post.published:
        context['post'] = post
    return render(request, 'posts/details.html', context)

def posts_list(request):
    #posts = Post.objects.all()
    posts = Post.objects.filter(published=True)
    q = request.GET.get("q")
    if q:
        posts = posts.filter(title__icontains=q)
    context = {'posts_list': posts}
    return render(request, 'posts/list.html', context)

def add_post(request):
    newpost = request.GET.get("newpost")
    published_yes = request.GET.get("published")
    published_not = request.GET.get("Npublished")

    return render(request, 'posts/add.html')

def add_post_form(request):
    if request.method == "POST" and request.user.is_authenticated:
        form = PostForm(request.POST) #PostForm z forms.py
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return HttpResponseRedirect(reverse("posts:add")) # przekierownie urzytkownika do
        # czystego formularza
    else:
        form = PostForm()
    return render(
        request,
        "posts/add.html",
        {"form": form}
        )

def edit_post(request, post_id):
    #if request.method == "POST" and request.user.is_authenticated:
    #    print("request.method == POST")
    post = get_object_or_404(Post, pk=post_id)
    print(f"druk testowy postu: {post}")
    print(f"{request.method}") # tu uzyskuję odpowieź GET
    if request.method == "POST":
        print("punkt kontrolny")
        form = PostFormEdit(request.POST, instance=post)
        if form.is_valid():
            print("if ok")
            instance = form.save()
            instance.save()
            return HttpResponseRedirect(reverse("posts:details"))
    else:
        print('else')
        form = PostFormNotEdit(instance=post)
        for field in form.fields:
            #print(form.fields[field])
            form.fields[field].disabled=True
        #for lay in form.helper.layout.fields:
        #    print(lay)
         #   form.helper.layout.fields[1].disabled=True
        #form.helper.inputs=[]

    return render(
        request,
        "posts/edit.html",
        {"form": form},
    )