from transformers import pipeline
from qa_input import QA_input

model_name = "deepset/roberta-base-uncased"
qa = pipeline("question-answering", model=model_name, tokenizer=model_name)

while True:
    question_asked = input("Question: ").lower()
    if question_asked == "quit" or question_asked == "\q":
        break
    if question_asked == "help":
        help_words = "help => display's the help contents\nquit or \q => breaks the loops and stops"
        print(help_words)
    count = 0
    for index in QA_input:
        if index['question'] == question_asked:
            answer = qa(question_asked, QA_input[count]['context'])
            print(answer['answer'])
        else:
            answer_trial = qa(QA_input[0]['question'], QA_input[0]['context'])
            print(answer_trial['answer'])
            break
        count +=1
        