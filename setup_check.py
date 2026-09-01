import os
import sys

def check_setup():
    print("--- Checking Setup Status ---")
    print(f"Python Version: {sys.version.split()[0]}")
    
    # 1. Check Dotenv & Groq API Key
    try:
        from dotenv import load_dotenv
        load_dotenv()
        key = os.getenv("GROQ_API_KEY")
        if key and key.startswith("gsk_"):
            print("✅ 'GROQ_API_KEY' loaded successfully.")
        else:
            print("❌ 'GROQ_API_KEY' missing or invalid in .env! (Must start with 'gsk_')")
    except ImportError:
        print("❌ Missing 'python-dotenv'. Run: pip install python-dotenv")

    # 2. Check Core OpenAI SDK
    try:
        import openai
        print("✅ Package 'openai' installed.")
    except ImportError:
        print("❌ Missing 'openai'. Run: pip install openai")

    # 3. Check Microsoft Agent Framework
    try:
        import agent_framework
        from agent_framework.openai import OpenAIChatClient
        print("✅ Package 'agent-framework-core' and 'agent-framework-openai' installed.")
    except ImportError:
        print("❌ Missing agent framework packages! Check your requirements.txt.")

if __name__ == "__main__":
    check_setup()
