# Predicting Flower Types
## Overview

Your friend John is a flower farmer, but he's an idiot. Despite studying agriculture for 5 years, he doesn't know how to classify the different types of flowers for his client. He needs something that will classify the different flowers for him by using the properties of flowers, since he can't figure it out himself. He called you to help you him out.

He gave you a dataset that has a bunch of instances of flowers. It can in the form of a .csv file, kind of like an excel spreadsheet. Each row represents a different type of flower, and each column represents a feature of that flower(like petal length, sepal length, etc.). 

Train an Ai to classify the different flowers for your friend John, since he can't even do his own job.    

## Getting started

Open a Google Collab file through google drive, or just open a jupyter notebook file locally. Typically AI engineers work in notebooks and not normal python files, because it's a lot easier to visualize things that way.

Download the data from [here](https://www.kaggle.com/datasets/uciml/iris), and try loading the dataset into the google notebook with Pandas. If you're not sure how to do this, check out [this video](https://www.youtube.com/watch?v=VCllZKM7Njk).

## Training your model

There is 4 major steps in training a basic Ai model:
1. Split your data into <ins>training</ins> and <ins>testing</ins>, and then each of those groups into X and Y.
2. Load in the desired model from Sklearn
3. Call the model.fit(X, Y) method, and wait for your model to train
4. Test the performance of your model

[This video](https://www.youtube.com/watch?v=f3ZJbTyz_pU) does a good job of walking you through the steps for the Logistic Regression. The process is pretty similar for every other model, the only line that changes is the line where you define your model. 
 
Typically, it is good practice to try a couple of different models on the dataset to see which one will work best. Look through the following models and try that ones that interest you. Try to get the best performance you can!

### Linear Regression

### Support Vector Machine (SVM)

### Random Forest

### K Nearest Neighbors  (KNNs)


## Looking at your model's performance

When you train Ai models, one of the most importance parts of the process is seeing how good your model actually is. There's a couple ways to do this, but we'll keep it simple, since your friend John isn't the sharpest tool in the shed.

Since we're training a classification model (a model that predicts classes, instead of a regression model that predicts numbers), the simplest way that we can measure performance is by looking at its **accuracy**. This is just the number of correct predictions divided by the number of total predictions, as you might expect.

Additionally, you could use the .score method, as described in the video recommended above. This is easier to calculate but a little harder to interpret. It's very similar to an $r^2$ value, but it can be negative as well.

### How to calculate accuracy

Get a subset of the dataset, however you want to do it. Have your model make a prediction for each instance in the dataset, and put all the predictions in a list.

Then, loop through the list and check how many predictions your model got right. Divide this number by the length of the list to get your models accuracy. 

Typically, anything above 85% is consider really good.        
