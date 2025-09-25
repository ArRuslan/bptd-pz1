VERBOSE_AF = True
VERBOSE_ONELINE = True


def main() -> None:
    alphabet = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"

    text = "Воу Увщґдгб, ягаг еаорвши ґгдгсщр, р ефащ Еєодгбж Ягуояж цшр егпщ бгагушю агібов Яодґг Афємїшю."
    key = 18

    result = ""

    for ch in text:
        if ch.upper() not in alphabet:
            if VERBOSE_AF:
                print(f"\"{ch}\" - ігнорується.", end=" " if VERBOSE_ONELINE else "\n")
            result += ch
            continue

        idx = alphabet.index(ch.upper())
        if VERBOSE_AF:
            print(f"\"{ch}\" = {idx}.", end=" " if VERBOSE_ONELINE else "\n")
        new_idx = (idx - key) % len(alphabet)
        if VERBOSE_AF:
            print(f"{idx} - {key} = {new_idx}.", end=" " if VERBOSE_ONELINE else "\n")
        new_char = alphabet[new_idx]
        new_char = new_char.lower() if not ch.isupper() else new_char
        if VERBOSE_AF:
            print(f"{new_idx} = \"{new_char}\".", end=" " if VERBOSE_ONELINE else "\n")
        result += new_char

    if VERBOSE_AF and VERBOSE_ONELINE:
        print()

    print(text)
    print(result)


if __name__ == "__main__":
    main()
