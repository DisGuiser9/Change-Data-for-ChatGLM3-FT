import os
import json

def transfer():
    #Change directory to your dataset directory
    directory = 'the root to your dataset directory'
    filenames = os.listdir(directory)

    #Automatically load JSON files
    json_files = [filename for filename in filenames if filename.endswith(".json")]
    if json_files is None:
        raise IndexError
    new_data = []
    for json_file in json_files:
        json_file_path = os.path.join(directory, json_file)
        try:
            with open(json_file_path, 'r',encoding='utf-8') as f:
                data = json.load(f)

            for item in data:
                if 'instruction' in item and 'output' in item:
                # Create a new dictionary 
                    conversation = {"conversations": [
                    {"role": "user", "content": item['instruction']},
                    {"role": "assistant", "content": item['output']}
                    ]}
                    new_data.append(conversation)
                else:
                    print(f"Key not found, skipping item.")
                    continue

            with open('new_' + str(json_file), 'w', encoding='utf-8') as f:
                # dump the file, set indent with 4, ensure_ascii=False to avoid error
                json.dump(new_data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error processing {json_file}: {e}")

if __name__ == '__main__':
    transfer()