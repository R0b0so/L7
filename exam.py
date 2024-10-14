medical_cause = input("do you have a medical cause? (yes or no)")

attendance = int(input("what is your attendance? "))
if medical_cause == "yes":
    print("you can take the exam")
else:
    if attendance < 75:
        print("you can't take the exam")
    else: 
        print("you can take the exam")