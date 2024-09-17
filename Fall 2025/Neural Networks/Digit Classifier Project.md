
# Digit Recognition with PyTorch

## Overview
The goal of this project is to build a neural network that is able to classify handwritten digits. For example, if shown a picture of a handwritten "4", the neural network should be able to identify the image as a "4". This project is a great way to get experience not only with very common deep learning frameworks, but also to get a much better understanding of deep learning as a whole. 
### By completing this project you will learn:
1. **Pytorch**: How it works and how to use it
	* This is one of the most desired skills from recruiters in machine learning
	* Suggested from **Lockheed Martin**
2. **Neural Networks**
	* Neural Networks are the basis of all modern deep learning applications
	* Understanding neural networks is the first step in breaking into Artificial Intelligence
3. **Gradient Decent**
	* Gradient Decent is the core of literally every single deep learning architecture. It is how models "learn"
	* Understanding gradient decent will unlock many doors for future models
## How to get started

If you ever get stuck there are endless amounts of resources online (and in this document) to help!

### Setup
1. Open up Google Colab - This is an IDE, a place to write the code.
	1. Go to your google drive, click "New", then click "More", then click "Colab"
	2. Print something random to make sure its running your code
	3. This requires an internet connection, because its running code on google's CPUs. Its great, because you can train machine learning models even if your computer isn't the best.
2. Follow along with a tutorial (if you want)
	* PyTorch has a decently steep learning curve, so following along with a tutorial is a good way to get your feet under you. Just make sure you have a good understanding of whats going on!
	* This video does a good job of walking you through everything: https://www.youtube.com/watch?v=vBlO87ZAiiw&t=0s&ab_channel=NeuralNine

## PyTorch Basics

Creating a machine learning model can be thought of in terms of 3 steps:
1. Loading in the data
	* This is from 2:30 - 4:00 in the video mentioned above
2. Transforming the data so that the model can use it
	* For example, making sure all the images are the same shape
	* The transformations are already done for you in this dataset, but the Youtube video does the transformations from 6:00 - 6:30 
3. Building the model architecture
	* In the video, this happens from 7:00 - 13:30
	* This is arguably the most confusing part, but there are plenty of resources online to help explain what's going on in this part.
	* In the video, the guy uses convolutional layers (the self.conv1 layers),  and dropout layers (self.conv2_dropout). **In my opinion, this is extremely overkill and I wouldn't worry about understanding those if you're a beginner**. The important things to understand is the Linear layer, in PyTorch its called nn.Linear(). This is the basis for neural networks, and you can **learn more about them here**: https://www.youtube.com/watchv=aircAruvnKk&t=0s&ab_channel=3Blue1Brown 
4. Training the model
	* This is the easy part, you just run the training loop! 
	* This part takes the longest for your computer to run, but you don't need to be around to watch it.
	* This is the part where the neural network "learns" how to complete the task!
5. Profit
	* You can check the accuracy of your model and do whatever you want with it, but you have now trained a neural network! 

## Resources to help you

* If you are interesting in learning how neural networks work, this video is amazing: https://www.youtube.com/watch?v=aircAruvnKk&t=0s&ab_channel=3Blue1Brown

* If you just want a tutorial to walk you through training a model, here are some videos:
	* https://www.youtube.com/watch?v=vBlO87ZAiiw&ab_channel=NeuralNine
	* https://www.youtube.com/watch?v=gBw0u_5u0qU&t=0s&ab_channel=Mr.PSolver
	* https://www.youtube.com/watch?v=ijaT8HuCtIY&t=0s&ab_channel=KrishnaRamesh
