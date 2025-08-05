import re, os, time

id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # digital_botz client config
    API_ID = os.environ.get("API_ID", "rfl")
    API_HASH = os.environ.get("API_HASH", "rdl")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "rfl") 

    # premium account string session required 😢 
    STRING_SESSION = os.environ.get("STRING_SESSION", "rfl")
    
    # database config
    DB_NAME = os.environ.get("DB_NAME", "rfl")     
    DB_URL = os.environ.get("DB_URL", "rdl")
 
    # other configs
    RKN_PIC = os.environ.get("RKN_PIC", "https://i.ibb.co/fzgHjXQn/1752254564132.png")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6318135266').split()]
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001925329161"))

    # free upload limit 
    FREE_UPLOAD_LIMIT = 6442450944  # 6 GB

    # premium mode feature ✅
    UPLOAD_LIMIT_MODE = True 
    PREMIUM_MODE = True 
    
    # force subs
    try:
        FORCE_SUB = int(os.environ.get("FORCE_SUB", "")) 
    except:
        FORCE_SUB = os.environ.get("FORCE_SUB", "modstorexd")
        
    # web response configuration     
    PORT = int(os.environ.get("PORT", "8090"))
    BOT_UPTIME = time.time()


class rkn(object):
    # part of text configuration
    START_TXT = """<b>Ｈ𝙰𝙄, {}👋

✨ Welcome To AI Renamer & Media Magician Bot

📂 Transform your files with AI power! ✨

🛠 FEATURES:
✅ Rename files in seconds! ✏️
✅ Custom thumbnails 🖼️
✅ Convert videos ↔ files easily! 🎥⇄📄
✅ Add custom captions 📝
✅ Edit metadata with Easy! 🔍

<i>🌟 Blazing fast, AI-powered, and loaded with premium features! 🚀</i>

<i>💎Powered By</i> @xspes 🚀</b>"""

    ABOUT_TXT = """<b>╭───────────⍟
├🤖 ᴍy ɴᴀᴍᴇ : {}
├🖥️ Dᴇᴠᴇʟᴏᴩᴇʀꜱ : {}
├👨‍💻 Pʀᴏɢʀᴀᴍᴇʀ : {}
├📕 Lɪʙʀᴀʀʏ : {}
├✏️ Lᴀɴɢᴜᴀɢᴇ: {}
├💾 Dᴀᴛᴀ Bᴀꜱᴇ: {}
├☁️ Pʟᴀᴛꜰᴏʀᴍ: <a href=https://aws.amazon.com/>AWS</a>
├👑 Mᴀɪɴᴛᴀɪɴᴇʀ: <a href=https://t.me/xspes>NAm</a>
├📊 ᴠᴇʀꜱɪᴏɴ: <a href=https://github.com/yuIlariy/Digital-Rename-Bot>{}</a></b>     
╰───────────────⍟ """

    HELP_TXT = """
<b>•></b> /start Tʜᴇ Bᴏᴛ.

✏️ <b><u>Hᴏᴡ Tᴏ Rᴇɴᴀᴍᴇ A Fɪʟᴇ</u></b>
<b>•></b> Sᴇɴᴅ Aɴy Fɪʟᴇ Aɴᴅ Tyᴩᴇ Nᴇᴡ Fɪʟᴇ Nᴀᴍᴇ \nAɴᴅ Sᴇʟᴇᴄᴛ Tʜᴇ Fᴏʀᴍᴀᴛ [ document, video, audio ].           
ℹ️ 𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/DigitalBotz_Support>𝑺𝑼𝑷𝑷𝑶𝑹𝑻 𝑮𝑹𝑶𝑼𝑷</a>
"""

    UPGRADE_PREMIUM = """..."""  # (unchanged for brevity)
    UPGRADE_PLAN = """..."""     # (unchanged for brevity)
    THUMBNAIL = """..."""        # (unchanged for brevity)
    CAPTION = """..."""          # (unchanged for brevity)
    BOT_STATUS = """..."""       # (unchanged for brevity)
    LIVE_STATUS = """..."""      # (unchanged for brevity)
    DIGITAL_METADATA = """..."""# (unchanged for brevity)
    CUSTOM_FILE_NAME = """..."""# (unchanged for brevity)
    DEV_TXT = """..."""          # (unchanged for brevity)
    SEND_METADATA = """..."""   # (unchanged for brevity)

    @staticmethod
    def get_speed_icon(speed: float) -> str:
        """
        Returns a speed icon based on the speed in bytes per second.
        🚀 for fast speeds (>= 8MB/s), 🚨 for slow speeds.
        """
        threshold = 8 * 1024 * 1024  # 8 MB/s
        return "🚀" if speed >= threshold else "🚨"

    RKN_PROGRESS = """<b>
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣

┃    🗂️ ᴄᴏᴍᴘʟᴇᴛᴇᴅ: {1}

┃    📦 ᴛᴏᴛᴀʟ ꜱɪᴢᴇ: {2}

┃    🔋 ꜱᴛᴀᴛᴜꜱ: {0}%

┃    {5} ꜱᴘᴇᴇᴅ: {3}/s

┃    ⏰ ᴇᴛᴀ: {4}

╰━━━━━━━━━━━━━━━━➣
</b>"""


