from django.db.models.aggregates import Count
from profiles.models import Profile
from django.shortcuts import redirect, render
from .models import Like, Post, Comment
from .forms import PostModelForm  ,CommentModelForm
# Create your views here.

def posts_comment_create_list_view(request):

    qs = Post.objects.all()
    profile = Profile.objects.get(user = request.user)


    # initials
    p_form  = PostModelForm()
    c_form = CommentModelForm()
    post_added = False
    profile = Profile.objects.get(user = request.user)
    

    if 'submit_p_form' in request.POST:
        p_form  = PostModelForm(request.POST or None , request.FILES or None )
        if p_form.is_valid():
            instance = p_form.save(commit=False)
            instance.author = profile
            instance.save()
            p_form  = PostModelForm()
            post_added = True

    if 'submit_c_form' in request.POST:
        c_form = CommentModelForm(request.POST )
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.user = profile
            instance.post =Post.objects.get(id =request.POST.get('post_id'))
            instance.save()
            c_form = CommentModelForm()

    context = {"qs":qs ,'profile':profile , "p_form":p_form , "c_form":c_form , "post_added":post_added }
    return render(request, 'posts/main.html', context)





    
def like_unlike_post(request):
    user = request.user  #  the user who login
    if request.method == "POST":
        post_id = request.POST.get("post_id")
        post_obj = Post.objects.get(id = post_id)
        profile = Profile.objects.get(user = user) # admin

        # for liked list in Post model
        if profile in post_obj.liked.all():
            post_obj.liked.remove(profile)
        else:
            post_obj.liked.add(profile)
            
        # for Like model
    #exested 
        like , created = Like.objects.get_or_create(user=profile , post =post_obj )# (post_id = post_id)
    
        if not created:
              if like.value == 'Like':
                  like.value ='Unlike'
              else :
                  like.value='Like'
        else:
            like.value='Like'
 
            post_obj.save()
            like.save()
    return redirect ("posts:main-post-view")


