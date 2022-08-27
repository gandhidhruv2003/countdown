try:
    def countdown():
        import time
        user = int(input("Enter the time you want to start the countdown in seconds: "))
        userMessage = input("Enter the message you wish to print after the end of the countdown: ")
    
        for sec in range(user,0,-1):
            print(sec)
            time.sleep(1)
    
        print(userMessage)
    
    countdown()
except ValueError:
    print("Enter a number!")
except:
    print("Enter correctly")