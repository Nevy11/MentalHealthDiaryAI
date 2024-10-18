from transformers import pipeline
from convert import QA_input
from qa_input import QA_input as QAI
import random

"""
the model_name roberta-base-squad2 model is what we are using
We'll use pipeline which is a much simpler way to generate output
loop over the queries
"""
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
    """
    loop over the QA_input that is from the changed output file.json
    in one loop, compare whether the context matches the question asked, if it matches, generates the answer using the qa model stored by the pipeline.
    Take in the question asked
    """
    for index in QA_input:
        # print(index)
        if index['Context'] == question_asked:
            answer = qa(question_asked, QA_input[count]['Response'])
            print(answer['answer'])
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
         count = 0
         for index in QAI:
            print(index)
            if index['Context'] == question_asked.lower():
                answer = qa(question_asked.lower(), QAI[count]['Response'])
                print(answer['answer'])
                found=True
                number_of_found_answers += 1
                answers_found.append(answer['answer'])
            count +=1
    if not found:
        count = 0
        for index in QAI:
            if index['Context'] == question_asked + "?":
                answer = qa(question_asked + "?", QAI[count]['Response'])
                print(answer['answer'])
                found=True
                number_of_found_answers += 1
                answers_found.append(answer['answer'])

            count +=1
            
    if not found:
            answer_trial = qa(QA_input[0]['Context'], QA_input[0]['Response'])
            print(answer_trial['answer'])
    if found:
            print("number_of_found_answers", number_of_found_answers)
            index = random.randrange(0, number_of_found_answers)
            print("answers_found: ", answers_found)
            print("Selecting: ", answers_found[index])
    