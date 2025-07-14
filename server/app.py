from flask import Flask, request, jsonify
import requests
import random

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.json
    form_url = data.get("formUrl")
    choices = data.get("choices")  # e.g. {entry.123: {"A": 50, "B": 50}}
    times = int(data.get("times", 1))

    for _ in range(times):
        form_data = {}
        for entry_id, options in choices.items():
            options_list = []
            for option, percent in options.items():
                options_list += [option] * int(percent)
            selected = random.choice(options_list)
            form_data[entry_id] = selected
        try:
            requests.post(form_url, data=form_data)
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    return jsonify({"status": f"{times} submissions sent."})

if __name__ == '__main__':
    app.run()
