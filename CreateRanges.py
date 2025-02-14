import secp256k1 as ice
from ht import HashTable

target = "739437bb3dd6d1983e66629c5f08c70e52769371"

# Minimum prefix length to consider for a match
min_p = 6

# Percentage value in base 100 for range calculations
pct = 30

A_val = [ (16**n * pct) // 100 for n in range(2, 21) ]

ht = HashTable("ht.bin")

def chk_p(addr, target):
    for i in range(20, min_p-1, -1):
        if addr[:i] == target[:i]:
            return i
    return 0

def get_pk(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield int(line.strip(), 16)

keys = get_pk("range.txt")

for pk in keys:
    if ht.is_range(pk):
        continue
    addr = ice.privatekey_to_h160(0, 1, pk).hex()
    if addr == target:
        with open("TargetFound.txt", "a") as data:
            data.write(f"{pk}={addr}\n")
            break

    m_length = chk_p(addr, target)

    if m_length > 0:
        val = A_val[m_length - 2]
        r1 = pk - val
        r2 = pk + val
        print(f"Skip Range: {r1}:{r2} {addr}")
        ht.add_range(r1, r2)
