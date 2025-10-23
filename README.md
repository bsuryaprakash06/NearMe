# Ex04 Places Around Me
## Date: 23-10-2025

## AIM
To develop a website to display details about the places around my house.

## DESIGN STEPS

### STEP 1
Create a Django admin interface.

### STEP 2
Download your city map from Google.

### STEP 3
Using ```<map>``` tag name the map.

### STEP 4
Create clickable regions in the image using ```<area>``` tag.

### STEP 5
Write HTML programs for all the regions identified.

### STEP 6
Execute the programs and publish them.

## CODE

<details>
  <summary>Manhattan Map</summary>

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Explore Manhattan</title>
</head>

<body bgcolor="#f0f8ff">

    <h1 align="center" style="color: navy;">Explore Manhattan</h1>
    <h3 align="center" style="color: darkred;">Interactive Tourist Map</h3>

    <center>
        <img src="{% static 'images/nyc.png' %}" usemap="#manhattanmap" width="1400" height="800">

        <map name="manhattanmap">

            <area shape="circle" coords="150,450,25" href="{% url 'statue' %}" title="Statue of Liberty">

            <area shape="rect" coords="340,200,380,260" href="{% url 'empire' %}" title="Empire State Building">

            <area shape="circle" coords="360,180,20" href="{% url 'times' %}" title="Times Square">

            <area shape="rect" coords="280,60,500,130" href="{% url 'park' %}" title="Central Park">
        </map>
    </center>

</body>

</html>
```
</details>

<details>
  <summary>Empire State Building</summary>

```html
{% load static %}
<html>
<head>
    <title>Empire State Building</title>
</head>
<body style="background-color: #fff8dc; font-family: Georgia, serif; padding: 20px;">
    <h1 style="text-align: center; color: darkblue;">Empire State Building</h1>
    <hr style="height: 3px; background-color: blue; border: none;">
    <img src="{% static 'images/emp.jpg' %}" alt="Empire State Building"
         style="float: left; width: 200px; height: auto; border: 2px solid black; border-radius: 5px; margin-right: 20px;">
    <p style="text-align: right; font-size: 18px; width: calc(100% - 220px);">
        The Empire State Building is a 102-story Art Deco skyscraper located in Midtown Manhattan.
        Completed in 1931, it was the tallest building in the world for nearly 40 years.
        It remains a major tourist attraction with observation decks on the 86th and 102nd floors,
        offering panoramic views of New York City. The building is known for its iconic spire and colorful lighting
        displays at night.
    </p>
</body>
</html>
```
</details>

<details>
  <summary>Central Park</summary>

```html
{% load static %}
<html>
<head>
    <title>Central Park</title>
</head>
<body style="background-color: #e0ffe0; font-family: Georgia, serif; padding: 20px;">
    <h1 style="text-align: center; color: forestgreen;">Central Park</h1>
    <hr style="height: 3px; background-color: green; border: none;">
    <img src="{% static 'images/cnt.jpg' %}" alt="Central Park"
         style="float: left; width: 200px; height: auto; border: 2px solid forestgreen; border-radius: 5px; margin-right: 20px;">
    <p style="text-align: right; font-size: 18px; width: calc(100% - 220px);">
        Central Park is a large public park in the heart of Manhattan, stretching over 840 acres.
        It offers a peaceful escape from the city's hustle with scenic walking paths, lakes, gardens, and cultural
        attractions.
        The park includes landmarks like Bethesda Terrace, the Central Park Zoo, and the Great Lawn.
        It is a popular spot for walking, jogging, boating, and hosting concerts and events throughout the year.
    </p>
    <div style="clear: both;"></div>
</body>
</html>
```
</details>

<details>
  <summary>Times Square</summary>

```html
{% load static %}
<html>

<head>
    <title>Times Square</title>
</head>

<body style="background-color: #ffe4e1; font-family: Georgia, serif; padding: 20px;">
    <h1 style="text-align: center; color: crimson;">Times Square</h1>
    <hr style="height: 3px; background-color: red; border: none;">

    <img src="{% static 'images/ts.jpg' %}" alt="Times Square"
        style="float: left; width: 200px; height: auto; border: 2px solid crimson; border-radius: 5px; margin-right: 20px;">

    <p style="text-align: right; font-size: 18px; width: calc(100% - 220px);">
        Times Square is one of the most vibrant and bustling locations in New York City, known for its bright
        lights, digital billboards, and nonstop energy. Located at the junction of Broadway and Seventh Avenue,
        it is home to major theaters, restaurants, shops, and entertainment venues.
        Times Square is also famous for the annual New Year’s Eve Ball Drop celebration, attracting millions of
        viewers worldwide.
    </p>
</body>

</html>
```
</details>

<details>
  <summary>Statue of Liberty</summary>

```html
{% load static %}
<html>

<head>
    <title>Statue of Liberty</title>
</head>

<body style="background-color: #e6f2ff; font-family: Georgia, serif; padding: 20px;">
    <h1 style="text-align: center; color: darkgreen;">Statue of Liberty</h1>
    <hr style="height: 3px; background-color: green; border: none;">

    <img src="{% static 'images/stl.jpg' %}" alt="Statue of Liberty"
        style="float: left; width: 200px; height: auto; border: 2px solid green; border-radius: 5px; margin-right: 20px;">

    <p style="text-align: right; font-size: 18px; width: calc(100% - 220px);">
        The Statue of Liberty is one of the most iconic symbols of freedom and democracy in the world.
        Located on Liberty Island in New York Harbor, it was a gift from France to the United States in 1886.
        The statue was designed by Frédéric Auguste Bartholdi, with its internal structure built by Gustave Eiffel.
        The torch represents enlightenment, and the crown's seven spikes symbolize the seven continents and oceans.
    </p>
</body>

</html>
```
</details>

## OUTPUT

### Manhattan Map:
<img width="1919" height="1118" alt="image" src="https://github.com/user-attachments/assets/5b73fb1e-4c0e-4445-a72e-c4df573a1d44" />


### Empire State Building:
<img width="1919" height="1118" alt="image" src="https://github.com/user-attachments/assets/eec5999f-ca38-4bf3-8560-6fe765c1771a" />


### Central Park:
<img width="1919" height="1122" alt="image" src="https://github.com/user-attachments/assets/0c952bcd-574e-4662-8ebb-7d05f629ca93" />


### Times Square:
<img width="1919" height="1125" alt="image" src="https://github.com/user-attachments/assets/e37f0915-34de-46cc-ad99-d1b7d901c951" />


### Statue of Liberty:
<img width="1919" height="1122" alt="image" src="https://github.com/user-attachments/assets/3c6f2388-a94a-41c2-aa52-485f02267d68" />

## RESULT
The program for implementing image maps using HTML is executed successfully.
