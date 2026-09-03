#!/usr/bin/env python3
"""
Робот с локальной российской LLM (Ollama + Saiga)
Работает на Mac M1 полностью без интернета!
"""

import os
import sys
import ollama

MODEL_NAME = "akdengi/saiga-llama3-8b"  # Российская модель

def get_llm_response(user_message):
    """Отправляет запрос в локальную LLM Saiga."""
    try:
        response = ollama.chat(
            model=MODEL_NAME,
            messages=[
                {
                    'role': 'system', 
                    'content': 'Ты — дружелюбный русскоязычный робот-помощник. Отвечай кратко и по делу.'
                },
                {'role': 'user', 'content': user_message}
            ]
        )
        return response['message']['content']
    except Exception as e:
        print(f"⚠️ Ошибка LLM: {e}")
        return f"Я робот. Получил запрос: {user_message}"

def robot_speak(text):
    """Робот произносит текст вслух (встроенный синтезатор Mac)."""
    print(f"🤖 Робот говорит: {text}")
    os.system(f'say "{text}"')
    
    with open("speech.txt", "a", encoding="utf-8") as f:
        f.write(f"{text}\n")

def main():
    user_text = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Привет, я робот-стажер!"
    
    print("🧠 LLM думает...")
    response = get_llm_response(user_text)
    robot_speak(response)
    print("✅ Готово!")

if __name__ == "__main__":
    main()