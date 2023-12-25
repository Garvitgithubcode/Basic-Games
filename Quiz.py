# Quiz like KBC

import time
import random
easy1=["""Question 1:
What is the capital city of France?
A) London
B) Paris
C) Rome
D) Berlin

""","""
Question 1:
Which planet is known as the Red Planet?
A) Venus
B) Mars
C) Jupiter
D) Saturn

""","""
Question 1:
What is the chemical symbol for water?
A) H2O
B) CO2
C) O2
D) CH4

"""]
easy2=["""Question 2:
Which famous scientist developed the theory of relativity?
A) Isaac Newton
B) Albert Einstein
C) Marie Curie
D) Galileo Galilei

""","""
Question 2:
What is the largest mammal in the world?
A) Elephant
B) Blue Whale
C) Giraffe
D) Gorilla

""","""
Question 2:
Which planet is closest to the Sun?
A) Mercury
B) Venus
C) Earth
D) Mars

"""]
easy3=["""Question 3:
What is the capital of Japan?
A) Beijing
B) Tokyo
C) Seoul
D) Bangkok

""","""
Question 3:
Which gas do plants absorb from the atmosphere and release oxygen?
A) Carbon Dioxide
B) Oxygen
C) Nitrogen
D) Hydrogen

""","""
Question 3:
What is the chemical symbol for gold?
A) Au
B) Ag
C) Fe
D) Hg

"""]
easy4=["""
Question 4:
Who painted the Mona Lisa?
A) Vincent van Gogh
B) Leonardo da Vinci
C) Pablo Picasso
D) Michelangelo

""","""
Question 4 (Easy):
What is the capital city of India?
A) Mumbai
B) New Delhi
C) Kolkata
D) Chennai

""","""
Question 4 (Easy-Medium):
Who wrote the play "Romeo and Juliet"?
A) William Shakespeare
B) Jane Austen
C) Charles Dickens
D) Leo Tolstoy

"""]

medium1=["""Question 5:
What is the currency of Japan?
A) Yen
B) Won
C) Ringgit
D) Baht

""","""
Question 5:
Who wrote the play "Romeo and Juliet"?
A) William Shakespeare
B) Jane Austen
C) Charles Dickens
D) Mark Twain

""","""
Question 5:
Which gas do plants absorb to perform photosynthesis?
A) Carbon Dioxide
B) Oxygen
C) Nitrogen
D) Hydrogen

"""]
medium2=["""Question 6:
Which planet is known as the "Morning Star" or the "Evening Star"?
A) Mercury
B) Venus
C) Mars
D) Jupiter

""","""
Question 6:
In which year did Christopher Columbus first reach the Americas?
A) 1492
B) 1501
C) 1520
D) 1545

""","""
Question 6:
What is the chemical symbol for the element Gold?
A) Au
B) Ag
C) Fe
D) Hg

"""]
medium3=["""Question 7:
Who painted the famous artwork "Starry Night"?
A) Vincent van Gogh
B) Pablo Picasso
C) Leonardo da Vinci
D) Claude Monet

""","""
Question 7:
Which planet is known as the "Red Planet"?
A) Venus
B) Mars
C) Jupiter
D) Saturn

""","""
Question 7:
What is the largest organ in the human body?
A) Liver
B) Heart
C) Skin
D) Lungs

"""]
medium4=["""Question 8:
Which scientist developed the theory of general relativity?
A) Isaac Newton
B) Albert Einstein
C) Marie Curie
D) Galileo Galilei

""","""
Question 8 (Medium):
Which planet is known as the "Red Planet"?
A) Mars
B) Jupiter
C) Venus
D) Saturn

""","""
Question 8 (Medium-Hard):
Who painted the famous artwork "Starry Night"?
A) Vincent van Gogh
B) Pablo Picasso
C) Leonardo da Vinci
D) Michelangelo

"""]
print(f"welcome to our KBC Quiz".center(50))
name=input("Enter your name: ")

