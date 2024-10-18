from transformers import pipeline
from qa_input import QA_input

model_name = "deepset/roberta-base-uncased"
qa = pipeline("question-answering", model=model_name, tokenizer=model_name)



QA_input = QA_input
while True:
    question_asked = input("Question: ")
    if question_asked == "quit" or question_asked == "\q":
        break
    if question_asked == "help":
        help_words = "help => display's the help contents\nquit or \q => breaks the loops and stops"
        print(help_words)
    count = 0
    for index in QA_input:
        if index['question'] == question_asked:
            answer = qa(question_asked.lower(), QA_input[count]['context'])
            print(answer['answer'])
        count +=1