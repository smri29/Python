from questionClass import Question
question_prompt = [
    "What color are Apples?\n(a) Red/Green\n(b) Magenta\n(c) Orange\nAnswer: ",
    "What color are Bananas?\n(a) Yellow\n(b) Purple\n(c) Orange\nAnswer: ",
    "What color are Strawberries?\n(a) Pink\n(b) Blue\n(c) Red\nAnswer: ",
]

questions = [
    Question (question_prompt[0],"a"),
    Question (question_prompt[1],"a"),
    Question (question_prompt[2],"c"),
]

def run_test (qustion):
    score = 0
    for qustion in questions:
        answer = input(qustion.propmt)
        if answer == qustion.answer:
            score+=1
    if score >= len(questions)/2:
        print("Congratulations! You got " + str(score) + "/" + str(len(questions)))
    else:
        print("Need to improve! You got " + str(score) + "/" + str(len(questions)))

run_test(questions)
