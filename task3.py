def main() -> None:
    alphabet = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"

    text = "Єхєйеґ дєг нєедквдгп ієшю живґщ щобівррнр Пхщ Фсвюд 1984 меаи. Рєд дєшлієзшю, нґ пяью ш'прегпжн їечвшюяєзл ююаддезждрпупзш шв сюуижщзшз вбої єґ'о рпк єґлєкуз румчєи Оіяєь, єк кх егдтптшіе р жяісфґж лжґйфбіеи оюихґєеїьботяю сжбо-обгяе єцвні. Фдряюя кон яфцн Фсвюдщ ьпвшфсбреш гщлф ижпжшюен бдеєждсмсиюїйен угіесдакґадм, щгх т 2000 дккь, щоюцобш кцгюю юяфдбєб сєодгщтгниь т фіядзшудьа ямюдзгяжпіщж, яфцм юцпвгнр сзщіюжь р ґюжзн."
    key = "спрощ"
    result = ""

    key_index = 0
    for char in text:
        if char.upper() not in alphabet:
            result += char
            continue

        key_char = key[key_index % len(key)]
        key_index += 1

        char_index = alphabet.index(char.upper())
        key_char_index = alphabet.index(key_char.upper())

        decrypted_idx = (char_index - key_char_index) % len(alphabet)
        decrypted_char = alphabet[decrypted_idx]
        result += decrypted_char.lower() if not char.isupper() else decrypted_char

    print(text)
    print(result)


if __name__ == "__main__":
    main()

























































# I didn't understand task correctly at first, i thought we need to implement known plaintext attack or whatever it called

# def main() -> None:
#     alphabet = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
#
#     text = "Єхєйеґ дєг нєедквдгп ієшю живґщ щобівррнр Пхщ Фсвюд 1984 меаи. Рєд дєшлієзшю, нґ пяью ш'прегпжн їечвшюяєзл ююаддезждрпупзш шв сюуижщзшз вбої єґ'о рпк єґлєкуз румчєи Оіяєь, єк кх егдтптшіе р жяісфґж лжґйфбіеи оюихґєеїьботяю сжбо-обгяе єцвні. Фдряюя кон яфцн Фсвюдщ ьпвшфсбреш гщлф ижпжшюен бдеєждсмсиюїйен угіесдакґадм, щгх т 2000 дккь, щоюцобш кцгюю юяфдбєб сєодгщтгниь т фіядзшудьа ямюдзгяжпіщж, яфцм юцпвгнр сзщіюжь р ґюжзн."
#     known_plaintext = "Першим про спрощення"
#     key = ""
#     result = ""
#
#     for encrypted, plain in zip(text[:len(known_plaintext)], known_plaintext):
#         # D = C - K
#         # plain = encrypted - key
#         # plain - encrypted = -key
#         # key = encrypted - plain
#
#         if encrypted.upper() not in alphabet:
#             continue
#
#         encrypted_index = alphabet.index(encrypted.upper())
#         plain_index = alphabet.index(plain.upper())
#
#         key_index = (encrypted_index - plain_index) % len(alphabet)
#
#         key += alphabet[key_index]
#
#     print(key)