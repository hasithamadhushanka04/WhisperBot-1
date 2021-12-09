from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}.
Welcome to {}

A TeleGram Bot to send messages to a person secretly!

You can use me to send whispers to your friend in groups and channels (even if I'm not there).
Only that friend and you will be able to read the message even though others are in same group. 

To see how to use me press 'How to Use' below.

By @CloudUpdateslk
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔒 Send a Whisper 🔒", switch_inline_query="")],
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("🔒 Send a Whisper 🔒", switch_inline_query="")
        ],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("updates channel", url="https://t.me/CloudUpdateslk")],
    ]

    # Help Message
    HELP = """
Just type the message in below format in any chat.

`@WhisperStarkBot your_message friend_username/id`
    """

    # About Message
    ABOUT = """
hi
    """
