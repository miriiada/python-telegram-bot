import logging
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from config import TELEGRAM_TOKEN
from handlers import start_command, help_command, handle_message, new_request_callback

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CallbackQueryHandler(new_request_callback, pattern="new_request"))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # launching the bot
    logger.info("Bot launched!")
    app.run_polling()

if __name__ == "__main__":
    main()