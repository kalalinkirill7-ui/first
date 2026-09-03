#!/usr/bin/env python3
import os
import ollama

MODEL = "akdengi/saiga-llama3-8b"

def speak(text):
    os.system(f'say "{text}"')

print("🤖 Робот готов к диалогу. Напишите 'выход' чтобы закончить.")
print("-" * 40)

while True:
    user_input = input("Вы: ")
    if user_input.lower() in ["выход", "пока", "exit"]:
        speak("До свидания!")
        break
    
    response = ollama.chat(
        model=MODEL,
        messages=[{'role': 'user', 'content': user_input}]
    )
    
    answer = response['message']['content']
    print(f"🤖 Робот: {answer}")
    speak(answer)