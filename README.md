# Introduction

Detection and tracking of football players using YOLO and OpenCV. YOLO is a real-time object detection model. You can read the documentation [here](https://docs.ultralytics.com/).

I'll be using a dataset from Kaggle called [DFL - Bundesliga Data Shootout](https://www.kaggle.com/competitions/dfl-bundesliga-data-shootout).


The main objective of this project is to try to detect and track football players in order to determine statistics such as each player's speed, distance covered and ball possession for each team.

## Plan

Therefore, I'll be using YOLO to detect and track the players. I'll also train the model using datasets on Roboflow to improve the output of the base model.
- Differentiate between goalkeepers and players and detect referees
- Improving ball detection and tracking accuracy

Then, I'll segment the players according to their team using the color of their jersey.
- Cluster pixels of the jerseys of each player using KMeans Clustering

Next, I'll be measuring Camera Movement and Perspective Transformation to get distance of the players not in pixels but in actual meters.

Finally, I'll be measuring each player's speed and distance covered.