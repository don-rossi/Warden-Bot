from flask import Flask, request, jsonify
import random, string
from .bot_commands import BOT_NAME, BOT_PICTURE, COMMANDS, WHATSAPP_CHANNEL, WHATSAPP_GROUP

app = Flask(__name__)
pairing_codes = {}  # stores pairing codes temporarily

# Generate random 6-character pairing code
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

# Endpoint to view bot menu
@app.route("/menu", methods=["GET"])
def menu():
    menu_text = f"{BOT_NAME} Commands Menu\n\n"
    for cmd, info in COMMANDS.items():
        menu_text += f"{cmd} - {info['desc']}\n"
    return jsonify({
        "bot_name": BOT_NAME,
        "bot_picture": BOT_PICTURE,
        "whatsapp_channel": WHATSAPP_CHANNEL,
        "whatsapp_group": WHATSAPP_GROUP,
        "menu": menu_text
    })

# Run the bot
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
