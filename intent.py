def detect_intent(text):
    text = text.lower()

    # Create file intent
    if "create file" in text or "create a file" in text:
        return {"intent": "create_file"}

    # Write code intent
    elif "python file" in text or "write code" in text or "create python file" in text:
        return {
            "intent": "write_code",
            "filename": "generated.py"
        }

    # Summarize intent
    elif "summarize" in text:
        return {"intent": "summarize"}

    # Default: chat
    else:
        return {"intent": "chat"}