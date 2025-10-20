from flask import Flask, jsonify
import random

app = Flask(__name__)

# Some example quotes
quotes = [
    "The best way to predict the future is to invent it.",
    "Life is 10% what happens to us and 90% how we react to it.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Believe you can and you're halfway there.",
    "It does not matter how slowly you go as long as you do not stop."
]

@app.route('/quote', methods=['GET'])
def get_quote():
    # Return a random quote from the list
    quote = random.choice(quotes)
    return jsonify({"quote": quote})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
