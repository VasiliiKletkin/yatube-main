from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import datetime as dt

from yatube.settings import POSTS_IN_PAGINATOR
from .models import Post, Group
from .forms import PostForm, CommentForm


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, POSTS_IN_PAGINATOR)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    current_year = dt.datetime.now().year

    return render(request, "posts/index.html", {"page": page, "year": current_year})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    paginator = Paginator(posts, POSTS_IN_PAGINATOR)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        "group": group,
        "page": page
    }

    return render(request, "posts/group.html", context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts = author.posts.all().order_by("-pub_date")
    paginator = Paginator(posts, POSTS_IN_PAGINATOR)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        'page': page,
        'author': author,
        "posts_count": author.posts.count()
    }

    return render(request, 'posts/profile.html', context)


def post_view(request, username, post_id):
    post = get_object_or_404(Post, author__username=username, pk=post_id)
    author = post.author
    posts_count = author.posts.count()
    form = CommentForm
    comments = post.comments.select_related('author').all()

    context = {
        "post": post,
        "author": author,
        "posts_count": posts_count,
        'form': form,
        'comments': comments
    }

    return render(request, 'posts/post.html', context)


@login_required
def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("index")
    form = PostForm()

    context = {
        "form": form,
    }

    return render(request, "posts/new_post.html", context)


@login_required
def post_edit(request, username, post_id):
    post = get_object_or_404(Post, author__username=username, pk=post_id)

    if request.user == post.author:
        form = PostForm(instance=post, data=request.POST or None, files=request.FILES or None)

        if form.is_valid():
            form.save()

            return redirect('post', username=username, post_id=post_id)

        context = {
            'form': form,
        }

        return render(request, 'posts/post_edit.html', context)

    else:
        return redirect('post', username=username, post_id=post_id)


def page_not_found(request, exception):
    # Переменная exception содержит отладочную информацию,
    # выводить её в шаблон пользователской страницы 404 мы не станем
    return render(
        request,
        "misc/404.html",
        {"path": request.path},
        status=404
    )


def server_error(request):
    return render(request, "misc/500.html", status=500)


@login_required
def add_comment(request, username, post_id):
    post = get_object_or_404(Post, author__username=username, pk=post_id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.author = request.user
        new_comment.post = post
        new_comment.save()
    return redirect('post', username, post_id)
