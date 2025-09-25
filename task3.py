VERBOSE_AF = True
VERBOSE_ONELINE = True


def main() -> None:
    alphabet = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"

    #text = "Єхєйеґ дєг нєедквдгп ієшю живґщ щобівррнр Пхщ Фсвюд 1984 меаи. Рєд дєшлієзшю, нґ пяью ш'прегпжн їечвшюяєзл ююаддезждрпупзш шв сюуижщзшз вбої єґ'о рпк єґлєкуз румчєи Оіяєь, єк кх егдтптшіе р жяісфґж лжґйфбіеи оюихґєеїьботяю сжбо-обгяе єцвні. Фдряюя кон яфцн Фсвюдщ ьпвшфсбреш гщлф ижпжшюен бдеєждсмсиюїйен угіесдакґадм, щгх т 2000 дккь, щоюцобш кцгюю юяфдбєб сєодгщтгниь т фіядзшудьа ямюдзгяжпіщж, яфцм юцпвгнр сзщіюжь р ґюжзн."
    #key = "спрощ"

    text = "Бмлдяц бьй южьаебчез жсвт ивсцд птлдцшїиз Лле Дтцць 1984 лшга. Нсї щзрбамяяї, іш чфур ф'зьрґигз ішьххїеюіє нрзшзргяйїїїляд зг їцлзьяяху зхрґ цц'ч иуш бшуяєїд иаьшюд Иисир, ґш см жшфішїяха і мфґирчо щзшжмааза лїнмеяхбефтгцт щачє-кфййє юсчма. Чшнйду миг самс Длцеьт плхддтхлюч хядс флиирншц фзрбяййзиестчєж ошишфшьшіфєж, лхб ї 2000 зшжс, ґифлкфд шччцу ьсчшюсж їзифхдїєюґс ь мґсбядґесш флржяайлийсч, самр їриишиз няехяях ї гріяк."
    key = "лишити"

    result = ""

    printed_char_desc = False

    key_index = 0
    for char in text:
        if char.upper() not in alphabet:
            if VERBOSE_AF:
                print(f"\"{char}\" - ігнорується.", end=" " if VERBOSE_ONELINE else "\n")
            result += char
            continue

        key_char = key[key_index % len(key)]
        key_index += 1

        char_index = alphabet.index(char.upper())
        key_char_index = alphabet.index(key_char.upper())

        if VERBOSE_AF:
            char_desc = "Т" if printed_char_desc else "Буква тексту (далі Т)"
            key_desc = "К" if printed_char_desc else "Буква ключа (далі К)"
            print(f"{char_desc} \"{char}\" = {char_index}.", end=" " if VERBOSE_ONELINE else "\n")
            print(f"{key_desc} \"{key_char}\" = {key_char_index}.", end=" " if VERBOSE_ONELINE else "\n")
            printed_char_desc = True

        decrypted_idx = (char_index - key_char_index) % len(alphabet)
        if VERBOSE_AF:
            print(f"{char_index} - {key_char_index} = {decrypted_idx}.", end=" " if VERBOSE_ONELINE else "\n")

        decrypted_char = alphabet[decrypted_idx]
        decrypted_char = decrypted_char.lower() if not char.isupper() else decrypted_char
        if VERBOSE_AF:
            print(f"{decrypted_idx} = \"{decrypted_char}\".", end=" " if VERBOSE_ONELINE else "\n")

        result += decrypted_char

    if VERBOSE_AF and VERBOSE_ONELINE:
        print()

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