from flask import Flask, render_template, request
from model import generate_caption  # Import the caption function
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def home():
    caption = ""
    image_url = ""

    if request.method == "POST":
        image_file = request.files["image"]
        if image_file:
            image_path = os.path.join(app.config["UPLOAD_FOLDER"], image_file.filename)
            image_file.save(image_path)
            caption = generate_caption(image_path)
            image_url = image_path  # Store image URL for display

    return render_template("index.html", caption=caption, image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True)
