"""Basic calendar for interaction with the cmd"""

from time import sleep,strftime 

FIRST_NAME = "Tom"

calendar = {}

def welcome():
 print "Welcome " + FIRST_NAME
 print "Calendar opening..."
 sleep(1)
 print strftime("%A %d %Y")
 print strftime("%H" + ":" + "%M" + ":" + "%S") 
 sleep(1)
 print "What would you like to do?"
  
def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input("A to Add, U to Update, V to View, D to Delete, X to Exit:")
    user_choice = user_choice.upper()
    if user_choice == "V":
      if len(calendar.keys()) < 1:
        print "Your calendar is empty"
      else:
        print calendar
    elif user_choice =="U":
     date = raw_input("What date?")
     update = raw_input("Enter the update: ")
     calendar[date] = update
     print "Update Successful"
     print calendar
    elif user_choice =="A":
     event = raw_input("Enter event:")
     date = raw_input("Enter date (MM/DD/YYYY):")
     if len(date)>10 or int(date[6:9]) > int(strftime("%Y")):
       print "Invalid date entered"
       try_again = raw_input("Try Again? Y for Yes, N for No: ")
       try_again = try_again.upper()
       if try_again =="Y":
         continue
       else:
         start = False
     else:
       calendar[date] = event
       print "Event successfully added"
    elif user_choice =="D":
      if len(calendar.keys()) < 1:
        print "Your calendar is empty"
      else:
        event = raw_input("What event?")
        for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print "Event deleted"
            print calendar
          else:
            print "That event does not exist"
    elif user_choice =="X":
      start = False
    else:
      print "Invalid entry"
      start = False
          
start_calendar()  
