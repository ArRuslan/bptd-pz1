from task4 import otp_decrypt


def main() -> None:
    message = input("Message: ")
    key = input("Key: ")

    ciphertext = otp_decrypt(message, key)
    print(f"Plaintext: {ciphertext!r}")


if __name__ == "__main__":
    main()
