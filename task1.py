def main() -> None:
    alphabet = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"

    text = "Воу Увщґдгб, ягаг еаорвши ґгдгсщр, рефащ Еєодгбж Ягуояж цшр егпщбгагушю агібов Яодґг Афємїшю."
    key = 18

    result = ""

    for ch in text:
        if ch.upper() not in alphabet:
            result += ch
            continue

        idx = alphabet.index(ch.upper())
        new_idx = (idx - key) % len(alphabet)
        new_char = alphabet[new_idx]
        result += new_char.lower() if not ch.isupper() else new_char

    print(text)
    print(result)


if __name__ == "__main__":
    main()
