import random
firstwords = True
robot = input('Would you like to turn me on? ON/OFF')
robot = robot.lower()
if robot =='on':
    while robot != 'off':
        if firstwords == True:
            robot = input('Hello, user, my name is 𝘿𝙖𝙣𝙖. I am an artificial \'intelligence\' that can respond to 🆅🅴🆁🆈 limited sentences. If you want to see other options, type "menu". Now, ask me something.')
            robot = robot.lower()
            firstwords = False
        if robot == 'menu':
            print('calculator')
            print('coinflip')
            print('rock paper scissors')
            print('guess the word')
            print('guess the letter')
            print('odd/even detector')
            print('number generator')
            robot = input('You can type one of the following and I will generate it. If you want to exit out of one the options, type "quit". Also, if you want to turn me off, you can NOT turn me off while on one of the option. If none of these interest you, type "close" to go back.')
            robot = robot.lower()
            if robot == 'close':
                ask = True
        if robot.find('what') != -1 and robot.find('your') != -1 and robot.find('name') != -1 and robot.find('creator') == -1:
            print('My name is Dana, my name is based on my creator\'s coding guru.')
            ask = True
        elif robot.find('what') != -1 and robot.find('your') != -1 and robot.find('creator') != -1 and robot.find('name') != -1:
            print('My creator\'s name is Chello, and he programmed me to tell you this.')
            ask = True
        elif robot.find('when') != -1 and robot.find('you') != -1 and robot.find('created') != -1:
            print('I was in production at July 7th 2023, and finished at July 11th 2023 I was created because the original Dana assigned my creator to make me.')
            ask = True
        elif robot.find('tell') != -1 and robot.find('me') != -1 and robot.find('fact') != -1:
            factlist = ['The only letter that doesn’t appear on the periodic table is J.', 'One habit of intelligent humans is being easily annoyed by people around them but saying nothing in order to avoid a meaningless argument.', 'If a Polar Bear and a Grizzly Bear mate, their offspring is called a “Pizzy Bear.”', 'In 2006, a Coca-Cola employee offered to sell Coca-Cola secrets to Pepsi. Pepsi responded by notifying Coca-Cola.', 'The ten highest mountain summits in the United States are all located in Alaska.', 'Nintendo trademarked the phrase “It’s on like Donkey Kong” in 2010.']
            ask = True
        elif robot == 'calculator':
                print('🅳🅰🅽🅰\'🆂 🅲🅰🅻🅲🆄🅻🅰🆃🅾🆁')
                print('1. Add')
                print('2. Subtract')
                print('3. Multiply')
                print('4. Divide')
                print('5. Quit')
                operator = int(input('Choose an operator you want to calculate with by typing their assigned number.'))
                while operator != 5:
                    activate_print = 1
                    while activate_print == 1:
                        activate_print = 0
                        print('By the way, if you want to quit, type the sequence of numbers: 99879')
                        no1 = int(input('Type in the first number..'))
                        if no1 == 99879:
                            ask = True
                        elif no1 != 99879:
                            no2 = int(input('..aaand, the second one.'))
                        if no2 == 99879:
                                ask = True
                        elif operator == 1:                   
                            answer = no1 + no2
                            print(answer)
                        elif operator == 2:
                            answer = no1 - no2
                            print(answer)
                        elif operator == 3:
                            answer = no1*no2
                            print(answer)
                        elif operator == 4:
                            answer = no1/no2
                            print(answer)
                        elif operator == 5:
                            ask = True
                        else:
                            print('Not an option, try again')
                            operator = int(input('Choose an operator you want to calculate with'))
                            activate_print = 1
                ask = True
        elif robot.find('you') != -1 and robot.find('have') != -1 and robot.find('favourite') != -1:
            print('I am a robot, I don\'t have favourites')
            ask = True
        elif robot == 'coinflip': 
            robot = input('Type "flip" to flip.')
            robot = robot.lower()
            while robot == 'flip' and robot != 'quit':
                print('Flipping coin..')
                coinlist = ['Heads', 'Tails']
                print(random.choice(coinlist))
                input('Flip again? (\'flip\')')
        elif robot == 'rock paper scissors':
            if rpsoption == 'no':
                while rpsreqrematch == 'yes' or robot == 'quit':
                    rpsreqrematch = 'no'
                    robot = input('Pick one.')
                    rps = ['🪨', '📄', '✂️']
                    rpsitem = random.choice(rps)
                    print(rpsitem)
                    robot = robot.lower()
                    if robot == 'rock':
                        if rpsitem == '📄':
                            print('Yay! Looks like I won.')
                        if rpsitem == '✂️':
                            print('Darn.. Looks like I lost')
                        if rpsitem == '🪨':
                            robot = input('Wow! Looks like we tied. Rematch!')
                            rpsreqrematch = 'yes'
                    elif robot == 'paper':
                        if rpsitem == '📄':
                            robot = input('Wow! Looks like we tied. Rematch!')
                            reqrematch = 'yes'
                        if rpsitem == '✂️':
                            print('Yay! Looks like I won.')
                        if rpsitem == '🪨':
                            print('Darn.. Looks like I lost.')
                    elif robot == '✂️':
                        if rpsitem == '🪨':
                            print('Yay! Looks like I won.')
                        if rpsitem == '📄':
                            print('Darn.. Looks like I lost.')
                        if rpsitem == '✂️':
                            robot = input('Wow! Looks like we tied. Rematch!')
                            rpsreqrematch = 'yes'
                    else:
                        robot = input('That is an illegal move, try again.')
                    rpsreqrematch = input('Rematch?(YES/NO)')
                    rpsreqrematch = rpsreqrematch.lower()     
            if rpsoption == 'yes':
                rpspointgoal = int(input('How much points are we aiming for?'))
                while danarpspoints != rpspointgoal and yourrpspoints != rpspointgoal and rpsreqrematch == 'yes':
                    if rpsreqrematch == 'yes':
                        robot = input('Pick one.')
                        rps = ['🪨', '📄', '✂️']
                        rpsitem = random.choice(rps)
                        print(rpsitem)
                        robot = robot.lower()
                        rpsreqrematch = 'no'
                        if robot == 'rock':
                            if rpsitem == '📄':
                                danarpspoints += 1
                                print('👦', yourrpspoints, '-', danarpspoints, '🤖')
                                rpsreqrematch = 'yes'
                            if rpsitem == '✂️':
                                yourrpspoints += 1
                                print('👦',  yourrpspoints, '-', danarpspoints, '🤖')
                                rpsreqrematch = 'yes'
                            if rpsitem == '🪨':
                                print('Wow! Looks like we tied. Redo!')
                                rpsreqrematch = 'yes'
                        elif robot == 'paper':
                            if rpsitem == '📄':
                                print('Wow! Looks like we tied. Redo!')
                                rpsreqrematch = 'yes'
                            if rpsitem == '✂️':
                                danarpspoints += 1
                                print('👦',  yourrpspoints, '-', danarpspoints, '🤖')
                                rpsreqrematch = 'yes'
                            if rpsitem == '🪨':
                                yourrpspoints += 1
                                print('👦',  yourrpspoints, '-', danarpspoints, '🤖')
                                rpsreqrematch = 'yes'
                        elif robot == 'scissors':
                            if rpsitem == '🪨':
                                danarpspoints += 1
                                print('👦',  yourrpspoints, '-', danarpspoints, '🤖')
                                rpsreqrematch = 'yes'
                            if rpsitem == '📄':
                                yourrpspoints += 1
                                print('👦',  yourrpspoints, '-', danarpspoints, '🤖')
                                rpsreqrematch = 'yes'
                            if rpsitem == '✂️':
                                print('Wow! Looks like we tied. Redo!')
                                rpsreqrematch = 'yes'
                        else:
                            print('That is an illegal move, try again.')
                            rpsreqrematch = 'yes'
                        robot = robot.lower()
                if rpspointgoal == danarpspoints or rpspointgoal == yourrpspoints:
                    if danarpspoints > yourrpspoints:
                        print('Yay! Looks like I win.')
                    if yourrpspoints > danarpspoints:
                        print('Darn.. Looks like I lost.')
                rpsreqrematch = input('Rematch?(YES/NO)')
                rpsreqrematch = rpsreqrematch.lower()
            if rpsoption == 'quit':
                robot = input('Anything else?')
                robot = robot.lower()
        elif robot == 'guess the word':
            getletter = False
            letteramt = 0
            hint = ['_', '_','_','_','_']
            order = 0
            themestr = ['fruits', 'furniture', 'school', 'animal', 'tech']
            fruits = ['apple', 'peach', 'dates', 'grape', 'lemon', 'mango', 'olive', 'melon']
            furniture = ['chair', 'table', 'doors', 'shelf']
            school = ['books', 'class', 'teach', 'pupil', 'maths', ]
            animal = ['snake', 'gator', 'lions', 'tiger', 'liger', 'human', 'birds']
            tech = ['phone', 'robot', 'mouse', 'cable']
            theme = [fruits, furniture, school, animal, tech]
            chosentheme = random.choice(theme)
            word = random.choice(chosentheme)
            print(word)
            if chosentheme == fruits:
                themestr = 'FRUITS'
            elif chosentheme == furniture:
                themestr = 'FURNITURE'
            elif chosentheme == school:
                themestr = 'SCHOOL'
            elif chosentheme == animal:
                themestr = 'ANIMAL'
            elif chosentheme == tech:
                themestr = 'TECH'
            print('Theme:', themestr)
            wordguess = input('Guess the 5 letter word!')
            wordguess = wordguess.lower()
            while wordguess != word:
                for i in range(5):
                    if wordguess[order] == word[order]:
                        hint[i] = (word[order])
                        letteramt += 1
                        getletter = True
                    order += 1
                if getletter == True:
                    print('Nice! You guessed', letteramt, 'letters correctly!')
                    print(''.join(hint))
                    getletter = False
                wordguess = input('Keep guessing!')
                wordguess = wordguess.lower()
                order = 0
                letteramt = 0
            if wordguess == word:
                print('Great job!! You guessed the word')
                ask = True
        elif robot == 'odd/even detector':
            redo = 'yes'
            while number != 99879 and redo != 'no':
                if redo == 'yes':
                    number = int(input('Type a number. (type 99879 if you want to quit)'))
                    if number%2 == 0:
                        print('Your number is even.')
                    else:
                        print('Your number is odd.')
                    redo = input('Try again? (YES/NO)')
                    redo = redo.lower()
                elif redo == 'no':
                    ask = True
                else:
                    redo = input('No 𝕖𝕟𝕥𝕚𝕖𝕟𝕕𝕠..')
        elif robot == 'guess the number':
            number = random.randint(1, 100)
            hint = int(input('Guess the number! (1-100)'))
            while hint != number:
                while hint <= 0 or hint > 100:
                    hint = int(input('Remember, it is from 1 to 100..'))
                if hint > number:
                    hint = int(input('Lower..'))
                if hint < number:
                    hint = int(input('Higher..'))
            while hint == number:
                print('You guessed it!')
                again = input('Play again?! (yes/no)')
                number = random.randint(1, 100)
                if again == 'yes':
                    hint = int(input('Guess the number! (1-100)'))
                elif again == 'no':
                    print('Alright, good game!')
                    ask = True
                else:
                    print('Sorry, I do not understand')
        elif robot == 'number generator':
            numbergenerator_conditions = True
            print('𝕿𝖍𝖊 𝕲𝖗𝖊𝖆𝖙 𝕹𝖚𝖒𝖇𝖊𝖗 𝕲𝖊𝖓𝖊𝖗𝖆𝖙𝖔𝖗\n(as always, (if you experieced OTHER number related options), type the set of number 99879 to exit)')
            number_regenerate = True
            while number_regenerate == True:
                if numbergenerator_conditions == True or numbergenerator_redo == 'conditions':
                    minimum = int(input('Enter the MINIMUM number.')) 
                    if minimum != 99879:
                        maximum = int(input('Enter the MAXIMUM number.'))
                        if maximum != 99879:
                            roll = input('Type \"roll\" to roll.')
                            roll = roll.lower()
                            if roll == 'roll' or numbergenerator_redo == 'reroll':
                                print(random.randint(minimum, maximum+1))
                                numbergenerator_redo = True
                            elif roll == 'quit':
                                ask = True
                                number_regenerate = False
                            else:
                                print('Never told you to write that, if you want to exit this option, type \"quit\"')
                                roll = input('Type \"roll\" to roll.')
                            if numbergenerator_redo != False:
                                numbergenerator_redo = input('Options; if you want to reroll, type \"reroll\", if you want to create a new set of conditions, type\"conditions\", if you want to exit, type \"quit\"')
                                numbergenerator_redo = numbergenerator_redo.lower()
                                while numbergenerator_redo == 'reroll':
                                    roll = input('Type \"roll\" to roll.')
                                    roll = roll.lower()
                                    if roll == 'roll' or numbergenerator_redo == 'reroll':
                                        print(random.randint(minimum, maximum+1))
                                        numbergenerator_redo = True
                                    elif roll == 'quit':
                                        ask = True
                                        number_regenerate = False
                                    else:
                                        print('Never told you to write that, if you want to exit this option, type \"quit\"')
                                        roll = input('Type \"roll\" to roll.')
                                        numbergenerator_conditions = False
                                        print(numbergenerator_conditions)
                                        if numbergenerator_conditions == 'quit':
                                            ask = True
                                            number_regenerate = False
                                    if numbergenerator_redo != False:
                                        numbergenerator_redo = input('Options; if you want to reroll, type \"reroll\", if you want to create a new set of conditions, type\"conditions\", if you want to exit, type \"quit\"')
                                        numbergenerator_redo = numbergenerator_redo.lower()
                        else:
                            ask = True
                            number_regenerate = False
                    else:
                        ask = True
                        number_regenerate = False
        else:
            print('wI\'m sorry, I didn\'t quite understand you. Please write your sentence in a form where I can understand it')
            ask = True
        if ask == True:
            robot = input('Anything else?')
elif robot == 'off':
    print('😴😴😴')
else:
    print('Taking that as \"off\".')
