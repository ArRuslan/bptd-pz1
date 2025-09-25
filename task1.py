from typing import Counter

# pz
#TEXT = "тусҐг їусҐйхй нумтхсгргокї юмчуг щзгув"
# my
#TEXT = "хцфшмжумр хцфіфжкщй лфчїцїікщжешм лщчмссд уе чхцфєею хфжуфо фрщхеяно іфуїягрфо фєсечшн, фєфцфум ше щшцмтеуун шїцмшфцнп"
TEXT = "а оґєсйшрюрз спнзцлжу гзі нзгомєгзйза пжй мямомлж, амомб чмгґллм єюєлюд єлюхлжу ароюр мпмямамбм пїйюгс рю азіпшїмами рґулзїж"
ALPHABET = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"

VERBOSE_AF = False
VERBOSE_ONELINE = False


def decode_text(text: str, key: int, verbose: bool = True) -> str:
    result = ""

    for ch in text:
        if ch.upper() not in ALPHABET:
            if VERBOSE_AF:
                print(f"\"{ch}\" - ігнорується.", end=" " if VERBOSE_ONELINE else "\n")
            result += ch
            continue

        idx = ALPHABET.index(ch.upper())
        if VERBOSE_AF:
            print(f"\"{ch}\" = {idx}.", end=" " if VERBOSE_ONELINE else "\n")
        new_idx = (idx - key) % len(ALPHABET)
        if VERBOSE_AF:
            print(f"{idx} - {key} = {new_idx}.", end=" " if VERBOSE_ONELINE else "\n")
        new_char = ALPHABET[new_idx]
        new_char = new_char.lower() if not ch.isupper() else new_char
        if VERBOSE_AF:
            print(f"{new_idx} = \"{new_char}\".", end=" " if VERBOSE_ONELINE else "\n")
        result += new_char

    if VERBOSE_AF and VERBOSE_ONELINE:
        print()

    if verbose:
        print(key, result)

    return result


def main() -> None:
    text = TEXT.lower()
    for key in range(1, 33):
        decode_text(text, key)


def statistical_thingy() -> None:
    most_common = ["О", "И", "Е", "А"]
    text = TEXT.lower()
    counter = Counter(text)
    diffs = Counter()

    for ch in list(counter.keys()):
        if ch.upper() not in ALPHABET:
            del counter[ch]

    print(f"Most common letters: {', '.join(f'{char}: {count}' for char, count in counter.most_common())}")

    for char, _ in counter.most_common(4):
        for mchar in most_common:
            diff = (ALPHABET.index(char.upper()) - ALPHABET.index(mchar)) % len(ALPHABET)
            print(f"Відстань між \"{char}\" та \"{mchar}\" - {diff}")
            diffs[diff] += 1

    for key, _ in diffs.most_common(4):
        print(f"Key: {key}, deciphered: \"{decode_text(text, key, False)}\"")


if __name__ == "__main__":
    #main()
    statistical_thingy()