print(f"Hey {name} ")
option=input("There are 8 questions in this quiz, Are you ready to play this quiz\n (Yes/No)")
games = 0
your_score = 0
if option == "yes":
  print("Great lets play")
  while True:
    a = random.choice(easy1)
    time.sleep(1)
    print("\nThis Question Worth Rs.10000")

    print(a)
    ans1 = input("Type your answer(In small letters): ")
    if ans1 == "paris" or ans1 == "mars" or ans1 == "h2o":
      ab="Correct answer"
      print(ab)
      print("You win 10000")
      your_score += 1
      if ab == "Correct answer":
          rs1 = 10000
    else:
      print("Incorrect answer")
      rs1=0

    
    b = random.choice(easy2)
    time.sleep(2)
    print("\nThis Question Worth Rs.20000")

    print(b)
    ans2 = input("Type your answer(In small letters): ")
    if ans2=="albert ainstein" or ans2=="blue whale" or ans2=="mercury":
      bc="Correct answer"
      print(bc)
      print("You win 20000")
      your_score += 1
      if bc == "Correct answer":
          rs2=20000
      
    else:
      print("Incorrect answer")
      rs2 = 0
    
    c = random.choice(easy3)
    time.sleep(2)
    print("\nThis Question Worth Rs.40000")

    print(c)
    ans3 = input("Type your answer(In small letters): ")
    if ans3 == "tokyo" or ans3 == "carbon dioxide" or ans3 == "au":
      cd="Correct answer"
      print(cd)
      print("You win 40000")
      your_score += 1
      if cd == "Correct answer":
          rs3=40000
    else:
      print("Incorrect answer")
      rs3 = 0


    d = random.choice(easy4)
    time.sleep(2)
    print("\nThis Question Worth Rs.80000")

    print(d)
    ans4 = input("Type your answer(In small letters): ")
    if ans4 == "leonardo da vinci" or ans4 == "new delhi" or ans4 == "william shakespeare":
      de="Correct answer"
      print(de)
      print("You win 80000")
      your_score += 1
      if de == "Correct answer":
          rs4=80000
      
    else:
      print("Incorrect answer")
      rs4 = 0


    e = random.choice(medium1)
    time.sleep(2)
    print("\nThis Question Worth Rs.160000")

    print(e)
    ans5 = input("Type your answer(In small letters): ")
    if ans5 == "yen" or ans5 == "william shakespeare" or ans5 == "carbon dioxide":
      ef="Correct answer"
      print(ef)
      print("You win 160000")
      your_score += 1
      if ef == "Correct answer":
          rs5=160000
    else:
      print("Incorrect answer")
      rs5 = 0


    f = random.choice(medium2)
    time.sleep(2)
    print("\nThis Question Worth Rs.320000")

    print(f)
    ans6 = input("Type your answer(In small letters): ")
    if ans6 == "venus" or ans6 == "1492" or ans6 == "au":
      fg="Correct answer"
      print(fg)
      print("You win 320000")
      your_score += 1
      if fg == "Correct answer":
          rs6=320000
    else:
      print("Incorrect answer")
      rs6 = 0

    g = random.choice(medium3)
    time.sleep(2)
    print("\nThis Question Worth Rs.640000")

    print(g)
    ans7 = input("Type your answer(In small letters): ")
    if ans7 == "vincent van gogh" or ans7 == "mars" or ans7 == "skin":
      gh="Correct answer"
      print(gh)
      print("You win 640000")
      your_score += 1
      if gh == "Correct answer":
          rs7=640000
    else:
      print("Incorrect answer")
      rs7 = 0

    h = random.choice(medium4)
    time.sleep(2)
    print("\nThis Question Worth Rs.1 crore")

    print(h)
    ans8 = input("Type your answer(In small letters): ")
    if ans8 == "albert einstein" or ans8 == "mars" or ans8 == "vincent van gogh":
      hi="Correct answer"
      print(hi)
      print("You win 1 crore")
      your_score += 1
      if hi == "Correct answer":
          rs8=10000000
    else:
      print("Incorrect answer")
      rs8 = 0
    
  print("Gmae Over".center(50))
  time.sleep(1)
  print(f"\nCongratulation {name} your score is",your_score,"out of",games)
  time.sleep(1)
  print("Your total reward you win in this quiz is",rs1+rs2+rs3+rs4+rs5+rs6+rs7+rs8)
  print("Thanks for playing\n Have fun")
elif option=="no":
  print("It's ok next time")
else:
  print("Invalid input \nplease enter (yes/no)")
