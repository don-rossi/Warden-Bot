# .bot_commands.py

BOT_NAME = "⟁ 𝐖𝐀𝐑𝐃Ξ𝐍🎖️BOT"
BOT_PICTURE = "https://i.imgur.com/your_bot_image.png"  # You can replace with any image URL

WHATSAPP_CHANNEL = "https://whatsapp.com/channel/0029Vb7mwSm3LdQRu3JT5D1B"
WHATSAPP_GROUP = "https://chat.whatsapp.com/GHc5qDYUNeN2w3Nei1yESy?mode=gi_t"

# Commands structure: command_name: {"desc": description, "type": "group/user", "action": "kick/warn/info/etc"}
COMMANDS = {
    ".menu": {"desc": "Show all bot commands", "type": "user", "action": "show_menu"},
    ".antilink": {"desc": "Enable anti-link protection in groups", "type": "group", "action": "toggle_antilink"},
    ".autoview": {"desc": "Auto view statuses", "type": "user", "action": "toggle_autoview"},
    ".chatbot": {"desc": "Chat with the bot", "type": "user", "action": "chat"},
    ".kick": {"desc": "Kick a user from group", "type": "group", "action": "kick_user"},
    ".warn": {"desc": "Warn a user", "type": "group", "action": "warn_user"},
    ".delete": {"desc": "Delete a message", "type": "group", "action": "delete_message"},
    ".antistatusdelete": {"desc": "Prevent users from deleting status", "type": "group", "action": "toggle_antistatusdelete"},
    ".userinfo": {"desc": "Show user info", "type": "user", "action": "show_userinfo"},
}
