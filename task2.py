VERBOSE_AF = True
VERBOSE_ONELINE = True


def main() -> None:
    alphabet = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"

    text = "Кгжирґоґжяю жбхнмяоочдць лглйч рьґькяріфю оїун'ьгкялць фюякзз кяфнїпцйн шьщсхн. Юзр кї рр зюлга янмлд, мр, ім яябмияойї ґгсіґґж їпяс йбаязрюс, лглйї авжсфямх мхлґшяґіюк зізаи. Щхрїкфґжє шьщс, м гжзґ ююмрююмфзлґе нйчвґжщяграч лпґьсркфзлґе щоґаґмчщомкфґкдм т лчлаоїь нжйкрїїмху шхґ."
    key = "ключ"
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
