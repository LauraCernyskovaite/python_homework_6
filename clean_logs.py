def celsius_converter(f_temp):
    c_temp = (float(f_temp) - 32) * 5 / 9
    return round(c_temp, 2)

def parse_and_clean(line):
    parts = line.split("|")
    parts = [part.strip() for part in parts]

    if len(parts) != 5:
        return None

    if "" in parts:
        return None

    if parts[4] != "ACTIVE":
        return None

    try:
        float(parts[2])
        float(parts[3])
    except ValueError:
        return None

    return parts


import csv

skipped_lines = 0
valid_lines = 0

with open("environmental_raw.txt", "r", encoding="utf-8") as input_file, \
     open("environmental_clean.csv", "w", newline="", encoding="utf-8") as output_file:

    writer = csv.writer(output_file)

    writer.writerow([
        "Timestamp", "StationID", "Temp(C)",
        "Humidity(%)", "Sensor_Status"
    ])

    for line in input_file:
        cleaned = parse_and_clean(line)

        if cleaned is None:
            skipped_lines += 1
            continue

        cleaned[2] = celsius_converter(cleaned[2])

        writer.writerow(cleaned)
        valid_lines += 1

print("Data cleaning completed!")
print("Valid lines:", valid_lines)
print("Skipped lines:", skipped_lines)
