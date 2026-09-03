#!/usr/bin/env python3
import os
import sys
import time
import ollama

MODEL = "akdengi/saiga-llama3-8b"

def get_llm_answer(question):
    try:
        response = ollama.chat(
            model=MODEL,
            messages=[{'role': 'user', 'content': question}]
        )
        return response['message']['content']
    except:
        return "Извините, я задумался. Повторите пожалуйста."

def speak(text):
    print("🤖 Робот говорит:", text)
    os.system(f'say "{text}"')

def wave_hand():
    print("👋 Робот машет рукой")
    # Здесь будет код для реального робота
    # Пока просто имитация

def nod_head():
    print("🤖 Робот кивает")
    # Здесь будет код для реального робота

def main():
    print("\n" + "="*40)
    print("🤖 РОБОТ ЗАПУЩЕН")
    print("="*40)
    
    speak("Привет! Я готов общаться")
    nod_head()
    
    while True:
        user = input("\n👤 Вы: ")
        if user.lower() in ["пока", "выход"]:
            speak("До свидания!")
            wave_hand()
            break
        
        print("🧠 Думаю...")
        answer = get_llm_answer(user)
        speak(answer)
        nod_head()

if __name__ == "__main__":
    main()
