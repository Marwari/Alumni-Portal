from __future__ import unicode_literals

import os
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from AlumniPortal.settings import BASE_DIR
from imgurpython import ImgurClient

from .forms import PostForm, SignUpForm, LoginForm

from .forms import LikeForm, CommentForm
from .models import UserModel, LikeModel, PostModel, CommentModel, SessionToken

#Signup view starts here
def SignupView(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # saving data to DB
            user = UserModel(name=name, password=make_password(password), email=email, username=username)
            user.save()
            return render(request, 'signup_success.html')
            # return redirect('login/')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

# Login view starts here
def LoginView(request):
    response_data = {}
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = UserModel.objects.filter(username=username).first()

            if user:
                if check_password(password, user.password):
                    token = SessionToken(user=user)
                    token.create_token()
                    token.save()
                    response = redirect('/')
                    response.set_cookie(key='session_token', value=token.session_token)
                    return response
                else:
                    response_data['message'] = 'Incorrect Password! Please try again!'
            else:
                response_data['message'] = 'User does not exist!!!!'

    elif request.method ==  'GET':
        form = LoginForm()

    response_data['form'] = form
    return render(request, 'login.html', response_data)

# Feed view starts here
def FeedView(request):
    user = CheckValidation(request)
    if user:
        posts = PostModel.objects.all().order_by('-created_on')

        for post in posts:
            existing_like = LikeModel.objects.filter(post_id=post.id, user=user).first()
            if existing_like:
                post.has_liked = True

        return render(request, 'feed.html', {'posts': posts})
    else:

        return redirect('/login/')

# Post view starts here
def PostView(request):
    user = CheckValidation(request)
    if user:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                image = form.cleaned_data.get('image')
                caption = form.cleaned_data.get('caption')

                # saving post in database

                post = PostModel(user=user, image=image, caption=caption)
                post.save()

                path = os.path.join(BASE_DIR, post.image.url)

                client = ImgurClient('c83158842a9256e', 'ba219c35073b2a80347afaf222e1ebc28dcc8e1a')
                post.image_url = client.upload_from_path(path, anon=True)['link']

                #post.image_url = cloudinary.uploader.upload(path)
                post.save()
                return redirect('/')

        else:
            form = PostForm()
        return render(request, 'post.html', {'form': form})
    else:

       return redirect('/login/')

# Like view starts here
def LikeView(request):
    user = CheckValidation(request)
    if user and request.method == 'POST':
        form = LikeForm(request.POST)
        if form.is_valid():
            post_id = form.cleaned_data.get('post').id
            existing_like = LikeModel.objects.filter(post_id=post_id, user=user).first()
            if not existing_like:
                LikeModel.objects.create(post_id=post_id, user=user)
            else:
                existing_like.delete()
            return redirect('/')
        else:
            return redirect('/login/')

# Comment starts here
def CommentView(request):
    user = CheckValidation(request)
    if user and request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            post_id = form.cleaned_data.get('post').id
            comment_text = form.cleaned_data.get('comment_text')
            comment = CommentModel.objects.create(user=user, post_id=post_id, comment_text=comment_text)
            comment.save()
            return redirect('/')
        else:
            return redirect('/')
    else:
      return redirect('/login')

# Validation of the session
def CheckValidation(request):
    if request.COOKIES.get('session_token'):
        session = SessionToken.objects.filter(session_token=request.COOKIES.get('session_token')).first()
        if session:
           return session.user
    else:
        return None

def LogoutView(request):
    response = redirect("/")
    response.delete_cookie("session_token")
    return response

def MembersView(request):
    user = CheckValidation(request)
    if user:
        return render(request, 'members.html')
def EventsView(request):
    user = CheckValidation(request)
    if user:
        return render(request,'events.html')
def AboutView(request):
    user = CheckValidation(request)
    if user:
        return render(request, 'about_us.html')
def ContactView(request):
    user = CheckValidation(request)
    if user:
        return render(request, 'contact_us.html')
def ForgotView(request):
    return render(request, 'forgot_password.html')