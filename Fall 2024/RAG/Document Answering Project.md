    # Document Answering Program with RAG

## Overview
The goal of this project is to build a program that can leverage data to make LLM generations more accurate. Here's the goal of the program:
* The user (you) will ask a question about Messi
* The program will first use RAG to get the most relevant material from the messi.txt file to answer the question
* The program will then incorporate the results from RAG into a prompt into ChatGPT (or some other LLM, it doesn't matter)
* The LLM will give a response to the question (and hopefully its more accurate using RAG)

### By completing this project you will learn:
1. **OpenAI API**: How it works and how to use it
    * Using an API in general is the one of the most useful skills in programming
    * Suggested skill directly from **Lockheed Martin**
2. **Embeddings**
    * The concept of embeddings is extremely useful in ML, and you can solve a lot of problems with them if you're creative.
    * They're the building blocks for ChatGPT!

## Some tips to get started

Here's what you'll need to do in order to complete the project:
1. The first thing you'll need is an API key for OpenAi. Usually this costs money, but you can use mine for this project (please don't spam the api key I'm broke and fighting for my life). Navigate to OpenAi's Embedding api documentation to find the syntax for calling the api and creating embeddings. 
    * The api key is on the discord
2. The second thing you'll need to do is embed you reference material (the messi.txt). Here's a really simple way of doing this: 
    * Create a python dictionary with sentences as keys and embeddings as values
    * Break the messi.txt document into chunks of like 50 characters (totally arbitrary, you can choose any chunking you like), and store the chunk and its embedding in the dictionary. It should look like {"This is an example sentence": [1, 2, 5, 1, 6, ....], "Another..": [123, 1, 1, 3, 4, ...], ....}.
    * Now, create the embedding for the question, and calculate the cosine simularity for the question and each chunk
    * Take the sentences from the top 5 largest cosine simularities, and create one big string that contains the original question and each of the 5 most relevant prompts. 
    * Ask the LLM the answer to the question and get a response. 