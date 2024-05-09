# Introduction

Detection and tracking of football players using YOLO and OpenCV. YOLO is a real-time object detection model. You can read the documentation [here](https://docs.ultralytics.com/).

I'll be using a dataset from Kaggle called [DFL - Bundesliga Data Shootout](https://www.kaggle.com/competitions/dfl-bundesliga-data-shootout).


The main objective of this project is to try to detect and track football players in order to determine statistics such as each player's speed, distance covered and ball possession for each team.

## Plan
First, I'll start by detecting the football players using yolov8x model.

Once the detection has been carried out, I'll train the model to improve its ability to detect the ball, but also to filter out the classes that the model detects but that aren't useful to us. I'm going to use a dataset of around 600 images found on Roboflow to train the model. I would have liked to find a dataset with more images, but this will already helps us. Here are what I'm trying to do:
- Differentiate between goalkeepers, players and detect referees
- Improving ball detection
- Filtering people that are off the field

Then, I'll segment the players according to their team using the color of their jersey.
- Cluster pixels of the jerseys of each player using KMeans Clustering

Next, I'll be measuring Camera Movement and Perspective Transformation to get distance of the players not in pixels but in actual meters.

Finally, I'll be measuring each player's speed and distance covered.