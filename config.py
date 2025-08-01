import os

# TradingView Example Alert Message:
# {
# "key":"9T2q394M92", "telegram":"-1001298977502", "msg":"Long #{{ticker}} at `{{close}}`"
# }

sec_key = os.environ.get("SEC_KEY", "")

# Telegram Settings
send_telegram_alerts = os.environ.get("SEND_TELEGRAM_ALERTS", "False").lower() == "true"
tg_token = os.environ.get("TG_TOKEN", "")  # Bot token. Get it from @Botfather
channel = int(os.environ.get("CHANNEL", "0"))  # Channel ID (ex. -1001487568087)

# Deshabilitar otras plataformas explícitamente si se lee de config.py original
send_discord_alerts = False
discord_webhook = ""

send_slack_alerts = False
slack_webhook = ""

send_twitter_alerts = False
tw_ckey = ""
tw_csecret = ""
tw_atoken = ""
tw_asecret = ""

send_email_alerts = False
email_sender = ""
email_receivers = [""]
email_subject = "Trade Alert!"
email_port = 465
email_host = ""
email_user = ""
email_password = ""
