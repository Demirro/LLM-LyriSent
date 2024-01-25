from flask import Flask, render_template
import os
import json

app = Flask(__name__)


def get_json_content(folder_path):
    json_content = {}
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".json"):
                file_path = os.path.join(root, filename)
                with open(file_path, 'r') as file:
                    # Use relative path as key
                    relative_path = os.path.relpath(file_path, folder_path)
                    json_content[relative_path] = json.load(file)
    return json_content


@app.route('/')
def index():
    project_folder = 'C:/Users/Theo/PycharmProjects/LLM-LyriSent'  # Change this to the path of your project folder
    json_content = get_json_content(project_folder)
    return render_template('index.html', json_content=json_content)


app.run(debug=True)