import secp256k1 as ice
import random
from ht import HashTable

target = "739437bb3dd6d1983e66629c5f08c70e52769371"

start = 73786976294838206463
end = 147573952589676412927

# Minimum prefix length to consider for a match
min_p = 6

# Percentage value in base 100 for range calculations
pct = 30

A_val = [(16**n * pct) // 100 for n in range(2, 21)]

ht = HashTable("ht.bin")

def chk_p(addr, target):
    for i in range(20, min_p-1, -1):
        if addr[:i] == target[:i]:
            return i
    return 0

while True:
    rand = random.randint(start, end)
    if ht.is_range(rand):
        continue
    addr = ice.privatekey_to_h160(0, 1, rand).hex()
    if addr == target:
        with open("TargetFound.txt", "a") as data:
            data.write(f"{rand}={addr}\n")
            break

    m_length = chk_p(addr, target)

    if m_length > 0:
        val = A_val[m_length - 2]
        r1 = rand - val
        r2 = rand + val
        print(f"Skip Range: {r1}:{r2} {addr}")
        ht.add_range(r1, r2)
        
        with open("range.txt", "a") as range_file:
            range_file.write(f"0x{rand:x}\n")
