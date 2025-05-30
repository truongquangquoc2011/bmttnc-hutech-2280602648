from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher



app = Flask(__name__)

# Router routes for home page
@app.route("/")
def home():
    return render_template('index.html')

# Router routes for caesar cipher
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# VIGENERE CIPHER
@app.route("/vigenere")
def vigenere():
    return render_template("vigenere.html")


@app.route("/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    text = request.form["inputPlainText"]
    key = request.form["inputKeyPlain"]
    cipher = VigenereCipher()
    encrypted = cipher.vigenere_encrypt(text, key)
    return f"text: {text}<br>key: {key}<br>encrypted: {encrypted}"

@app.route("/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    text = request.form["inputCipherText"]
    key = request.form["inputKeyCipher"]
    cipher = VigenereCipher()
    decrypted = cipher.vigenere_decrypt(text, key)
    return f"text: {text}<br>key: {key}<br>decrypted: {decrypted}"

# RAILFENCE CIPHER
@app.route("/railfence")
def railfence():
    return render_template("railfence.html")
@app.route("/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    text = request.form["inputPlainText"]
    key = int(request.form["inputKeyPlain"])
    cipher = RailFenceCipher()
    encrypted = cipher.rail_fence_encrypt(text, key)
    return f"text: {text}<br>key: {key}<br>encrypted: {encrypted}"
@app.route("/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    text = request.form["inputCipherText"]
    key = int(request.form["inputKeyCipher"])
    cipher = RailFenceCipher()
    decrypted = cipher.rail_fence_decrypt(text, key)
    return f"text: {text}<br>key: {key}<br>decrypted: {decrypted}"

# PLAYFAIR CIPHER
@app.route("/playfair")
def playfair():
    return render_template("playfair.html")
@app.route("/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    text = request.form["inputPlainText"]
    key = request.form["inputKeyPlain"]
    cipher = PlayFairCipher()
    matrix = cipher.create_playfair_matrix(key)
    encrypted = cipher.playfair_encrypt(text, matrix)
    return f"text: {text}<br>key: {key}<br>encrypted: {encrypted}"

@app.route("/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    text = request.form["inputCipherText"]
    key = request.form["inputKeyCipher"]
    cipher = PlayFairCipher()
    matrix = cipher.create_playfair_matrix(key)
    decrypted = cipher.playfair_decrypt(text, matrix)
    return f"text: {text}<br>key: {key}<br>decrypted: {decrypted}"

# TRANSPOSITION CIPHER
@app.route("/transposition")
def transposition():
    return render_template("transposition.html")
@app.route("/transposition/encrypt", methods=["POST"])

def transposition_encrypt():
    text = request.form["inputPlainText"]
    key = int(request.form["inputKeyPlain"])
    cipher = TranspositionCipher()
    encrypted = cipher.encrypt(text, key)
    return f"text: {text}<br>key: {key}<br>encrypted: {encrypted}"

@app.route("/transposition/decrypt", methods=["POST"])
def transposition_decrypt():
    text = request.form["inputCipherText"]
    key = int(request.form["inputKeyCipher"])
    cipher = TranspositionCipher()
    decrypted = cipher.decrypt(text, key)
    return f"text: {text}<br>key: {key}<br>decrypted: {decrypted}"

# Main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
