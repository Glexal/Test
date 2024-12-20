# took way to long....... i had to make a game this is what i came up with 
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
first=input("you can hunt down the treasure or go back home. do you chose to hunt or go home? hunt or go home")
if first=="hunt":
    second=input('you picked the right one....... you see a big lake do you wait and hope that a boat can give you as ride or do you swim? wait or swim? ')
    if second=='wait':
        third=input('you wait and wait but nothing happens... you fall asleep and find yourself on a boat but dont know who took you. do you try and snek out or do you wait to find out what happens? snek or wait')
        if third=='wait':
            fourth=input('you wait and hope for the best until you see them throw someone overboard but its to late as you are next they throw you over for you to realize that it was an illusion and you have to pick between three doors. the first red the second yellow and the third blue. which do you pick? red, yellow, or blue')
            if fourth == 'red':
                print('you found the treasure!!!!!!!! now you have to find you way back home(the next part is coming out soon')
            else: fourth == 'blue' or 'yellow'
            print('you came so far many failed but you were the chosen one... unfortunately they were wrong you fell for greed and fear and didnt win')

        elif third == 'snek':
            print('you end up sneaking off and swimming away but the water is to much for you to swim as you realize that you dont know how to swim you are never to be seen again')
    elif second=='swim':
        print('you try and swim but not even half way there you end up being taken by the water enver to be seen again')
elif first=='go home':
    print('you go home and live out the rest of your days thinking about what could have been if you went on that hunt')
else:"please type only what is given and how it is show otherwise it will not work"