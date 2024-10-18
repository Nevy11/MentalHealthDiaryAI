from transformers import pipeline
from qa_input import QA_input 
import random

model_name = 'deepset/roberta-base-squad2'
qa = pipeline('question-answering', model=model_name, tokenizer=model_name)
while True:
    answers_found = []
    number_of_found_answers = 0
    question_asked = input("Question: ")
    found = False
    if question_asked == "quit" or question_asked == "\q":
        
        break
    if question_asked == "help":
        help_words = "help => display's the help contents\nquit or \q => breaks the loops and stops"
        print(help_words)
        found=True
    count = 0
    for index in QA_input:
        if index['Context'] == question_asked:
            answer = qa(question_asked, QA_input[count]['Response'])
            # print(answer['answer'])
            found=True
            number_of_found_answers += 1
            answers_found.append(answer['answer'])
        count +=1
    if not found:
        count = 0
        for index in QA_input:
            if index['Context'] == question_asked + "?":
                answer = qa(question_asked, QA_input[count]['Response'])
                # print(answer['answer'])
                found=True
                number_of_found_answers += 1
                answers_found.append(answer['answer'])

            count +=1
            
        if not found:
            answer_trial = qa(QA_input[0]['Context'], QA_input[0]['Response'])
            print(answer_trial['answer'])
        if found:
            index = random.randrange(0, number_of_found_answers+1)
            print("answers_found: ", answers_found)
            print("Selecting: ", answers_found[index])
    