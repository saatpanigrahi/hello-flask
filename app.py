from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

# Digit-to-letter dictionary
digit_to_char = {
    '0': 'A',
    '1': 'B',
    '2': 'C',
    '3': 'D',
    '4': 'E',
    '5': 'F',
    '6': 'G',
    '7': 'H',
    '8': 'I',
    '9': 'J'
}

def encode_time(dt: datetime) -> str:
    raw_digits = dt.strftime("%Y%m%d%H%M%S")
    return ''.join(digit_to_char[d] for d in raw_digits)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Access Code</title>
    <style>
        body {
            font-family: monospace;
            padding: 2em;
            text-align: center;
        }
        .code-line {
            display: inline-flex;
            align-items: center;
            font-size: 2em;
            gap: 0.5em;
            color: #333;
        }
        .code-box {
            padding: 0.2em 0.6em;
            border: 1px solid #ccc;
            border-radius: 6px;
            background: #f0f0f0;
        }
    </style>
</head>
<body>
    <div class="code-line">
        <span>Code:</span>
        <div class="code-box">{{ code }}</div>
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    now = datetime.utcnow()
    code = encode_time(now)
    return render_template_string(HTML_TEMPLATE, code=code)

if __name__ == "__main__":
    app.run(debug=True)
