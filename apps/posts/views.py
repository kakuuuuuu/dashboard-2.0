from django.shortcuts import render, redirect
from models import User, Post, Comment
from datetime import datetime
def makePost(request,user_id):
    user=User.objects.get(id=user_id)
    print user
    print request.user
    Post.objects.create(post=request.POST['post'],created_at=datetime.now(),user=request.user,reciever=user)
    # Post.objects.create(post=request.POST['post'],created_at=datetime.now(),user=request.user,reciever=user)
    url='/users/'+str(user_id)
    return redirect(url)
def makeComment(request,user_id,post_id):
    post=Post.objects.get(id=post_id)
    Comment.objects.create(comment=request.POST['comment'],created_at=datetime.now(),post=post,user=request.user)
    url='/users/'+str(user_id)
    return redirect(url)
def deletePost(request,user_id,post_id):
    Post.objects.get(id=post_id).delete()
    url='/users/'+str(user_id)
    return redirect(url)
def deleteComment(request,user_id,comment_id):
    Comment.objects.get(id=comment_id).delete()
    url='/users/'+str(user_id)
    return redirect(url)
# Create your views here.
