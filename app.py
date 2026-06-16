from flask import Flask, render_template, request, jsonify
from Cipher.Caesar import CaesarCipher
from Cipher.Vigenere import VigenereCipher
from Cipher.RailFence import RailFenceCipher
from Cipher.Playfair import PlayFairCipher
from Cipher.Transposition import TranspositionCipher

app = Flask(__name__)

# ==========================================
# KHỞI TẠO OBJECT THUẬT TOÁN
# ==========================================
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher()
playfair_cipher = PlayFairCipher()
transposition_cipher = TranspositionCipher()


# ==========================================
# HOME PAGE
# ==========================================
@app.route("/")
def home():
    return render_template("index.html")


# ==========================================
# PAGE ROUTES
# ==========================================
@app.route("/caesar")
def caesar_page():
    return render_template("caesar.html")


@app.route("/vigenere")
def vigenere_page():
    return render_template("vigenere.html")


@app.route("/railfence")
def railfence_page():
    return render_template("railfence.html")


@app.route("/playfair")
def playfair_page():
    return render_template("playfair.html")


@app.route("/transposition")
def transposition_page():
    return render_template("transposition.html")


# ==========================================
# CAESAR WEB FORM
# ==========================================
@app.route("/encrypt", methods=["POST"])
def caesar_encrypt_form():
    try:
        text = request.form["inputPlainText"]
        key = int(request.form["inputKeyPlain"])

        encrypted_text = caesar_cipher.encrypt_text(text, key)

        return f"""
        <h2>CAESAR ENCRYPT RESULT</h2>
        <b>Plain Text:</b> {text}<br>
        <b>Key:</b> {key}<br>
        <b>Encrypted Text:</b> {encrypted_text}
        """

    except Exception as e:
        return f"Error: {str(e)}"


@app.route("/decrypt", methods=["POST"])
def caesar_decrypt_form():
    try:
        text = request.form["inputCipherText"]
        key = int(request.form["inputKeyCipher"])

        decrypted_text = caesar_cipher.decrypt_text(text, key)

        return f"""
        <h2>CAESAR DECRYPT RESULT</h2>
        <b>Cipher Text:</b> {text}<br>
        <b>Key:</b> {key}<br>
        <b>Decrypted Text:</b> {decrypted_text}
        """

    except Exception as e:
        return f"Error: {str(e)}"


