from task4 import otp_encrypt


def main() -> None:
    message = input("Message: ")
    key = input("Key: ")

    ciphertext = otp_encrypt(message, key)
    print(f"Ciphertext: {ciphertext!r}")


if __name__ == "__main__":
    main()
