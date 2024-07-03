# โจทย์ 1 : การหาค่าผสมที่เป็นไปได้ของเลขชุดที่ให้ผลรวมเป็นจำนวนเฉพาะ 
# รายละเอียด: เขียนโปรแกรมที่รับอาร์เรย์ของจำนวนเต็มและจำนวนเต็มหนึ่งจำนวน (ผลรวมที่ต้องการ) 
# แล้วทำการหาค่าผสมของตัวเลขในอาร์เรย์ที่มีผลรวมเป็นจำนวนเฉพาะ
# อินพุต: อาร์เรย์ของจำนวนเต็ม และจำนวนเต็มหนึ่งจำนวน
# เอาท์พุต: ลิสต์ของค่าผสมที่ผลรวมเป็นจำนวนเฉพาะ

from itertools import combinations
import numpy as np
from itertools import combinations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_combinations(arr, target_sum):
    result = []
    for r in range(1, len(arr) + 1):
        for combo in combinations(arr, r):
            if sum(combo) == target_sum:
                result.append(list(combo))
    return result

def prime_sum_combinations(arr, target_sum):
    if not is_prime(target_sum):
        return []
    all_combinations = find_combinations(arr, target_sum)
    return all_combinations

arr = [2, 3, 4, 5, 6, 7]
target_sum = 13
result = prime_sum_combinations(arr, target_sum)
print(f"อาร์เรย์ของจำนวนเต็ม: {arr}")
print(f"จำนวนเต็มหนึ่งจำนวน (ผลรวมที่ต้องการ): {target_sum}")
print(f"ค่าผสมที่เป็นไปได้: {result}")
