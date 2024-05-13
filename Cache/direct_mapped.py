def hex_to_bin_extended(hex_num):
    print(hex_num)

    if hex_num.startswith("0x"):
        hex_num = hex_num[2:]

    full_binary = bin(int(hex_num, 16))[2:].zfill(len(hex_num) * 4)

    if len(full_binary) < 6:
        return "The binary representation is too short to perform the specified operations."

    if len(full_binary) >= 6:
        index = full_binary[-6:-4]
    else:
        index = "NA"
    print(f"Index: {index}")

    new_binary = full_binary[:-6] + "000000" if len(full_binary) > 6 else full_binary
    tag = hex(int(new_binary, 2))[2:].zfill(
        (len(new_binary) + 3) // 4
    )
    print(f"Tag: 0x{tag}")

    lower_bound_decimal = int(full_binary[:-4] + "0000", 2)
    upper_bound_decimal = int(full_binary[:-4] + "1111", 2)

    lower_bound_hex = hex(lower_bound_decimal)
    upper_bound_hex = hex(upper_bound_decimal)

    print(f"M[{lower_bound_hex}:{upper_bound_hex}]")

    if index in cache:
        if cache[index] == str(tag):
            print("Hit")
        else:
            print(f"Miss")
            cache[index] = str(tag)

    print("\n")


hex_values = [
    "0x40028",
    "0x4002c",
    "0x40030",
    "0x40034",
    "0x40038",
    "0x4003c",
    "0x40040",
    "0x40044",
    "0x40048",
    "0x4004c",
    "0x40050",
    "0x40054",
    "0x40058",
    "0x4005c",
    "0x40060",
    "0x40064",
    "0x40068",
    "0x4006c",
    "0x4003c",
    "0x40040",
    "0x40044",
    "0x40048",
    "0x4004c",
    "0x40050",
    "0x40054",
    "0x40058",
    "0x4005c",
    "0x40060",
    "0x40064",
    "0x40068",
    "0x4006c",
    "0x4003c",
    "0x40040",
    "0x40044",
    "0x40048",
    "0x4004c",
    "0x40050",
    "0x40054",
    "0x40058",
    "0x4005c",
    "0x40060",
    "0x40064",
    "0x40068",
    "0x4006c",
    "0x40070",
]

cache = {"00": "", "01": "", "10": "", "11": ""}
count = 1

for hex_value in hex_values:

    print(count)
    hex_to_bin_extended(hex_value)
    count += 1
