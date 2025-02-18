import os

from flask import Flask, send_from_directory

SITE_HTML = """
<head>
    <title>Is Trump still president?</title>
    <link rel="icon" type="image/x-icon" href="/static/favicon.ico">
</head>
<body style="background-color:black">
    <div style="text-align:center; padding-top:150px;">
        <img src="/static/captain.jpg"/>
    </div>
</body>
"""
app = Flask(__name__)


@app.route("/")
def home():

    return SITE_HTML


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


if __name__ == "__main__":
    app.run(debug=True)
