from flask import Flask, render_template_string, request, redirect
import requests
import os

app = Flask(__name__)

BACKEND_URL = os.environ.get("BACKEND_URL", "http://127.0.0.1:8000")

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Calendar Picker</title>
</head>
<body>
    <h2>Calendar Picker</h2>
    <form method="post" action="/select_date">
        <input type="date" name="selected_date" required>
        <button type="submit">Select Date</button>
    </form>

    {% if date %}
        <h3>Selected Date: {{ date }}</h3>
    {% endif %}
</body>
</html>
"""

def get_current_date():
    try:
        response = requests.get(f"{BACKEND_URL}/get_date")
        return response.json().get("selected_date")
    except:
        return None

@app.route("/", methods=["GET"])
def home():
    return render_template_string(HTML_TEMPLATE, date=get_current_date())

@app.route("/select_date", methods=["POST"])
def select_date():
    date_selected = request.form.get("selected_date")
    try:
        requests.post(f"{BACKEND_URL}/set_date/{date_selected}")
    except:
        pass
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
