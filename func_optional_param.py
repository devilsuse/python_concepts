def display(message, value=None):
    if(value!=None):
        print(message + value);
    else:
        print(message + " without value");


display("this is message...")
display("this is message...", str(333))
# print(1+"s") gives error


