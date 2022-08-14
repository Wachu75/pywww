from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from posts.models import Post
from .forms import PostForm, PostFormEdit, PostFormNotEdit
from .editforms import PostEditForm


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
    print(f"{request.method}")
    if request.method == "POST" and request.user.is_authenticated:
        form = PostForm(request.POST, request.FILES) #PostForm z forms.py
        print(f"druk testowy postu: {form}")
        print("punkt kontrolny")
        if form.is_valid():
            print("punkt kontrolny is_valid add_post_form")
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            print(f"print po instance.save: {instance}")
            return HttpResponseRedirect(reverse("posts:add")) # przekierownie urzytkownika do
        # czystego formularza
    else:
        print('else w add_post_form')
        form = PostForm()
        #form.helper.inputs=[] #chyba wyłącza button submit
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
        form = PostFormEdit(request.POST,request.FILES ,instance=post)
        if form.is_valid():
            print("if ok")

            instance = form.save()
            instance.save()
            return HttpResponseRedirect(reverse("posts:details"))
    else:
        print('else w edit_post()')
        #print(f"druk testowy postu w else: {post}")
        form = PostFormEdit(instance=post)
        #print(f"druk testowy form w else: {form}")
        #for field in form.fields:
            #print(form.fields[field])
        #    form.fields[field].disabled=True
        #for lay in form.helper.layout.fields:
        #    print(lay)
        #   form.helper.layout.fields[1].disabled=True
        #form.helper.layout.inputs=[]

    return render(
        request,
        "posts/edit.html",
        {"form": form}
    )

def save_post(request):
    post = get_object_or_404(Post)
    if request.method == "POST" and request.user.is_authenticated:
        #form = PostForm(request.POST)
        form = PostFormEdit(request.POST, instance=post)
        if form.is_valid():
            instance = form.save()
            instance.save()
            return HttpResponseRedirect(reverse("posts:details"))
    else:
        print('else')

    return render(
        request,
        "posts/edit.html",
        {"form": form}
    )