If you haven't already, checkout the github: https://github.com/JPM2002/Tech-Team---Nittany-Ai

General Structure
----------

MLB for the Fall will have 4 “sections” over the course of the semester. Each section will have a corresponding list of project options aimed to give experience in that section of AI. Meetings will not be related to the projects directly, but instead aim to introduce the current section through games and fun visualizations.

  

Additionally, at the end of the semester we are planning to have a mock technical interview, where each person who is interested in the certificate will have a chance to practice interviewing skills. Prize for the top interviewee as well.

  

In order to get the certificate, students will have to complete a certain amount of “points” and the technical interview. Each project is worth a different amount of points (most are the same, but some bonus projects are worth a lot more because they are substantially more involved). The standard projects are expected to take ~2 hours per week for a beginner, and the bonus projects take around 3 times that. Additionally, I was planning on giving awards to those with the highest points.

  

Sections
----------

1.  White box models
    
2.  Neural Networks
    
3.  Fine tuning
    
4.  RAG
    

  

Certificate Requirements
----------

You need 21 points to get the certification

-   Meetings are 1 point
    
-   Most projects are 3 points
    
-   Bonus projects are worth a lot more (depending on the project)
    
-   Games during the meetings will offer point awards to winners, usually 1 point
    

  

Explanation: I feel like a fair bar to set is 9 out of 11 meetings and 3 completed projects, one from each section. Obviously we can make exceptions for people that can’t make meetings or are struggling with certain projects. This isn’t a rigid requirement, just something for students to aim at.

  

MLB Dates
----------

### Introduction: One meeting

Sept 11

### White Box Models: 2 weeks

Sept 18

Sept 25

  

### Neural Networks: 3 weeks

Oct 2

Oct 9

Oct 16

  

### Fine Tuning: 2 weeks

Oct 23

Oct 30

  

### Rag: 2 weeks

Nov 6

Nov 13

  

### Technical Interview: 1 meeting

Nov 20

  
  

Project Due Dates
----------

White Box: Sept 27

Neural Network: Oct 18

Fine Tuning: Nov 1

RAG: Nov 15

  
  

Project Options: 
----------

### White Box Model Projects:

  

#### Build a model to classify flowers

This is like this print(“Hello world”) of AI. There are a ton of videos online doing this, and it teaches you a lot of the fundamentals.

  

Difficulty: 2/10

  

Tips: I made a little document outlining generally how to do this if you're stuck or don’t know where to start.

  

#### Build a model from Scratch:

If you are interested in getting a deep understanding of how these fundamental models work under the hood, then this is a great opportunity for you. Build your choice of Random forest from scratch, SVMs from scratch, Linear regression from scratch, or any other model you find interesting.

  

Difficulty (depending on the model you build from scratch): If you are looking for a very easy project, Linear regression is certainly the easiest and very approachable. If you are looking for something more difficult, Random forest or SVMs are slightly more complex (and a lot more practical, too). Logistic regression sits in the middle, and is also very approachable.

  

Tips: There’s a ton of tutorials on youtube about how to build these things from scratch.

  

#### House evaluation project with Zillow dataset:

If you’re really into real estate then this is a super practical project for you. The entire job of a successful real estate investor is being able to accurately predict the value of a property. What if you could make an AI to do it? This is an application of AI that is being used in the real world right now, and if you’re able to make a model better than what others have made in the past, you’ve got some real money in your hands lol!

  

Difficulty: 5/10. It really depends on how good you want your model to be, so be creative! Who knows, maybe you’ll have the next innovation in real estate…

  

Tips: When you're thinking about how to make your model better, think about what information you would use as a human to make a better prediction. When valuing a house, maybe you think about how big it is, how many bedrooms, the value of houses in the same area, etc. The more information like this that you provide your model, the better it will do!

  
  
  

### Neural Network Projects:

  

#### Beginner - MNIST Classification with PyTorch:

Most employers of AI applications use a python library called PyTorch to build and develop AI, so it's probably best for you to get some experience with it. The problem is, however, that it kinda has a learning curve (I hate it tbh). It's really good when you know what you’re doing, but unfortunately you have to actually get some practice first.

  

Difficulty: 4/10

  

