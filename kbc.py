from questions import QUESTIONS
import random

def isAnswerCorrect(question, answer):

    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''
    return question["answer"] == answer 


def lifeLinefun(ques,i):

    '''
    :param ques: The question for which the lifeline is asked for. (Type JSON)
    :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    '''
    a = ques["answer"]
    b = ques["answer"]
    while a == ques["answer"]:
        a = random.randint(1,4)
    while b == ques["answer"] or b == a : 
        b = random.randint(1,4)
    print(f'\tQuestion {i+1}: {ques["name"]}' )
    print(f'\t\tOptions:')
    for x in range(1,5):
        if a != x and b != x : 
            if x==1:
                print(f'\t\t\tOption {x}: {QUESTIONS[i]["option1"]}')
            elif x==2:
                print(f'\t\t\tOption {x}: {QUESTIONS[i]["option2"]}')
            elif x==3:
                print(f'\t\t\tOption {x}: {QUESTIONS[i]["option3"]}')
            elif x==4:
                print(f'\t\t\tOption {x}: {QUESTIONS[i]["option4"]}')
    ans = input('Your choice from give option : ')
    return ans 




def kbc():
    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''
    i = 0
    lifeLine = 0
    quit = False
    winning_prize = 0
    lost = 0
    current_amount = 0
    minimum_winnig_prize = 0
    print("\nINSTRUCTION\n")
    print("For using Lifeline use 5.\nfor Quiting the game use q character .")
    print("You cannot able to use Lifeline if you are in last Question although you have not used your lifeline till last Question.\n")
    while i < 15 and not quit and not lost :

        #  Display a welcome message only once to the user at the start of the game.
        #  For each question, display the prize won until now and available life line.
        # For now, the below code works for only one question without LIFE-LINE and QUIT checks

        print(f'\tQuestion {i+1}: {QUESTIONS[i]["name"]}' )
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[i]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[i]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[i]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[i]["option4"]}')
        ans = input('Your choice ( 1-4 ) : ')

        # check for the input validations
        if ans == "q":
            quit = True
            continue 

        if int(ans) == 5 :
            if lifeLine == 0 and i != 14 :
                lifeLine = 1
                ans = lifeLinefun(QUESTIONS[i],i)
            else :
                print("You already used the life line.")
                continue 
        
        
        if isAnswerCorrect(QUESTIONS[i], int(ans) ):
            # print the total money won.
            # See if the user has crossed a level, print that if yes
            current_amount = QUESTIONS[i]["money"]
            print('\nCorrect !')
            if i == 4 : 
                minimum_winnig_prize = int(QUESTIONS[i]["money"]) 
            elif i == 10 : 
                minimum_winnig_prize = int(QUESTIONS[i]["money"]) 
            print( "current price = {} \nminimum winnig price = {} ".format(QUESTIONS[i]["money"],minimum_winnig_prize))

        else:
            # end the game now.
            # also print the correct answer
            print('\nIncorrect !')
            lost = 1
        i += 1 
    if lost : 
        print("Congratualation You Won {}".format(minimum_winnig_prize))
    elif quit : 
        print("Congratualation You Won {}".format(current_amount))
    else:
        print("You Become Crorepati {}".format(current_amount))
    # print the total money won in the end.


kbc()
