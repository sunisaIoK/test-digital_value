
# โจทย์ 2 : การหาคำที่ใช้ตัวอักษรทุกตัวในภาษาอังกฤษอย่างน้อยหนึ่งครั้ง (Pangram)
# รายละเอียด: เขียนโปรแกรมที่รับสตริงหนึ่งสตริงแล้วตรวจสอบว่าสตริงนั้นเป็น Pangram หรือไม่ ถ้าใช่ ให้หาคำที่ยาวที่สุดในสตริงนั้น
# อินพุต: สตริงหนึ่งสตริง
# เอาท์พุต: สตริงที่เป็นคำยาวที่สุดในสตริงที่เป็น Pangram หรือข้อความแสดงว่าไม่ใช่ Pangram
# ตัวอย่าง:
# อินพุต: "The quick brown fox jumps over the lazy dog"
# เอาท์พุต: "jumps"
# อินพุต: "Hello world"
# เอาท์พุต: "Not a Pangram"

import string

def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    return alphabet <= set(s.lower())

def longest_words(s):
    words = s.split()
    max_length = len(max(words, key=len))
    return [word for word in words if len(word) == max_length]

def pangram_and_longest_words(s):
    if is_pangram(s):
        longest = longest_words(s)
        return True, longest
    else:
        return False, None

input_string = "Pack my box with five dozen liquor jugs."
is_pangram, longest = pangram_and_longest_words(input_string)
print(f"string: \"{input_string}\"")
print(f"เป็น Pangram: {is_pangram}")
if is_pangram:
    print(f"คำที่ยาวที่สุด: {', '.join(longest)}")
