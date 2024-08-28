#MadLib.py
#Name:
#Date:
#Assignment:

def main():
  print("Madlib")
  #Ask user for words
  noun1 = input ("Enter a noun:")
  name1 = input ("Enter a name!:")
  noun2 = input("Enter second noun:")
  adjective1 = input("Enter an adjective:")
  verb1 = input ("Enter a verb:")
  adjective2 = input ("Enter another adjective:")
  name2 = input ("Enter another name:")
  verb2 = input ("Enter another verb:")
  #Print the story with the user supplied words.
  print ("Once upon a time, there was a knight, sir", (name2) )
  print ("The knight was on the run because he" + (verb2) + (name1) + "in the face")
  print ((name2) + "fled to the distasteful place of" + (noun1) + "and said it was quite" + (adjective2))
  print ((name1) + "Followed the knight, and found out what the knights most precious item was, a " +(noun2))
  print ("sir" + (name2) + "loved this eel because it was quite " + (adjective1))
  print ("sir" + (name2) + "then " + (verb2) + (name1) + "and " + (verb1) + "his " +(noun2) + "and ran away again")
#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
