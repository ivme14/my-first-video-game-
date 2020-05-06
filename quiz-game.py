import json, requests, random, html

url             = "https://opentdb.com/api.php?amount=1&category=15&difficulty=easy"
offline_message = "Sorry, there was a problem retreiving the question. Press enter to try again or type 'quit' to quit the game."
score_correct   = 0
score_incorrect = 0
score_total     = 0
score_average   = 0
endGame         = ""

while endGame != "quit":
    x = requests.get(url)
    if(r.status_code != 200):
        endGame = input(offline_message)
    else:
        valid_answer   = False
        answer_number  = 1
        data           = json.loads(r.text)
        category       = data['results'][0]['category']
        question       = data['results'][0]['question']
        answers        = data['results'][0]['incorrect_answers']
        correct_answer = data['results'][0]['correct_answer']
        answers.append(correct_answer)
        random.shuffle(answers)

        print("Category:\n{0}\n" .format(html.unescape(category)))
        print("{0}\n" .format(html.unescape(question)))

        for answer in answers:
            print("{0} - {1}" .format(answer_number,html.unescape(answer)))
            answer_number += 1

        while valid_answer == False:
            user_answer = input("\nType the number of the correct answer. ")
            try:
                user_answer = int(user_answer)
                if user_answer > len(answers) or user_answer <= 0:
                    print("Invalid answer")
                else:
                    valid_answer = True
            except:
                print("Invalid answer. Use only numbers.")

        user_answer = answers[int(user_answer)-1]

        if user_answer == correct_answer:
            print("\nCongratulations! You answered correctly! The correct answer was {0}" .format(html.unescape(correct_answer)))
            score_correct += 1
        else:
            print("Sorry, {1} is incorrect. The correct answer is: {0}" .format(html.unescape(correct_answer),html.unescape(user_answer)))
            score_incorrect += 1

        score_total    = score_correct + score_incorrect
        score_average  = round(((score_correct/score_total) * 100),2)

        print("\n##########################")
        print("--------Score---------")
        print(f"Correct answers: {score_correct}")
        print(f"Incorrect answers: {score_incorrect}")
        print(f"Your score is {score_correct} out of {score_total}, an average of {score_average}%")
        print("##########################")

        endGame = input("\nPress enter to play again or type 'quit' to quit the game.").lower()

print("\nThanks for playing")
