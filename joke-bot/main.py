import random

import markovify
from telebot import TeleBot
from telebot.types import Message
from config import TOKEN
from transformers import GPT2LMHeadModel, GPT2Tokenizer


print("Initializing tokenizer...")
tok = GPT2Tokenizer.from_pretrained("anekdoty")
print("Initializing model...")
model = GPT2LMHeadModel.from_pretrained("anekdoty")
print("Initializing Markov chain model")
with open("markov.json") as f:
    model_json = f.read()

start_model = markovify.NewlineText.from_json(model_json)
print(start_model.retain_original)

bot = TeleBot(token=TOKEN)


def generate_start_joke(size=(2, 6)):
    return ' '.join(start_model.make_short_sentence(100).split(' ')[:random.randint(*size)])


def generate_joke(start=None, num=1):
    if start is None:
        start = generate_start_joke()

    text = "<s>" + start
    text = tok.encode(text, return_tensors="pt")
    output = model.generate(text, max_length=500, repetition_penalty=1.0, do_sample=True, top_k=10, top_p=0.95,
                            temperature=1, num_return_sequences=num)

    output = tok.decode(output[0], clean_up_tokenization_spaces=True)
    output = output[output.find("<s>") + 3: output.find('</s>')]

    return output


@bot.message_handler(commands=["start"])
def start_handler(m: Message):
    bot.send_message(m.chat.id,
                     f"""Привет, {m.from_user.first_name}!\n"""
                     f"""Я могу сгенерировать какие-то шутки, качественные или нет, хз:)\n"""
                     f"""Будь осторожен, я могу быть расистом или гомофобом, был обучен на русских анекдотах:с""")


@bot.message_handler(commands=["generate"])
def generate_handler(m: Message):
    bot.send_message(m.chat.id, generate_joke())


@bot.message_handler(content_types=["text"])
def generate_text_handler(m: Message):
    bot.send_message(m.chat.id, generate_joke(m.text, 1))


print("Starting bot...")
bot.polling()