# ==========================================
# VIGENERE WEB FORM
# ==========================================
@app.route("/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt_form():
    try:
        text = request.form["inputPlainText"]
        key = request.form["inputKeyPlain"]

        encrypted_text = vigenere_cipher.vigenere_encrypt(text, key)

        return f"""
        <h2>VIGENERE ENCRYPT RESULT</h2>
        <b>Plain Text:</b> {text}<br>
        <b>Key:</b> {key}<br>
        <b>Encrypted Text:</b> {encrypted_text}
        """

    except Exception as e:
        return f"Error: {str(e)}"


@app.route("/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt_form():
    try:
        text = request.form["inputCipherText"]
        key = request.form["inputKeyCipher"]

        decrypted_text = vigenere_cipher.vigenere_decrypt(text, key)

        return f"""
        <h2>VIGENERE DECRYPT RESULT</h2>
        <b>Cipher Text:</b> {text}<br>
        <b>Key:</b> {key}<br>
        <b>Decrypted Text:</b> {decrypted_text}
        """

    except Exception as e:
        return f"Error: {str(e)}"


# ==========================================
# RAILFENCE WEB FORM
# ==========================================
@app.route("/railfence/encrypt", methods=["POST"])
def railfence_encrypt_form():
    try:
        text = request.form["inputPlainText"]
        key = int(request.form["inputKeyPlain"])

        encrypted_text = railfence_cipher.rail_fence_encrypt(text, key)

        return f"""
        <h2>RAILFENCE ENCRYPT RESULT</h2>
        <b>Plain Text:</b> {text}<br>
        <b>Key:</b> {key}<br>
        <b>Encrypted Text:</b> {encrypted_text}
        """

    except Exception as e:
        return f"Error: {str(e)}"


@app.route("/railfence/decrypt", methods=["POST"])
def railfence_decrypt_form():
    try:
        text = request.form["inputCipherText"]
        key = int(request.form["inputKeyCipher"])

        decrypted_text = railfence_cipher.rail_fence_decrypt(text, key)

        return f"""
        <h2>RAILFENCE DECRYPT RESULT</h2>
        <b>Cipher Text:</b> {text}<br>
        <b>Key:</b> {key}<br>
        <b>Decrypted Text:</b> {decrypted_text}
        """

    except Exception as e:
        return f"Error: {str(e)}"


# ==========================================
# PLAYFAIR WEB FORM
# ==========================================
@app.route("/playfair/encrypt", methods=["POST"])
def playfair_encrypt_form():
    try:
        text = request.form["inputPlainText"]
        key = request.form["inputKeyPlain"]

        matrix = playfair_cipher.create_playfair_matrix(key)

        encrypted_text = playfair_cipher.playfair_encrypt(text, matrix)

        return f"""
        <h2>PLAYFAIR ENCRYPT RESULT</h2>
        <b>Plain Text:</b> {text}<br>
        <b>Key:</b> {key}<br>
        <b>Encrypted Text:</b> {encrypted_text}
        """

    except Exception as e:
        return f"Error: {str(e)}"


@app.route("/playfair/decrypt", methods=["POST"])
def playfair_decrypt_form():
    try:
        text = request.form["inputCipherText"]
        key = request.form["inputKeyCipher"]

        matrix = playfair_cipher.create_playfair_matrix(key)

        decrypted_text = playfair_cipher.playfair_decrypt(text, matrix)

        return f"""
        <h2>PLAYFAIR DECRYPT RESULT</h2>
        <b>Cipher Text:</b> {text}<br>
        <b>Key:</b> {key}<br>
        <b>Decrypted Text:</b> {decrypted_text}
        """

    except Exception as e:
        return f"Error: {str(e)}"


# ==========================================
# TRANSPOSITION WEB FORM
# ==========================================
@app.route("/transposition/encrypt", methods=["POST"])
def transposition_encrypt_form():
    try:
        text = request.form["inputPlainText"]
        key = int(request.form["inputKeyPlain"])

        encrypted_text = transposition_cipher.encrypt(text, key)

        return f"""
        <h2>TRANSPOSITION ENCRYPT RESULT</h2>
        <b>Plain Text:</b> {text}<br>
        <b>Key:</b> {key}<br>
        <b>Encrypted Text:</b> {encrypted_text}
        """

    except Exception as e:
        return f"Error: {str(e)}"


@app.route("/transposition/decrypt", methods=["POST"])
def transposition_decrypt_form():
    try:
        text = request.form["inputCipherText"]
        key = int(request.form["inputKeyCipher"])

        decrypted_text = transposition_cipher.decrypt(text, key)

        return f"""
        <h2>TRANSPOSITION DECRYPT RESULT</h2>
        <b>Cipher Text:</b> {text}<br>
        <b>Key:</b> {key}<br>
        <b>Decrypted Text:</b> {decrypted_text}
        """

    except Exception as e:
        return f"Error: {str(e)}"


# ==========================================
# API - CAESAR
# ==========================================
@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt_api():
    try:
        data = request.json

        if not data:
            return jsonify({"error": "Invalid JSON"}), 400

        encrypted = caesar_cipher.encrypt_text(
            data["plain_text"],
            int(data["key"])
        )

        return jsonify({
            "algorithm": "Caesar Cipher",
            "plain_text": data["plain_text"],
            "key": data["key"],
            "encrypted_text": encrypted
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt_api():
    try:
        data = request.json

        if not data:
            return jsonify({"error": "Invalid JSON"}), 400

        decrypted = caesar_cipher.decrypt_text(
            data["cipher_text"],
            int(data["key"])
        )

        return jsonify({
            "algorithm": "Caesar Cipher",
            "cipher_text": data["cipher_text"],
            "key": data["key"],
            "decrypted_text": decrypted
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ==========================================
# API - VIGENERE
# ==========================================
@app.route("/api/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt_api():
    try:
        data = request.json

        encrypted = vigenere_cipher.vigenere_encrypt(
            data["plain_text"],
            data["key"]
        )

        return jsonify({
            "encrypted_text": encrypted
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt_api():
    try:
        data = request.json

        decrypted = vigenere_cipher.vigenere_decrypt(
            data["cipher_text"],
            data["key"]
        )

        return jsonify({
            "decrypted_text": decrypted
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ==========================================
# API - RAILFENCE
# ==========================================
@app.route("/api/railfence/encrypt", methods=["POST"])
def railfence_encrypt_api():
    try:
        data = request.json

        encrypted = railfence_cipher.rail_fence_encrypt(
            data["plain_text"],
            int(data["key"])
        )

        return jsonify({
            "encrypted_text": encrypted
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/railfence/decrypt", methods=["POST"])
def railfence_decrypt_api():
    try:
        data = request.json

        decrypted = railfence_cipher.rail_fence_decrypt(
            data["cipher_text"],
            int(data["key"])
        )

        return jsonify({
            "decrypted_text": decrypted
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ==========================================
# API - PLAYFAIR
# ==========================================
@app.route("/api/playfair/encrypt", methods=["POST"])
def playfair_encrypt_api():
    try:
        data = request.json

        matrix = playfair_cipher.create_playfair_matrix(data["key"])

        encrypted = playfair_cipher.playfair_encrypt(
            data["plain_text"],
            matrix
        )

        return jsonify({
            "encrypted_text": encrypted
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    data = request.json
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({"playfair_matrix": playfair_matrix})


@app.route("/api/playfair/decrypt", methods=["POST"])
def playfair_decrypt_api():
    try:
        data = request.json

        matrix = playfair_cipher.create_playfair_matrix(data["key"])

        decrypted = playfair_cipher.playfair_decrypt(
            data["cipher_text"],
            matrix
        )

        return jsonify({
            "decrypted_text": decrypted
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ==========================================
# API - TRANSPOSITION
# ==========================================
@app.route("/api/transposition/encrypt", methods=["POST"])
def transposition_encrypt_api():
    try:
        data = request.json

        encrypted = transposition_cipher.encrypt(
            data["plain_text"],
            int(data["key"])
        )

        return jsonify({
            "encrypted_text": encrypted
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/transposition/decrypt", methods=["POST"])
def transposition_decrypt_api():
    try:
        data = request.json

        decrypted = transposition_cipher.decrypt(
            data["cipher_text"],
            int(data["key"])
        )

        return jsonify({
            "decrypted_text": decrypted
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ==========================================
# MAIN
# ==========================================
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5050,
        debug=True
    )