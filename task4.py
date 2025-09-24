import math

letter_to_number = {
    "А": "1", "И": "2", "Т": "3", "Е": "4", "С": "5", "Н": "6", "О": "7",
    "Б": "81", "В": "82", "Г": "83", "Ґ": "84", "Д": "85", "Є": "86", "Ж": "87", "З": "88", "І": "89", "Ї": "80",
    "Й": "91", "К": "92", "Л": "93", "М": "94", "П": "95", "Р": "96", "У": "97", "Ф": "98", "Х": "99", "Ц": "90",
    "Ч": "01", "Ш": "02", "Щ": "03", "Ь": "04", "Ю": "05", "Я": "06", " ": "07",
}
number_to_letter = {
    value: key for key, value in letter_to_number.items()
}

def decrypt(message: str, key: str) -> str:
    key_encoded = ""
    for char in key:
        key_encoded += letter_to_number[char.upper()]

    print(f"{key_encoded       = !r}")
    print(f"{message           = !r}")

    key_repeat_times = math.ceil(len(message) / len(key_encoded))
    if key_repeat_times > 1:
        key_encoded = key_encoded * key_repeat_times

    print(f"{key_encoded       = !r}")

    plaintext_encoded = ""
    for cipher_num, key_num in zip(message, key_encoded):
        plain = (int(cipher_num) - int(key_num)) % 10
        plaintext_encoded += str(plain)

    print(f"{plaintext_encoded = !r}")

    plaintext = ""
    while plaintext_encoded:
        num = int(plaintext_encoded[0])
        if 1 <= num <= 7:
            plaintext += number_to_letter[plaintext_encoded[0]]
            plaintext_encoded = plaintext_encoded[1:]
        else:
            plaintext += number_to_letter[plaintext_encoded[:2]]
            plaintext_encoded = plaintext_encoded[2:]

    print(f"{plaintext         = !r}")

    return plaintext


def encrypt(message: str, key: str) -> str:
    message_encoded = ""
    for char in message:
        message_encoded += letter_to_number[char.upper()]

    key_encoded = ""
    for char in key:
        key_encoded += letter_to_number[char.upper()]

    print(f"{key_encoded        = !r}")
    print(f"{message_encoded    = !r}")

    key_repeat_times = math.ceil(len(message_encoded) / len(key_encoded))
    if key_repeat_times > 1:
        key_encoded = key_encoded * key_repeat_times

    print(f"{key_encoded        = !r}")

    ciphertext_encoded = ""
    for plain_num, key_num in zip(message_encoded, key_encoded):
        plain = (int(plain_num) + int(key_num)) % 10
        ciphertext_encoded += str(plain)

    print(f"{ciphertext_encoded = !r}")

    return ciphertext_encoded


def main() -> None:
    for message, key in [
        ("87279561301778659553288989517", "ліс"),  # <------ wtf
        ("416117613875320917532542166181", "сол"),
        ("2330993010441478992202587248", "три"),
        ("79507826026767241881559646721719", "два"),
        ("555021504264469821423931205095", "нав"),
        ("89479925747754451753658367718929", "пол"),
        ("62253825593953633817470164591", "одо"),
        ("6229382959335367381141471137", "ода"),
        ("87935393740778315385627989273", "лис"),
        ("79168822636723341442555256787819", "дев"),
    ]:
        try:
            plaintext = decrypt(message, key.upper())
        except Exception as e:
            print(f"Failed to decrypt message: {e.__class__.__name__}: {e}")
        else:
            print("-" * 32)
            ciphertext = encrypt(plaintext, key.upper())

            print(f"Original message and encrypted ciphertext match: {message == ciphertext}")

        print("="*32)


if __name__ == "__main__":
    main()
