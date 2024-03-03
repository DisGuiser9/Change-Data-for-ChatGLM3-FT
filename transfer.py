import os
import json

def transfer():
    # Change directory to your dataset directory
    directory = 'root'
    filenames = os.listdir(directory)

    # Automatically load JSON files
    json_files = [filename for filename in filenames if filename.endswith(".json")]
    if not json_files:
        raise IndexError

    # Prepare a new_data list to hold all conversations
    new_data = []

    for json_file in json_files:
        json_file_path = os.path.join(directory, json_file)
        try:
            with open(json_file_path, 'r',encoding='utf-8') as f:
                data = json.load(f)
            
            for item in data:
                if 'instruction' in item and 'output' in item:
                    # Append user and assistant's speech to the conversation
                    conversation = {"conversations": [
                        {"role": "user", "content": item['instruction']},
                        {"role": "assistant", "content": item['output']}
                    ]}
                    new_data.append(conversation)
                else:
                    print(f"Key not found, skipping item.")
                    continue
        except Exception as e:
            print(f"Error processing {json_file}: {e}")

    # Write all conversations into one file "train.json"
    with open('train.json', 'w', encoding='utf-8') as f:
        # dump the file, set indent with 4, ensure_ascii=False to avoid error
        json.dump(new_data, f, ensure_ascii=False, indent=4)
        f.write('\n')

if __name__ == "__main__":
    transfer()