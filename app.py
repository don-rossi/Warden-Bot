from flask import Flask, request, jsonify
import random, string, os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
pairing_codes = {}  # stores pairing codes temporarily

WHATSAPP_CHANNEL = os.getenv("WHATSAPP_CHANNEL")
WHATSAPP_GROUP = os.getenv("WHATSAPP_GROUP")
BOT_NAME = os.getenv("BOT_NAME")

# Generate random 6-character code
def generate_pairing_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

# Endpoint to request pairing code
@app.route("/link", methods=["POST"])
def link_phone():
    data = request.get_json()
    phone_number = data.get("phone")
    
    if not phone_number:
        return jsonify({"error": "Phone number required"}), 400
    
    code = generate_pairing_code()
    pairing_codes[code] = phone_number
    return jsonify({
        "pairing_code": code,
        "message": f"Use this code in WhatsApp to pair with {BOT_NAME}"
    })

# Endpoint to verify pairing code
@app.route("/verify", methods=["POST"])
def verify_code():
    data = request.get_json()
    code = data.get("code")
    
    if code in pairing_codes:
        phone = pairing_codes.pop(code)
        return jsonify({
            "success": True,
            "message": f"Phone {phone} paired! Join the channel: {WHATSAPP_CHANNEL} and group: {WHATSAPP_GROUP}"
        })
    else:
        return jsonify({"error": "Invalid pairing code"}), 400

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
