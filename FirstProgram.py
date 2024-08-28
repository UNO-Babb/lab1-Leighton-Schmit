#FirstProgram.py
#Name:
#Date:
#Assignment:

def main():
  print("First Program")
  #Say hello
  print ("Hello")
  #Ask for the user's name
  print ("What is your name?")
  #Use the user's name in the program.
  name = input("What is your name?: ")
  print(name)
  #Ask the user for their age.
  print ("How old are you?")
  age = input("How old are you?: ")
  print(age)
  #Tell the user what year they were born in.
  age = int(age)
  born=(2024-(age))
  print ("you were born in",born)
  #Assume that they have not had their birthday yet this year.


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
