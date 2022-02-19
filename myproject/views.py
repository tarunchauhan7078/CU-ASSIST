from django.core.checks import messages
from django.http import HttpResponse
from django.http.response import Http404, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from myapp import models
from myapp.models import Post
from myapp.models import postComment
from myapp.templatetags import extras
from django.utils.datastructures import MultiValueDictKeyError
from django.urls import reverse_lazy, reverse


def index(request):
    if request.method=="POST": 
        title = request.POST.get('title','')         
        dept = request.POST.get('dept','')        
        tag = request.POST.get('tag','')  
        try:      
            image = request.FILES['img']   
        except MultiValueDictKeyError:
            image=0    
        desc = request.POST.get('description','') 
        user = request.user        
        if(int(dept)>=1 or int(dept)<=6):
            ins = Post(post_title = title,post_desc= desc,post_category= dept,post_images= image,post_user=user)
            ins.save()
            messages.success(request,"Thread posted successfully!")
            return redirect("/")
        else:
            return HttpResponseBadRequest()
        # Post.objects.create(post_category=dept,post_likes=123,post_dislikes=333)
        
    else:
        x=request.GET.get("dept",None)
        id = request.GET.get("post_id")
        if(x==None or x==0):
            posts = Post.objects.all()            
        else:
            posts = Post.objects.filter(post_category=x)           
        n = len(posts)        
        params = {'range': range(n),'post': posts,'p_id':id}
        return render(request,'index.html', params) 
        

def handleSignup(request):
    if request.method == "POST":
        # get the post parameters
        username = request.POST['uname']
        name = request.POST['name']
        uemail = request.POST['email']
        upass = request.POST['pass']
        ucpass = request.POST['cpass']        
        # check for error in input
        if len(username)>10:
            messages.error(request,"Username must be less than 10 characters!")
            return redirect("/")
        if not username.isalnum():
            messages.error(request,"Username should only contain letters and numbers!")
            return redirect("/")
        if upass != ucpass:
            messages.error(request,"Please confirm your password again!")
            return redirect("/")

        # create the user
        myuser= User.objects.create_user(username, uemail, upass)
        myuser.name=name
        myuser.save()
        messages.success(request,"Your account has been created successfully!")
        return redirect('/')
    else:
        return HttpResponseBadRequest()

def handleLogin(request):
    if request.method == "POST":
       # get the post parameters        
        uname = request.POST['uname']
        upass = request.POST['pass']
        user = authenticate(username=uname, password=upass)

        if user is not None:       
            login(request, user)
            messages.success(request,"Successfully Logged in")
            return redirect('/')
        else:
            messages.error(request,"Invalid credentials! Try again")
            return redirect('/')
    else:
        return HttpResponse('404- Not found')
        

def handleLogout(request):
    logout(request)
    messages.error(request,"Successfully Logged Out!")
    return redirect('/')

def handlePostview(request,slug,id):    
    post_id=id    
    posts = Post.objects.get(id=post_id)    
    comment = postComment.objects.filter(post=posts, parent=None)
    replies = postComment.objects.filter(post=posts).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    params = {'post': posts,'comments':comment,'user':request.user,'replyDict':replyDict}

    return render(request, 'comments.html',params)

def postComments(request):    
    if request.method == "POST": 
        comment = request.POST.get("comment")       
        user = request.user
        postSno = request.POST.get("postSno")         
        post=Post.objects.get(id = postSno)   
        parentSno = request.POST.get("parentSno")         
        if parentSno == "":
            comment= postComment(comment=comment, user=user,post=post)
            comment.save()
            messages.success(request,"Your comment has been posted successfully!")
        else:
            parent = postComment.objects.get(sno=parentSno)
            comment= postComment(comment=comment, user=user,post=post,parent=parent)
            comment.save()
            messages.success(request,"Your have replied to this comment successfully!")
        
    return redirect(f"/postview/{post.slug}/{postSno}")

def handlePostLikes(request,id):
    post = get_object_or_404(Post, id = request.POST.get('post_id'))
    liked = False
    if post.post_likes.filter(id=request.user.id).exists():
        post.post_likes.remove(request.user)
        liked= False
    else:
        post.post_likes.add(request.user)    
        liked = True
    
    return redirect('/')

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
def postDislikes(request, id):
    
    if request.method == "POST":
        idd = id
        print("================================received id: ")
        print(idd)
        post=Post.objects.get(id=idd)
        is_like=False

        for post_likes in post.post_likes.all():
            if post_likes == request.user:
                is_like= True
                break

        if is_like:
            post.post_likes.remove(request.user)        

        is_dislike= False
        for post_dislikes in post.post_dislikes.all():
            if post_dislikes == request.user:
                is_dislike = True
                break

        if not is_dislike:
            post.post_dislikes.add(request.user)

        if is_dislike:
            post.post_dislikes.remove(request.user)

        next =request.POST.get('/')
        return HttpResponseRedirect(next)