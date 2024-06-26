def calculate_lrc(data):
    for i in range(len(data)):
        hex_values = data[i].split()

        # Convert each hex value to decimal and sum them
        total_sum = 0x100 - ( sum(int(value, 16) for value in hex_values) % 0x100 )
        p = data[i] + " " + hex(total_sum)[2:]
        p = p.replace(" ", "")
        p = ":" + p +  "\\r\\n"
        print(p)
str = [
"01 03 15 4A 00 07",
"01 03 15 51 00 07",
"01 03 15 58 00 07",
"01 03 15 5F 00 07",
"01 03 15 66 00 07",
"01 03 15 82 00 07",
"01 03 15 89 00 07",
"01 03 15 90 00 07",
"01 03 15 97 00 07",
"01 03 15 9E 00 07",
"01 03 15 A5 00 07",
"01 03 15 B3 00 07",
"01 03 15 BA 00 07",
"01 03 15 C1 00 07",
"01 03 15 C8 00 07",
"01 03 15 CF 00 07",
"01 03 15 D6 00 07",
"01 03 15 EB 00 07",
"01 03 15 F2 00 07",
"01 03 16 15 00 07",
"01 03 16 1C 00 07",
"01 03 16 23 00 07",
"01 03 16 2A 00 07",
"01 03 16 31 00 07",
"01 03 16 38 00 07",
"01 03 16 3F 00 07",
"01 03 16 46 00 07",
"01 03 16 4D 00 07",
"01 03 16 54 00 07",
"01 03 16 5B 00 07",
"01 03 16 62 00 07",
"01 03 16 69 00 07",
"01 03 16 93 00 07",
"01 03 16 9A 00 07",
"01 03 16 A1 00 07",
"01 03 16 A8 00 07",
"01 03 16 BD 00 07",
"01 03 16 C4 00 07",
"01 03 16 D9 00 07",
"01 03 16 E0 00 07",
"01 03 17 18 00 07",
"01 03 17 1F 00 07",
"01 03 17 26 00 07",
"01 03 17 2D 00 07",
"01 03 17 73 00 07",
"01 03 17 7A 00 07",
"01 03 17 A4 00 07",
"01 0D"
]

calculate_lrc(str)