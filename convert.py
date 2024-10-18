import json

# Step 1: Open the JSON file and process each line separately
with open('training_data/combined_dataset.json', 'r') as file:
    data = []
    for line in file:
        data.append(json.loads(line))  # Load each JSON object line by line

# Step 2: Now 'data' contains a list of all your JSON objects
# print(data)
QA_input = data
with open('/media/nevy11/myHardDisk/work/MentalDiaryApp/mentalHealthdiaryAI/output_file.json', 'w') as file:
    # Step 2: Save the Python dictionary/list back to the file as JSON
    json.dump(data, file, indent=4)  # 'indent=4' makes the JSON file easier to read

print("Data saved successfully!")