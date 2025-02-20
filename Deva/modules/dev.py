import os
import subprocess
import sys
from contextlib import suppress
from time import sleep

from telegram import TelegramError, Update
from telegram.error import Unauthorized
from telegram.ext import CallbackContext, CommandHandler

import Deva
from Deva import dispatcher
from Deva.modules.helper_funcs.chat_status import dev_plus


@dev_plus
def allow_groups(update: Update, context: CallbackContext):
    args = context.args
    if not args:
        update.effective_message.reply_text(f"Current state: {Deva.ALLOW_CHATS}")
        return
    if args[0].lower() in ["off", "no"]:
        Deva.ALLOW_CHATS = False
    elif args[0].lower() in ["yes", "on"]:
        Deva.ALLOW_CHATS = True
    else:
        update.effective_message.reply_text("Format: /lockdown Yes/No or Off/On")
        return
    update.effective_message.reply_text("Done! Lockdown value toggled.")


@dev_plus
def leave(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    if args:
        chat_id = str(args[0])
        try:
            bot.leave_chat(int(chat_id))
        except TelegramError:
            update.effective_message.reply_text("I couldn't leave that group.")
            return
        with suppress(Unauthorized):
            update.effective_message.reply_text("I left that group!")
    else:
        update.effective_message.reply_text("Send a valid chat ID.")


@dev_plus
def gitpull(update: Update, context: CallbackContext):
    sent_msg = update.effective_message.reply_text("Pulling latest changes...")

    result = subprocess.run(["git", "pull"], capture_output=True, text=True)

    sent_msg.edit_text(f"Git Pull Output:\n{result.stdout}\nRestarting in...")

    for i in reversed(range(5)):
        sent_msg.edit_text(f"Restarting in {i+1}...")
        sleep(1)

    restart_bot()


@dev_plus
def restart(update: Update, context: CallbackContext):
    update.effective_message.reply_text("Restarting bot...")

    restart_bot()


def restart_bot():
    python = sys.executable
    os.execl(python, python, *sys.argv)


LEAVE_HANDLER = CommandHandler("leave", leave)
GITPULL_HANDLER = CommandHandler("gitpull", gitpull)
RESTART_HANDLER = CommandHandler("reboot", restart)
ALLOWGROUPS_HANDLER = CommandHandler("lockdown", allow_groups)

dispatcher.add_handler(ALLOWGROUPS_HANDLER)
dispatcher.add_handler(LEAVE_HANDLER)
dispatcher.add_handler(GITPULL_HANDLER)
dispatcher.add_handler(RESTART_HANDLER)

__mod_name__ = "Dᴇᴠ"
__handlers__ = [LEAVE_HANDLER, GITPULL_HANDLER, RESTART_HANDLER, ALLOWGROUPS_HANDLER]
