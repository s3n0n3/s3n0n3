import random

def generate_key(length):
    """Генерация случайного ключа для шифрования"""
    return ''.join(random.choice('01') for _ in range(length))

def text_to_bin(text):
    """Преобразование текста в двоичное представление"""
    return ''.join(format(ord(char), '08b') for char in text)

def bin_to_text(binary):
    """Преобразование двоичного представления в текст"""
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)

def vernam_encrypt_decrypt(text, key):
    """Шифрование и дешифрование шифра Вернама"""
    binary_text = text_to_bin(text)
    if len(key) != len(binary_text):
        raise ValueError("Длина ключа должна совпадать с длиной текста в двоичном формате")
    
    encrypted_bin = ''.join(str(int(binary_text[i]) ^ int(key[i])) for i in range(len(binary_text)))
    return bin_to_text(encrypted_bin)

def store_encrypted_record(record):
    """Функция для шифрования и хранения записи о расходе материалов"""
    binary_record = text_to_bin(record)
    key = generate_key(len(binary_record))
    encrypted_record = vernam_encrypt_decrypt(record, key)
    print("Зашифрованная запись:", encrypted_record)
    return encrypted_record, key

def retrieve_decrypted_record(encrypted_record, key):
    """Функция для расшифровки записи о расходе материалов"""
    decrypted_record = vernam_encrypt_decrypt(encrypted_record, key)
    print("Расшифрованная запись:", decrypted_record)
    return decrypted_record

# пример расхода
material_record = "Учёт материалов: железо - 20 кг, медь - 15 кг"


encrypted_record, key = store_encrypted_record(material_record)

# дешифрование 
retrieve_decrypted_record(encrypted_record, key)

# Печать ключа для проверки
print("Использованный ключ:", key)