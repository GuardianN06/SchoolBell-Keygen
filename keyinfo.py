import string

def calculate_checksum(code):
    checksum = 0
    for char in code[:14]:
        checksum += ord(char)
    hex_checksum = hex(checksum)[2:] 
    return hex_checksum[-2:]

def parse_hex_values(code):
    values = []
    slices = [slice(0, 1), slice(1, 3), slice(3, 4), slice(4, 6), slice(6, 9), slice(9, 10), slice(10, 12)]
    for s in slices:
        values.append(int(code[s], 16))
    return values

def ascii_sum(name):
    return sum(ord(c) for c in name.strip())

def map_code(code, codes):
    mapped_code = []
    for i, char in enumerate(code):
        if char in codes[i]:
            index = codes[i].index(char)
            mapped_code.append(chr(index + 48 if index < 10 else index + 55))
        else:
            break
    return ''.join(mapped_code)

def compute_values(name):
    strlen = len(name)
    ascii_sum_val = ascii_sum(name)
    return (strlen + 10) & 0xF, ascii_sum_val & 0xFF, 10 & 0x0F, (ascii_sum_val & 0xFF) + 39

sqlf_code = [
    "SQLFTMKZHJYDVCWP", "XPQDHZFSRYCKWGJV", "CBFNWDQPJZVLKXGS",
    "ZSMXNLYTBFRCGVPD", "BPXWQHSLFTKZDYJV", "LJGNWKMTQRPXVBDH",
    "KZHTMPFLWDGNRJBY", "MDWJNYCLXZRKGQFP", "VDBYJRLSTHFNGMWK",
    "TLXJFMRSVNCYHGZW", "BCRKLJXDVWZSMQHG", "CNWFQGRTHSZDMXJK",
    "WZTXDNKSYCBMGHRF", "YMWBCVJDFZNPXSQH", "CXTHPYZSWNBGFKLJ",
    "WRGSVKXLNCMZDPJB"
]

username = input("Enter name:\n")
code_input = input("Enter key:\n")

if len(code_input) < 12:
    print("Error: The code must be at least 12 characters long.")
else:
    transformed_code = map_code(code_input, sqlf_code)
    if len(transformed_code) == 16:
        np1, np2, np3, np4 = compute_values(username.lower())
        parsed_values = parse_hex_values(transformed_code)
        print("\n" + transformed_code)
        print(calculate_checksum(transformed_code))
        print(f"\nkey: {parsed_values[6]:02}.{parsed_values[5]:02}.{parsed_values[4]:04}")
        print(f"\np1={parsed_values[0]} np1={np1}")
        print(f"p2={parsed_values[1]} np2={np2}")
        print(f"p3={parsed_values[2]} np3={np3}")
        print(f"p4={parsed_values[3]} np4={np4}")
    else:
        print("Failed to transform code adequately.")
