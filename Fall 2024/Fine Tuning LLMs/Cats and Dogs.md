
# Cats and Dogs classification with Tensorflow

**IMPORTANT:** This task is really hard, so if you can't get a great accuracy don't sweat it, just submit what you have. Challenge yourself to get good accuracy, though!

## Overview
The goal of this project is to train a model that can classify an image as either a cat or a dog, given an image of one of them.

As it turns out, this problem is pretty hard in general. Images of cats and dogs are not standardized at all, unlike the MNIST dataset with digits. The cat/dog could be laying down, standing up, sitting, different colors, in different parts of the image, etc. For this reason, our model needs to be pretty big in order to be smart enough to classify cats and dogs.

Instead of doing a bunch of work to figure out the ideal architecture and training, lets steal someone else's work! (kind of)

### By completing this project you will learn:
1. **Fine Tuning:** One of the most important skills in industry. Fine tuning saves time, computation, cost, and improves acccuracy. It really doesn't get any better than that!
2. **Keras:** You'll be using Keras to load in the pretrained model and fine tune it.
3. **Pandas:** The classic. This package is used pretty much every single time. 


## How to get started

If you ever get stuck there are endless amounts of resources online (and in this document) to help!

Here's a top down view of what we are doing:
1. First we look at our dataset. Its a bunch of images of cats and dogs, and we want to classify each image as either a cat or a dog.
2. Next we load in the ResNet50 model, which is a pretrained image model that already has a bunch knowledge in animal classification. We'll fine tune this model to specifically classify our cats and dogs.
3. We cut the top layer of the model off (which is done when we load the model with "include_top=False"), and add our own. Since we are doing a binary classification, we should replace the final layer with 1 neuron.
4. Finally, we train the adjusted model on our cats and dogs dataset, and let the model fine tune to this specific task.
5. Win/Profit (just make some predictions lol).

### Setup
1. Download the starter code from the Github (under the "Fine Tuning" folder)
	* Drag and drop this file into your Google Drive, and you should be able to open it up and start editing.
2. Follow along with a tutorial (if you want)
	* PyTorch has a decently steep learning curve, so following along with a tutorial is a good way to get your feet under you. Just make sure you have a good understanding of whats going on! 
	* This video does a good job of walking you through everything: https://www.youtube.com/watch?v=K0lWSB2QoIQ

	* If you would rather use Tensorflow (which is a lot easier, but isn't used it industry very often), this video does a good job of walking through the steps: https://www.youtube.com/watch?v=JcU72smpLJklist=PLQVvvaa0QuDfhTox0AjmQ6tvTgMBZBEXN 



## Resources to help you

* A basic youtube search will give you a ton of options, if the ones below aren't great for you.
    * ChatGPT/Claude are both really good at this kind of thing, so ask them if you ever need help!

* PyTorch tutorial: https://www.youtube.com/watch?v=K0lWSB2QoIQ
    
* Tensorflow tutorial: https://www.youtube.com/watch?v=JcU72smpLJklist=PLQVvvaa0QuDfhTox0AjmQ6tvTgMBZBEXN 

* If you just want a tutorial to walk you through training a model, here are some videos:
	* https://www.youtube.com/watch?v=vBlO87ZAiiw&ab_channel=NeuralNine
	* https://www.youtube.com/watch?v=gBw0u_5u0qU&t=0s&ab_channel=Mr.PSolver
	* https://www.youtube.com/watch?v=ijaT8HuCtIY&t=0s&ab_channel=KrishnaRamesh


## Requirements for the project:
* Load in the pretrained model, and adjust its top layer to fit your specific use case
* Train the model on the cats and dogs dataset (which is loaded in for you)
* Make some predictions
* Accuracy doesn't matter! Challenge yourself to get above 0.8, but don't worry if its lower.