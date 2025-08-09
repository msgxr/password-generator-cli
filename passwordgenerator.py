#!/usr/bin/env python3
"""
password_generator.py
----------------------
Güvenli rastgele şifre üreten CLI aracı.
Python'un 'secrets' modülünü kullanır, kriptografik olarak güvenlidir.
"""

import argparse
import string
import secrets


def generate_password(length: int, use_upper: bool, use_digits: bool, use_symbols: bool) -> str:
    """
    Belirtilen parametrelere göre güvenli şifre üretir.

    :param length: Şifrenin uzunluğu
    :param use_upper: Büyük harf kullanılsın mı
    :param use_digits: Rakamlar kullanılsın mı
    :param use_symbols: Semboller kullanılsın mı
    :return: Üretilmiş şifre
    """
    # Temel karakter kümesi: küçük harfler
    alphabet = list(string.ascii_lowercase)

    # Opsiyonel karakter kümeleri
    if use_upper:
        alphabet += list(string.ascii_uppercase)
    if use_digits:
        alphabet += list(string.digits)
    if use_symbols:
        alphabet += list("!@#$%^&*()-_=+[]{};:,.?/\\|")

    if not alphabet:
        raise ValueError("En az bir karakter seti seçmelisiniz.")

    # Güvenli rastgele seçim
    return ''.join(secrets.choice(alphabet) for _ in range(length))


def main():
    """
    Argümanları işler ve şifreyi üretir.
    """
    parser = argparse.ArgumentParser(
        description="Güvenli rastgele şifre üretici (CLI)",
        epilog="Örnek: python password_generator.py -l 20 --no-symbols"
    )
    parser.add_argument("-l", "--length", type=int, default=16, help="Şifre uzunluğu (varsayılan: 16)")
    parser.add_argument("--no-upper", action="store_true", help="Büyük harf kullanma")
    parser.add_argument("--no-digits", action="store_true", help="Rakam kullanma")
    parser.add_argument("--no-symbols", action="store_true", help="Sembol kullanma")
    args = parser.parse_args()

    password = generate_password(
        length=args.length,
        use_upper=not args.no_upper,
        use_digits=not args.no_digits,
        use_symbols=not args.no_symbols
    )

    print(password)


if __name__ == "__main__":
    main()
