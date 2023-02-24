#!/usr/bin/env python3

#Import the 'random' module.
#Define a dictionary called 'questions' with four keys, each representing a question about favorite winter activities, personalities, Disney songs, and magical powers. 
#The values for each key are lists containing four possible answer choices.
#Define a dictionary called 'results' with four keys, each representing a Frozen character, and the values are two answer choices that correspond to that specific character
#Define an empty list called 'user_answers'.
#Create a 'for' loop that iterates through each key-value pair in the 'questions' dictionary. 
#But within the loop
#Print the question to the console.
#Print each answer choice as a numbered list to the console.
#use a "try-except" block to get the user's answer as an integer
# If the user enters a number outside the range of valid answer choices, raise a "ValueError" and prompt the user to enter a valid number.
#If the user's answer is valid, append the corresponding answer choice to the 'user_answers' list and exit the 'while* loop #define a function called "determinw_result that takes in the "user_answers" list as an argument
#IN the functioncreate an empty dictonary called "match _counts" with keys that correspond to the fur frozen characters #iterate through the "user answers" list and check if any of the answers match the values for that key in the "result" dictonary.
# if a match is found, put the corresponding key in the "match_counts" disctonary.
# find eh maxium value in the "match_ counts dictonary
#Create a list called "possible _results" containing all keys from the "match_counts" dictonary that have a valueequal to the maximum value #return the "possible_result"list
#Calll the "determine result" function with the "user_answers: list as an argument and assign the result to a variable called "possible_results"
#Check if the "possible_results" list is empty
# if it is print an error message indicating that the program could not determine the user's result.
# randomly select a result from thr "possible_results" list using the "random. choice)" function and assign it to a variable called "result"
#Print a message to the console indicating which Frozen character the user is most like using the "result" variable.



import random

print("Hello! Let's play 'What Frozen Character Are You?'")
name = input("What is your name? ")
print(f"Welcome, {name}!")

# Define a list of questions with their corresponding answer choices, themed around Frozen characters
questions = {
    "What's your favorite winter activity?": ["Building a snowman", "Ice skating", "Sledding", "Drinking hot cocoa"],
    "Which of these best describes your personality?": ["Responsible and protective", "Optimistic and curious", "Loyal and dependable", "Playful and carefree"],
    "What's your favorite Disney song?": ["Let It Go from Frozen", "Circle of Life from The Lion King", "A Whole New World from Aladdin", "Part of Your World from The Little Mermaid"],
    "Which of these magical powers would you rather have?": ["Ice and snow powers like Elsa", "Invisibility like Jack Jack from The Incredibles", "Telekinesis like Violet from The Incredibles", "Super speed like Dash from The Incredibles"]
}

# Define a dictionary of possible results with their corresponding answers
results = {
    "Elsa": ["Building a snowman", "Ice and snow powers like Elsa"],
    "Anna": ["Optimistic and curious like Anna", "Let It Go from Frozen"],
    "Olaf": ["Playful and carefree like Olaf", "Drinking hot cocoa"],
    "Kristoff": ["Loyal and dependable like Kristoff", "Telekinesis like Violet from The Incredibles"],
}

# Define a while loop to ask the questions and get the user's answers
user_answers = []
for question, choices in questions.items():
    while True:

      # enumerate function to loop through the list of answer choices for that question (choices) and print each choice with its corresponding index number
      #index numbers start at 1 instead of 0 for readability purposes, so that the user can more easily choose an answer by typing in its corresponding number. The f-string includes the index number and the choice text separated by a period and a space.
        print(question)
        for index, choice in enumerate(choices):
            print(f"{index+1}. {choice}")
        try:
            user_answer = int(input())
            if user_answer < 1 or user_answer > len(choices):
                raise ValueError()
            user_answers.append(choices[user_answer-1])
            break
        except ValueError:
            print("Please enter a valid number.")

# Define a function to determine the user's result based on their answers
def determine_result(user_answers):
    match_counts = {result: 0 for result in results}
    for result, answers in results.items():
        for answer in user_answers:
            if answer in answers:
                match_counts[result] += 1
    max_count = max(match_counts.values())
    possible_results = [result for result, count in match_counts.items() if count == max_count]
    return possible_results

# Determine the user's result and print it out
possible_results = determine_result(user_answers)
if len(possible_results) == 0:
    print("Sorry, we couldn't determine your result.")
else:
    result = random.choice(possible_results)
    print(f"You are most like {result} from Frozen!")
