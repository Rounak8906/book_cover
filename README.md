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
</html><!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Book Cover</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f4f4f4;
      text-align: center;
    }

    .book-container {
      position: relative;
      display: inline-block;
      margin: 20px;
    }

    .book-cover {
      height: 750px;
      width: 600px;
      display: block;
    }

    .author-image {
      position: absolute;
      bottom: 40px;
      right: 3px;
      width: 120px;
      height: 120px;
      border: 1px solid black;
      box-shadow: 0 0 8px rgba(0,0,0,0.5);
      border-radius: 100px;
    }

    .top{
      position: absolute;
      top: 290px;
      width: 35%;
      border: 0;
      border-top: 1px solid darkslategrey;
      margin: 10px auto;
    }


    .edition{
      position: absolute;
      top: 270px;
      color: grey;
      font-family: 'Courier New', Courier, monospace;
      font-size: larger;
      left: 25px;
      margin: 10px auto;

    }
    .bottom{
      position: absolute;
      bottom: 80px;
      width: 29%;
      border: 0;
      border-top: 1px solid darkgray;
      margin:0 0 10px 300px; 

    }
    .author{
      position: absolute;
      bottom: 80px;
      right: 130px;
      color: #F6F5AE;
      font-family: 'Courier New', Courier, monospace;
      font-size: larger;
      margin: 10px auto;
    }
    .title {
    position: absolute;
    top: 40px;
    width: 100%;
    font-family: Georgia, 'Times New Roman', Times, serif;
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    color:darkslategray;
    }

    .subtitle {
    position: absolute;
    top: 150px; 
    font-family: Georgia, 'Times New Roman', Times, serif;
    width: 100%;
    text-align: center;
    font-size: 20px;
    color: slategrey;
    }
    
    body{
            background-image: url("{% static 'bgexp61.jpg' %}");
            height: 100vh;
            background-size: cover;
            background-position: center;
        }
  </style>
</head>
<body>
  
    <div class="book-container">
    <div class="title">THE VOYAGE OF THE BEAGLE</div>
    <div class="subtitle">A Naturalist’s Journal of Researches Around the World</div>
    <span class="edition"><strong>ORIGINAL EDITION</strong></span>
    <hr class="top">
    <hr class="bottom">
    <span class="author">CHARLES DARWIN</span>
    <img src="{% static 'bookcover.png' %}" alt="Book Cover" class="book-cover">

    <!-- Author photo -->
    <img src="{% static 'CHARLESDARWIN.png' %}" 
    alt="Author" class="author-image">
</div>
</body>
</html>



```
# OUTPUT:
![alt text](front/bookcoverss.png)
# RESULT:
The program for designing book front cover page using HTML and CSS is completed successfully.
