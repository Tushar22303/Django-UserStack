from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator


# View all Post
def post_list(request):
    query = request.GET.get('q', '')
    posts = Post.objects.all().order_by('-created_at')

    # for searching
    if query:
        posts = posts.filter(
            Q(title__icontains=query)
        )

    # Pagination
    paginator = Paginator(posts, 6) # 6 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'posts/post_list.html', {'page_obj': page_obj, 'query': query})


# View only current logged-in posts (my post)
@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'posts/my_posts.html', {'posts': posts})


# Create Post 
@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post Created Successfully!')
            return render(request, 'posts/post_form.html', {
                'form': PostForm(),
                'success': True
            })      
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html', {'form': form})



# Update Post
@login_required
def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id, author=request.user)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post Updated Successfully!')
            return render(request, 'posts/post_form.html', {'form':form, 'success':True})      
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_form.html', {'form': form})


# Delete Post
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id, author=request.user)
    if request.method == "POST":
        post.delete()
        messages.success(request, 'Post Deleted Successfully!')
        return render(request, 'posts/post_confirm_delete.html', {'post': post, 'success': True})
    return render(request, 'posts/post_confirm_delete.html', {'post': post})

