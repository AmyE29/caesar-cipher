import pytest
from caesar_cipher import encrypt, decrypt

def test_encrypt_1():
    text = 'Hello'
    expected = 'Jgnnq'
    assert encrypt(text, 2) == expected

def test_decrypt_1():
    encrypted_text = 'Jgnnq'
    expected = 'Hello'
    assert decrypt(encrypted_text, 2) == expected

def test_encrypt_2():
    text = 'Peanut'
    expected = 'Tieryx'
    assert encrypt(text, 4) == expected

def test_decrypt_2():
    encrypted_text = 'Tieryx'
    expected = 'Peanut'
    assert decrypt(encrypted_text, 4) == expected

def test_encrypt_3():
    text = 'Sasquatch'
    expected = 'Ygywagzin'
    assert encrypt(text, 6) == expected

def test_decrypt_3():
    encrypted_text = 'Ygywagzin'
    expected = 'Sasquatch'
    assert decrypt(encrypted_text, 6) == expected