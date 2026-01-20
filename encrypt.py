#!/usr/bin/env python3
"""
Caesar cipher encrypt/decrypt utility.

Usage:
  - Run the script and follow on-screen prompts.
  - Enter any integer for shift (e.g., 3, -5, 29). Shift is normalized modulo 26.
"""

from typing import Callable


def _shift_char(ch: str, shift: int) -> str:
    """Shift a single character preserving case. Non-letters returned unchanged."""
    if 'A' <= ch <= 'Z':
        base = ord('A')
        return chr((ord(ch) - base + shift) % 26 + base)
    if 'a' <= ch <= 'z':
        base = ord('a')
        return chr((ord(ch) - base + shift) % 26 + base)
    return ch


def caesar_encrypt(text: str, shift: int) -> str:
    """Encrypt text with Caesar cipher using positive shift."""
    s = shift % 26
    return ''.join(_shift_char(ch, s) for ch in text)


def caesar_decrypt(text: str, shift: int) -> str:
    """Decrypt text encrypted with Caesar cipher (inverse shift)."""
    s = (-shift) % 26
    return ''.join(_shift_char(ch, s) for ch in text)


def prompt_int(prompt: str) -> int:
    """Prompt repeatedly until user enters a valid integer."""
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Please enter a valid integer for shift.")


def run_interactive():
    print("Caesar Cipher Utility")
    print("---------------------")
    while True:
        print("\nChoose an option:")
        print("  1) Encrypt")
        print("  2) Decrypt")
        print("  3) Exit")
        choice = input("Enter 1, 2 or 3: ").strip()

        if choice == '3':
            print("Exiting.")
            break
        elif choice not in ('1', '2'):
            print("Invalid choice — try again.")
            continue

        message = input("Enter the message: ")
        shift = prompt_int("Enter shift (integer): ")

        if choice == '1':
            result = caesar_encrypt(message, shift)
            action = "Encrypted"
        else:
            result = caesar_decrypt(message, shift)
            action = "Decrypted"

        print(f"\n{action} result:\n{result}")


if __name__ == "__main__":
    run_interactive()
