# Ex.06 Book Front Cover Page Design
# Date:
# AIM:
To design a book front cover page using HTML and CSS.

# DESIGN STEPS:
## Step 1:
Create a Django Admin project.

## Step 2:
Create an app in the Django interface.

## Step 3:
Create a folder named 'static' in the app folder.

## Step 4:
Create a new HTML file in the static folder.

## Step 5:
Write the HTML code with relevant CSS properties.

## Step 6:
Choose the appropriate style and color scheme.

## Step 7:
Insert the images in their appropriate places.

## Step 8:
Publish the website in the LocalHost.

# PROGRAM:
views.py
```
from django.shortcuts import render


def frontcover(request):
    return render(request, 'frontcover.html')
```
urls.py
```
from django.contrib import admin
from django.urls import path
from cover import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.frontcover, name='home'),
]
```
frontcover.html file
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Book Cover</title>

  <style>
   
    body {
      margin: 0;
      font-family: Arial, sans-serif;
      background-image: url("{% static 'bgexp61.jpg' %}");
      background-size: cover;
      background-position: center;
      min-height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
    }

    .book-container {
      position: relative;
      width: 600px;
      height: 750px;
    }
    .book-cover {
      width: 100%;
      height: 100%;
      display: block;
    }

   
    .inner-border {
      position: absolute;
      top: 10px;
      left: 10px;
      right: 10px;
      bottom: 10px;
      border: 5px solid rgba(0,0,0,0.5);
      pointer-events: none;
    }

    .title {
      position: absolute;
      top: 40px;
      width: 100%;
      text-align: center;
      font-family: Georgia, 'Times New Roman', Times, serif;
      font-size: 45px;
      font-weight: bold;
      color: darkslategray;
    }

    .subtitle {
      position: absolute;
      top: 150px;
      width: 100%;
      text-align: center;
      font-family: Georgia, 'Times New Roman', Times, serif;
      font-size: 20px;
      color: slategrey;
    }

    .edition {
      position: absolute;
      top: 270px;
      left: 25px;
      font-family: 'Courier New', Courier, monospace;
      font-size: larger;
      color:darkslategrey;
    }

    .top {
      position: absolute;
      top: 290px;
      width: 34%;
      border: 0;
      border-top: 3px solid darkslategrey;
      margin:0 0 10px auto;
      left: 14px;
    }

    .bottom {
      position: absolute;
      bottom: 70px;
      width: 29%;
      border: 0;
      border-top: 3px solid darkgray;
      margin:0 0 10px 300px; 
      right:140px;
    }

    .author {
      position: absolute;
      bottom: 80px;
      right: 150px;
      font-family: 'Courier New', Courier, monospace;
      font-size: larger;
      color: #F6F5AE;
    }

    
    .author-image {
      position: absolute;
      bottom: 40px;
      right: 20px;
      width: 120px;
      height: 120px;
      border: 1px solid black;
      box-shadow: 0 0 8px rgba(0,0,0,0.5);
      border-radius: 100px;
    }
  </style>
</head>
<body>


  <div class="book-container">

    <div class="title">THE VOYAGE OF THE BEAGLE</div>
    
      <div class="subtitle">A Naturalist's Journal of Researches Around the World</div>
      <span class="edition"><strong>ORIGINAL EDITION</strong></span>
      <hr class="top">
      <hr class="bottom">

      <span class="author">CHARLES DARWIN</span>

     <img src="{% static 'bookcover.png' %}" alt="Book Cover" class="book-cover">
      <div class="inner-border"></div>

    <img src="{% static 'charlesdarwinimg.png' %}" alt="Author" class="author-image">
   </div>
  </div>


  
    <div class="book-container">
    <div class="title">THE VOYAGE OF THE BEAGLE</div>
    <div class="subtitle">A Naturalist’s Journal of Researches Around the World</div>
    <span class="edition"><strong>ORIGINAL EDITION</strong></span>
    <hr class="top">
    <hr class="bottom">
    <span class="author">CHARLES DARWIN</span>
    <img src="{% static 'bookcover.png' %}" alt="Book Cover" class="book-cover">
    <img src="{% static 'unnamed.jpg' %}" 
    alt="Author" class="author-image">
</div>

</body>
</html>

```
# OUTPUT:
![alt text](coverfront.png)
# RESULT:
The program for designing book front cover page using HTML and CSS is completed successfully.
