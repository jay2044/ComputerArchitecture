import time


def hex_to_bin_extended(hex_num):
    print(hex_num)

    if hex_num.startswith("0x"):
        hex_num = hex_num[2:]

    # Convert the hexadecimal to a binary string
    # Remove '0b' prefix and pad to the length of hex_num * 4 for full representation
    full_binary = bin(int(hex_num, 16))[2:].zfill(len(hex_num) * 4)

    # Check the length of the binary string to adjust operations
    if len(full_binary) < 6:
        return "The binary representation is too short to perform the specified operations."

    # Index: The 2 bits before the last 3 bits
    # Ensure there are at least 6 bits to work with
    if len(full_binary) >= 5:
        index = full_binary[-5:-3]
    else:
        index = "NA"
    print(f"Index: {index}")

    # Replace the last 5 bits with 0, convert back to hex
    new_binary = full_binary[:-5] + "000000" if len(full_binary) > 5 else full_binary
    tag = hex(int(new_binary, 2))[2:].zfill(
        (len(new_binary) + 3) // 4
    )  # Ensure hex digits are fully represented
    print(f"Tag: 0x{tag}")

    # Convert binary strings to decimal
    lower_bound_decimal = int(full_binary[:-3] + "000", 2)
    upper_bound_decimal = int(full_binary[:-3] + "111", 2)

    # Convert decimal numbers to hexadecimal
    lower_bound_hex = hex(lower_bound_decimal)
    upper_bound_hex = hex(upper_bound_decimal)

    # Print formatted range in hexadecimal
    print(f"M[{lower_bound_hex}:{upper_bound_hex}]")

    # LRU Cache Simulation
    if index in cache:
        found = False
        least_recent = None
        current_time = time.time()

        # Check for hit and update last used time
        for entry in cache[index]:
            if entry["tag"] == tag:
                entry["last_used"] = current_time
                print("Hit")
                found = True
                break
            # Track the least recently used entry
            if (
                least_recent is None
                or entry["last_used"] < cache[index][least_recent]["last_used"]
            ):
                least_recent = cache[index].index(entry)

        if not found:
            if len(cache[index]) < 2:  # Assume each set can hold 2 blocks
                cache[index].append({"tag": tag, "last_used": current_time})
                print("Miss - Filling empty slot")
            else:
                # Replace the least recently used entry
                cache[index][least_recent] = {"tag": tag, "last_used": current_time}
                print(f"Miss - Replaced LRU")

    print("\n")


hex_values = [
    "0x1234dc",
    "0x4231fc",
    "0xdcba98",
    "0x1234d8",
    "0x423200",
    "0xdcba9c",
    "0x1234d4",
    "0x423204",
    "0xdcbaa0",
    "0x1234d0",
    "0x423208",
    "0xdcbaa4",
    "0x1234cc",
    "0x42320c",
    "0xdcbaa8",
    "0x1234c8",
    "0x423210",
    "0xdcbaac",
]


cache = {"00": [], "01": [], "10": [], "11": []}
count = 1

for hex_value in hex_values:

    print(count)
    hex_to_bin_extended(hex_value)
    count += 1
