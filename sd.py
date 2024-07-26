import telebot
import re
import csv
import os

# توکن ربات تلگرام خود را در اینجا قرار دهید
API_KEY = "7401363504:AAESkDUtdZ1NU_PoYrnnQ9zJQaAHsjdysqk"

# ایجاد شیء ربات
bot = telebot.TeleBot(API_KEY)

# دیکشنری برای ذخیره تعداد هشتگ‌ها
hashtag_counts = {}
# لیستی برای ذخیره پیام‌ها و هشتگ‌ها
messages_with_hashtags = []

# نام فایل CSV
CSV_FILENAME = 'messsss.csv'

# تابعی برای آماده‌سازی فایل CSV (ایجاد ستون‌های اولیه)
def initialize_csv():
    if not os.path.isfile(CSV_FILENAME):
        with open(CSV_FILENAME, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Username', 'Message', 'Hashtags'])

# تابعی برای نوشتن پیام‌ها و هشتگ‌ها به فایل CSV
def write_to_csv(data):
    with open(CSV_FILENAME, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(data)

# هندلر برای دستور /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Forward messages from the channel to this bot to extract hashtags and save them to a CSV file. Use /search followed by a hashtag to search for messages containing that hashtag.")

# تابعی برای استخراج هشتگ‌ها از متن
def extract_hashtags(text):
    return re.findall(r'#\w+', text)

# هندلر برای دستور /search
@bot.message_handler(commands=['search'])
def ask_for_hashtag(message):
    parts = message.text.split()
    if len(parts) > 1:
        hashtag = parts[1]
        if hashtag.startswith('#'):
            count = hashtag_counts.get(hashtag, 0)
            bot.reply_to(message, f"The hashtag {hashtag} has been mentioned {count} times.")
            # جستجوی پیام‌ها و ذخیره پیام‌هایی که حاوی هشتگ مورد نظر هستند
            filtered_messages = [msg for msg in messages_with_hashtags if hashtag in msg[2]]
            if filtered_messages:
                for msg in filtered_messages:
                    write_to_csv(msg)
                bot.reply_to(message, f"Messages with hashtag {hashtag} saved to CSV.")
            else:
                bot.reply_to(message, f"No messages found with hashtag {hashtag}.")
        else:
            bot.reply_to(message, "Please provide a valid hashtag starting with #.")
    else:
        bot.reply_to(message, "Please provide a hashtag to search for.")

# هندلر برای پیام‌های فوروارد شده
@bot.message_handler(func=lambda message: message.forward_from_chat)
def find_and_store_hashtags(message):
    hashtags = extract_hashtags(message.text)
    if hashtags:
        for hashtag in hashtags:
            hashtag_counts[hashtag] = hashtag_counts.get(hashtag, 0) + 1
            # ذخیره پیام و هشتگ‌ها در لیست
            messages_with_hashtags.append([message.from_user.username, message.text, ', '.join(hashtags)])
        bot.reply_to(message, f"Found hashtags: {', '.join(hashtags)}")
    else:
        bot.reply_to(message, "No hashtags found.")

# آماده‌سازی فایل CSV
initialize_csv()

# شروع به کار ربات
bot.polling()