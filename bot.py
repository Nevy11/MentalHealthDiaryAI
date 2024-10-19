from transformers import pipeline
from qa_input import QA_input as QAI  # Assuming both 'qa_input' and 'QA_input' are similar

# Initialize the QA model pipeline
model_name = 'deepset/roberta-base-squad2'
qa = pipeline('question-answering', model=model_name, tokenizer=model_name)

def find_answer(question, qa_input_list, qa_pipeline):
    # Loop through the input list and check for context match
    for index, qa_item in enumerate(qa_input_list):
        if qa_item['Context'] == question or qa_item['Context'] == question + "?" or qa_item['Context'] == question + ".":
            answer = qa_pipeline(question, qa_item['Response'])['answer']
            if len(answer) < 3:
                continue
            return answer
    return None

# Main loop to handle questions
while True:
    question_asked = input("Question: ").strip()
    
    if question_asked.lower() in ["quit", "\\q"]:
        break
    elif question_asked.lower() == "help":
        print("Commands:\nhelp => display help\nquit or \\q => quit the loop")
        continue

    # First, try finding an answer in the primary QA_input
    answer = find_answer(question_asked, QAI, qa)
    
    if answer is None:  # If no answer found, try lowercase matching
        answer = find_answer(question_asked.lower(), QAI, qa)
    
    if answer is None:  # Fallback if no matches found
        print("No matching context found. Trying a generic response...")
        answer = qa(QAI[0]['Context'], QAI[0]['Response'])['answer']
    
    print("Answer:", answer)
