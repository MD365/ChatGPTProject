from flask import Flask, request
import openai

app = Flask(__name__)
openai.api_key = "your_openai_api_key"


@app.route("/")
def index():
    return "Hello World!"


@app.route("/openai", methods=["POST"])
def openai_text_completion():
    prompt = request.form.get("prompt")
    model = request.form.get("model")
    completions = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message


if __name__ == "__main__":
    app.run()
