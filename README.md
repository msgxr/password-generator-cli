# Password Generator CLI
Python ile yazılmış, kriptografik olarak güvenli şifreler üreten komut satırı aracı. Kullanıcı, şifre uzunluğunu ve kullanılacak karakter tiplerini kolayca belirleyebilir.

## Özellikler
- Uzunluk belirleme
- Büyük harf ekleme/çıkarma seçeneği
- Rakam ekleme/çıkarma seçeneği
- Sembol ekleme/çıkarma seçeneği
- Tamamen terminal üzerinden kullanım
- Python’un `secrets` modülü ile yüksek güvenlik

## Kurulum
1. Depoyu klonlayın: `git clone https://github.com/<kullanici-adi>/password-generator-cli.git && cd password-generator-cli`
2. (Opsiyonel) Sanal ortam oluşturun: `python -m venv .venv && .venv\Scripts\activate` (Windows) veya `source .venv/bin/activate` (macOS/Linux)
3. Ekstra bağımlılık yok, standart kütüphaneler ile çalışır.

## Kullanım
Varsayılan (16 karakter, tüm karakter tipleri): `python password_generator.py`  
24 karakter, sembolsüz: `python password_generator.py -l 24 --no-symbols`  
12 karakter, sadece küçük harf: `python password_generator.py -l 12 --no-upper --no-digits --no-symbols`

## Argümanlar
| Parametre | Açıklama | Varsayılan |
|-----------|----------|------------|
| -l, --length | Şifre uzunluğu | 16 |
| --no-upper | Büyük harf kullanmaz | False |
| --no-digits | Rakam kullanmaz | False |
| --no-symbols | Sembol kullanmaz | False |

## Örnek Çıktı
`$ python password_generator.py -l 20 --no-symbols`  
`gWpCajFzhyyLFVgwWduo`

## Lisans
MIT

