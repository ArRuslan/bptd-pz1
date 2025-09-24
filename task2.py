def main() -> None:
    alphabet = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"

    text = "Кгжирґоґжяю жбхнмяоочдць лглйч рьґькяріфю оїун'ьгкялць фюякзз кяфнїпцйн шьщсхн. Юзр кї рр зюлга янмлд, мр, ім яябмияойї ґгсіґґж їпяс йбаязрюс, лглйї авжсфямх мхлґшяґіюк зізаи. Щхрїкфґжє шьщс, м гжзґ ююмрююмфзлґе нйчвґжщяграч лпґьсркфзлґе щоґаґмчщомкфґкдм т лчлаоїь нжйкрїїмху шхґ."
    key = "ключ"
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
