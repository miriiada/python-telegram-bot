from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from context_manager import ContextManager
from openai_client import get_chatgpt_response

# Global content manager
context_mgr = ContextManager ()

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Command processor /start"""
    user_id = update.effective_user.id

    # Delete context
    context_mgr.clear_context(user_id)

    # Keyboard with button "New Requests"
    keyboard = [[InlineKeyboardButton("🔄 New Request", callback_data="new_request")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Hello! I'm bot with ChatGPT integration.\n\n "
        "Send me any message, and I will respond using AI\n"
        "I remember the context of our conversation!\n\n"
        "Commands:\n"
        "/start - Start again (delete history)\n"
        "/help - Help",
        reply_markup=reply_markup
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Command processor /help"""
    keyboard = [[InlineKeyboardButton("🔄 New Request", callback_data="new_request")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "ℹ️ <b>How using:</b>\n\n"
        "1. Write me any question\n"
        "2. I will respond using AI\n"
        "3. I remember the context conversation.\n\n"
        "<b>Commands:</b>\n"
        "/start - Delete history and start again\n"
        "/help - Show this reference",
        parse_mode="HTML",
        reply_markup=reply_markup
    )

async def new_request_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Button processor 'New request'"""
    query = update.callback_query
    user_id = update.effective_user.id

    # Clean context
    context_mgr.clear_context(user_id)

    await query.answer("Context cleared! Starting a new conversation.")
    await query.edit_message_text("✅ Context cleared. Asl a new question.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Text message processor """
    user_id = update.effective_user.id
    user_message = update.message.text

    context_mgr.add_message(user_id, "user", user_message)
    message = context_mgr.get_context(user_id)

    await update.message.reply_text("⏳ Think...")
    response = await get_chatgpt_response(message)

    context_mgr.add_message(user_id, "assistant", response)

    keyboard = [[InlineKeyboardButton("🔄 New request", callback_data="new_request")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(response, reply_markup=reply_markup)
