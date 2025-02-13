from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import *
from .models import *
from django.db.models import Q

from django.http import JsonResponse
from django.conf import settings
import os

import joblib
import numpy as np

def base(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'dashboard/about.html')

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            #create a new registration object and avoid saving it yet
            new_user = user_form.save(commit=False)
            #reset the choosen password
            new_user.set_password(user_form.cleaned_data['password'])
            #save the new registration
            new_user.save()
            return render(request, 'registration/register_done.html',{'new_user':new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html',{'user_form':user_form})

def profile(request):
    return render(request, 'profile/profile.html')



@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = EditProfileForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')
    else:
        user_form = EditProfileForm(instance=request.user)
    
    return render(request, 'profile/edit_profile.html', {'user_form': user_form})

@login_required
def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        messages.success(request, 'Your account was successfully deleted.')
        return redirect('base')  # Redirect to the homepage or another page after deletion

    return render(request, 'registration/delete_account.html')
# das
import json
Structure = r"static/json/scheme.json"

@login_required
def dashboard(request):
    users_count = User.objects.all().count()
    consumers = Consumer.objects.all().count
    review_count = Review.objects.all().count()
    with open(Structure, 'r') as f:
        data = json.load(f)
    context = {
        'users_count':users_count,
        'consumers':consumers,
        'review_count':review_count,
        'barData': [10, 20, 30],
        'lineData': [30, 25, 35],
        'pieData': [10, 40, 50],
        'scatterData': [{'x': 10, 'y': 20}, {'x': 15, 'y': 10}, {'x': 20, 'y': 30}],
        'crop_data':data
        
    }
    return render(request, "dashboard/dashboard.html", context=context)


#CRUD operations start here
@login_required
def dashvalues(request):
    consumers = Consumer.objects.all()
    search_query = ""
    
    if request.method == "POST": 
        if "create" in request.POST:
            name = request.POST.get("name")
            email = request.POST.get("email")
            image = request.FILES.get("image")
            content = request.POST.get("content")

            Consumer.objects.create(
                name=name,
                email=email,
                image=image,
                content=content
            )
            messages.success(request, "Consumer added successfully")
    
        elif "update" in request.POST:
            id = request.POST.get("id")
            name = request.POST.get("name")
            email = request.POST.get("email")
            image = request.FILES.get("image")
            content = request.POST.get("content")

            consumer = get_object_or_404(Consumer, id=id)
            consumer.name = name
            consumer.email = email
            consumer.image = image
            consumer.content = content
            consumer.save()
            messages.success(request, "Consumer updated successfully")
    
        elif "delete" in request.POST:
            id = request.POST.get("id")
            Consumer.objects.get(id=id).delete()
            messages.success(request, "Consumer deleted successfully")
        
        elif "search" in request.POST:
            search_query = request.POST.get("query")
            consumers = Consumer.objects.filter(Q(name__icontains=search_query) | Q(email__icontains=search_query))

    context = {
        "consumers": consumers, 
        "search_query": search_query
    }
    return render(request, "crud/dashvalue.html", context=context)
# CRUD operations end here

# Contact start
@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for contacting us!")
            return redirect('dashboard')  # Redirect to the same page to show the modal
    else:
        form = ContactForm()

    return render(request, 'contact/contact_form.html', {'form': form})

# contact end

# review start
@login_required
def add_review(request, consumer_id):
    consumer = get_object_or_404(Consumer, id=consumer_id)
    consumer_name = consumer.name

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # Assuming you have a Review model with fields 'comment' and 'rating'
            review = form.save(commit=False)
            review.consumer = consumer
            review.save()
            # You may want to add a success message here
            return redirect('dashboard')  # Redirect to the dashboard or any other page
    else:
        form = ReviewForm()

    return render(request, 'dashboard/review.html', {'consumer_id': consumer_id, 'consumer_name': consumer_name, 'form': form})
# review end

# views.py

@login_required
def view_reviews(request, consumer_id):
    consumer = get_object_or_404(Consumer, id=consumer_id)
    reviews = Review.objects.filter(consumer=consumer)

    return render(request, 'dashboard/view_reviews.html', {'consumer': consumer, 'reviews': reviews})



import smtplib
from email.message import EmailMessage

from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages

@login_required
def send_email(request):
    if request.method == 'POST':
        receiver = request.POST.get('receiver')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[receiver],
        )
        try:
            email.send()
            messages.success(request, 'Email sent successfully!')
        except:
            messages.error(request, 'Failed to send email.')

        return redirect('send_email')

    return render(request, 'email/sendemail.html')


#101224
import hashlib
import random
from django.shortcuts import render
from django.utils.timezone import now

@login_required
def upload_image(request):
    context = {"result": None}  # Initialize context to store results

    if request.method == "POST" and request.FILES.get("image"):
        # Extract the image file
        image_file = request.FILES["image"]
        image_name = image_file.name

        # Compute the hash of the image
        hasher = hashlib.sha256()
        for chunk in image_file.chunks():
            hasher.update(chunk)
        image_hash = hasher.hexdigest()

        # Check if the image already exists in the database
        existing_prediction = ImagePrediction.objects.filter(image_hash=image_hash).first()
        if existing_prediction:
            context["result"] = {
                "message": "This image has already been uploaded.",
                "prediction": existing_prediction.prediction,
                "detection_info": existing_prediction.detection_info,
                "suggestion": existing_prediction.suggestion,
                "recommendation": existing_prediction.recommendation,
                "image_url": existing_prediction.image.url
            }
            return render(request, "agri/upload_image.html", context)

        # Fetch a random suggestion from the PlantDisease table
        random_disease = PlantDisease.objects.order_by("?").first()
        if not random_disease:
            context["result"] = {
                "message": "No suggestions available in the database. Please add plant diseases.",
            }
            return render(request, "agri/upload_image.html", context)

        # Save the image prediction in the database
        prediction = ImagePrediction.objects.create(
            image_name=image_name,
            image_hash=image_hash,
            prediction=random_disease.disease_name,
            detection_info=f"Type of Disease: {random_disease.type_of_disease}",
            fertilizer=random_disease.natural_fertilizer,
            suggestion=random_disease.suggestion,
            recommendation=random_disease.recommendation,
            uploaded_at=now(),
            image=image_file  # Save the uploaded image
        )


        # Update the context with the prediction result
        context["result"] = {
            "message": "Image uploaded successfully.",
            "prediction": prediction.prediction,
            "fertilizer": prediction.fertilizer,
            "detection_info": prediction.detection_info,
            "suggestion": prediction.suggestion,
            "recommendation": prediction.recommendation,
            "image_url": prediction.image.url  # Display the uploaded image
        }

    return render(request, "agri/upload_image.html", context)

@login_required
def display_predictions(request):
    # Retrieve all ImagePrediction objects from the database
    predictions = ImagePrediction.objects.all()

    # Pass them to the template context
    context = {
        'predictions': predictions
    }

    return render(request, "agri/display_predictions.html", context)