Tips: Follow along with a youtube video, and when they do something you don’t understand, investigate! Try changing up the model architecture from the video, and see if that changes anything!

  

#### Intermediate - Dog and Cat Classification with PyTorch:

This is very similar to the MNIST option, except this is a lot harder and requires some more advanced techniques. Namely, you’ll have to use a technique called “Convolutional Neural Networks” in order to get any good results. Even with a youtube video guide this problem can be really hard, so don’t get discouraged when it doesn’t work on the first try!

  

Difficulty: 7/10

  

Tips: Follow along with a youtube video, and train the model overnight. This model will need to be a lot larger, so it will likely take a couple hours to train. Use google collab, it's got way better GPUs than your personal computer probably!

  

#### Bonus - Neural Network from scratch (BIG POINTS):

This was the first AI project I ever did, and it was incredibly transformative. If neural networks seem like black magic to you, this project is amazing at “demystifying” everything.

  
  

Difficulty: 9/10

  

Tips: If you don’t have any experience in AI, this shit is hard lol. But not impossible at all! There are a ton of video guides on youtube that walk you through how to do this. The hardest part is understanding “Gradient Decent”, but as it turns out, that’s the most important algorithm in AI by a million miles, so it's worth it.

  

If you are having trouble with this at all, let us know! We would be more than happy to help out.

  

### Fine Tuning Projects:

  

#### Fine tune a stable diffusion model to generate pictures of yourself

There’s so many creative things you can do with this, I think it's really fun. Also, most applications make you pay for something like this, so you can code it yourself and save money.

  

Difficulty: 5/10

  

Tips: As always, try following a youtube video. Doing is the best way to learn, and youtube is the goat for tutorials!

  
  

#### Fine tune an LLM to speak in a specific way, i.e. speak like Shakespeare all the time or like a Hippie.

This will give you a good understanding of how to use LLMs in a more fine grained way. Plus, you get a funny talking LLM at the end of it.

  

Difficulty: 4/10

  

Tips:  The hardest part of this is probably finding a good dataset. Look on Kaggle.com, or general text locations. You can try web scraping too, if you’re feeling ambitious!

  

#### Fine tune an LLM to be an expert in a certain task

This is actually the exact same as the option above, except the data you use will need to be different.

  

Difficulty: 4/10

  

Tips: When you deploy models in the real world, you need to test them to see how well they perform. In order to do this, ask your LLM questions about the subject that you trained it on, and measure its performance. This sounds small, but this is often the most important part of developing AI in industry.

  
  
  

#### Fine tune the RESNET model to classify Cats and Dogs

It’s usually impractical to train an entire model from scratch for whatever you’re doing. That’s why most people take a model that’s already been trained on a similar task (RESNSET in our case) and fine tune it on your specific task (classifying cats and dogs in our case). It’s a lot more effective!

  

Difficulty: 5/10

  

Tips: As always, make sure to follow a tutorial online. The RESNET model is pretty big, so downloading it might take a while. The idea of fine tuning is to only change the last layer of neurons during training, so that it keeps its general intelligence but it’s more specific to your specific task.

  

### RAG Projects:

  

#### Create the game [Contexto.me](http://contexto.me):

Trying playing the game at the website! It's like a NYT typa game, I think it's pretty fun. Its not too hard to build, either!

  

Difficulty:  4/10

  

Tips: Try playing around with embeddings first, and messing with cosine similarity. Here’s a cool trick you could try: If you take the embedding for “King”, and then you subtract the embedding for “Man”, and then add the embedding for “Women”, you get a vector that is pretty close to the embedding for “Queen”! It’s almost like the embeddings have “embedded” meaning (because they kinda have)!

  

#### Document answering app:

This is a REALLY common application of AI, and knowing how to make an app like this is REALLY USEFUL!! There’s a python library called “Langchain” that makes this process really easy.

  

This project is like less than 50 lines of code, but we made it a whole project because of how useful it is in industry. Knowing how to do something like this will be extremely applicable in your career (at least for now, who knows what the industry looks like in 2 years).

  

Difficulty: 3/10

  

Tips: You could use Langchain, and set up an OpenAi api account. Doing it without langchain isn’t hard either, some people think it's actually easier, but either way there are a ton of tutorials online that you can use.