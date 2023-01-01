from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from posts.models import Post
from .forms import PostForm, PostFormEdit, PostFormNotEdit
from .editforms import PostEditForm
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test



@login_required(login_url='login')
def post_details(request, post_id: int):
    post = Post.objects.get(pk=post_id)
    context = {}
    if post.published:
        context['post'] = post
    return render(request, 'posts/details.html', context)

@login_required(login_url='login')
def posts_list(request):
    #posts = Post.objects.all()
    posts = Post.objects.filter(published=True)
    q = request.GET.get("q")
    if q:
        posts = posts.filter(title__icontains=q)
    context = {'posts_list': posts}
    return render(request, 'posts/list.html', context)

'''def staff_required(login_url=None):
    return user_passes_test(lambda u: u.is_staff, login_url=login_url)

@staff_required(login_url="../admin")
def series_info(request)

def user_can_vote(user):
    return user.is_authenticated() and user.has_perm("polls.can_vote")

@user_passes_test(user_can_vote, login_url="/login/")

@login_required(login_url="/login")
@permission_required("main.add_post", login_url="/login", raise_exception=True)
'''

@login_required(login_url='login')
#@permission_required("posts.Can_add_post", raise_exception=True)
@permission_required("posts.add_post", login_url='login', raise_exception=True)
def add_post(request):
    newpost = request.GET.get("newpost")
    published_yes = request.GET.get("published")
    published_not = request.GET.get("Npublished")

    return render(request, 'posts/add.html')

@login_required(login_url='login')
#@permission_required("posts.Can_add_post", raise_exception=True)
@permission_required("posts.add_post", login_url='login', raise_exception=True)
def add_post_form(request):
    print(f"{request.method}")
    if request.method == "POST" and request.user.is_authenticated:
        form = PostForm(request.POST, request.FILES) #PostForm z forms.py
        #print(f"druk testowy postu: {form}")
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


@permission_required("posts.can_change_post", login_url='login')
def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    #order = Order.objects.get(id=pk)
    #form = OrderForm(instance=order)
    if request.method == "POST":
        form = PostFormEdit(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            #return redirect("posts:details", post_id)
            return HttpResponseRedirect(reverse("posts:details", args=(post_id,))) 
    else:
        form = PostFormEdit(instance=post)
    return render(request, 'posts/add.html', {'form': form})
# def edit_post(request, post_id: int):
#     #if request.method == "POST" and request.user.is_authenticated:
#     print("request.method == POST")
#     post = get_object_or_404(Post, pk=post_id)
#     #context = {}
#     print(f"druk testowy postu: {post}")
#     print(f"{request.method}") # tu uzyskuję odpowieź GET
#     if request.method == "POST":
#         print("punkt kontrolny")
#         form = PostForm(request.POST,instance=post)
#         if form.is_valid():
#             print("if ok")
#
#             #instance = form.save()
#             #instance.save()
#             form.save()
#             #return HttpResponseRedirect(reverse("posts:details"))
#     else:
#         print('else w edit_post()')
#         #print(f"druk testowy postu w else: {post}")
#         form = PostFormEdit(instance=post)
#         #print(f"druk testowy form w else: {form}")
#         #for field in form.fields:
#             #print(form.fields[field])
#         #    form.fields[field].disabled=True
#         #for lay in form.helper.layout.fields:
#         #    print(lay)
#         #   form.helper.layout.fields[1].disabled=True
#         #form.helper.layout.inputs=[]
#
#     return render(
#         request,
#         "posts/add.html",
#         {"form": form}
#     )

'''def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES, instance=post)
        if post_form.is_valid():
            post_form.save()
            return HttpResponseRedirect(reverse("posts:add_post"))
    else:
        post_form = PostForm(instance=post)
    return render(request, 'main/add.html', {'post_form': post_form})'''


@permission_required("posts.can_change_post", login_url='login')
def save_post(request):
    post = get_object_or_404(Post)
    print(post)

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
        "posts/save.html",
        {"form": form}
    )

