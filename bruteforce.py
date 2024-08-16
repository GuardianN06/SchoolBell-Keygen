import random
import string
import threading

def calculate_checksum(code):
    checksum = 0
    for char in code[:14]:
        checksum += ord(char)
    hex_checksum = hex(checksum)[2:] 
    return hex_checksum.upper()[-2:]

def parse_hex_values(code):
    values = []
    slices = [slice(0, 1), slice(1, 3), slice(3, 4), slice(4, 6), slice(6, 9), slice(9, 10), slice(10, 12)]
    for s in slices:
        values.append(int(code[s], 16))
    return values

def map_code(code, codes):
    mapped_code = []
    for i, char in enumerate(code):
        if char in codes[i]:
            index = codes[i].index(char)
            mapped_code.append(chr(index + 48 if index < 10 else index + 55))
        else:
            break
    return ''.join(mapped_code)

sqlf_code = [
    "SQLFTMKZHJYDVCWP", "XPQDHZFSRYCKWGJV", "CBFNWDQPJZVLKXGS",
    "ZSMXNLYTBFRCGVPD", "BPXWQHSLFTKZDYJV", "LJGNWKMTQRPXVBDH",
    "KZHTMPFLWDGNRJBY", "MDWJNYCLXZRKGQFP", "VDBYJRLSTHFNGMWK",
    "TLXJFMRSVNCYHGZW", "BCRKLJXDVWZSMQHG", "CNWFQGRTHSZDMXJK",
    "WZTXDNKSYCBMGHRF", "YMWBCVJDFZNPXSQH", "CXTHPYZSWNBGFKLJ",
    "WRGSVKXLNCMZDPJB"
]

def brute_force():
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=16))
        transformed_code = map_code(code, sqlf_code)
        if len(transformed_code) == 16:
            parsed_values = parse_hex_values(transformed_code)
            p1 = parsed_values[0]
            p2 = parsed_values[1]
            p3 = parsed_values[2]
            p4 = parsed_values[3]
            if p4 == (p2+39) and p3 == 10:
                print(code)

def start_threads(num_threads):
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=brute_force)
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()

start_threads(30)