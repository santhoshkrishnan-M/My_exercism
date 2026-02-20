def response(hey_bob):
    # Remove leading and trailing whitespace
    message = hey_bob.strip()

    # 1️⃣ Silence
    if not message:
        return "Fine. Be that way!"

    # Check if message has at least one letter
    has_letters = any(char.isalpha() for char in message)

    # 2️⃣ Yelled Question
    if message.endswith("?") and has_letters and message.isupper():
        return "Calm down, I know what I'm doing!"

    # 3️⃣ Yelling
    if has_letters and message.isupper():
        return "Whoa, chill out!"

    # 4️⃣ Question
    if message.endswith("?"):
        return "Sure."

    # 5️⃣ Anything else
    return "Whatever."