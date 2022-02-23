import os
# Use the package we installed
from slack_bolt import App

print(os.environ.get("SLACK_BOT_TOKEN"))
print(os.environ.get("SLACK_SIGNING_SECRET"))

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)


# The echo command simply echoes on command
@app.command("/echo")
def repeat_text(ack, respond, command):
    # Acknowledge command request
    ack()
    text = command['text']
    if not text:
        respond('You most provide a person to thank!')
        return

    recipient = text.split(' ')[0]
    app.client.chat_postMessage(channel='<user_id_for_dm>', user='<user_id>', text='i am a robot')
    # store info and increment recipient's 'score'
    # send message to recipient
    respond(f"{command['text']}")


# Add functionality here
# @app.event("app_home_opened") etc


# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))


# /thank <user> <message> -> void
# /view_thanks -> returns all thanks for requesting user
# /view_thanks <user> -> returns thanks for specified user (for managers)
# /view_coin_balance -> returns balance for requestin user
# /shop -> takes user to shopping page