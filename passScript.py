import itertools

common_passwords = ["password", "123456", "qwerty", "letmein", "football", "welcome"]


def passwords(length):
    characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    for password in itertools.product(characters, repeat=length):
        yield "".join(password)


def check_and_add_password(password):
    global common_passwords
    if password not in common_passwords:
        common_passwords.append(password)
        print(f"Added '{password}' to common passwords.")


def main():
    target_password = "secret"
    found = False

    for password in common_passwords:
        if password == target_password:
            print(f"Password found: {password}")
            found = True
            break

    if not found:
        max_length = 6
        for length in range(1, max_length + 1):
            for password in passwords(length):
                if password == target_password:
                    print(f"Password found: {password}")
                    found = True
                    check_and_add_password(password)
                    break
            if found:
                break

    if not found:
        print("Password not found. Try increasing the max length or using more powerful techniques.")


if __name__ == "__main__":
    main()
