
TEXT_LOCATION = "data/PINUS.txt"
CSV_LOCATION = "data/PINUS.csv"

import logging

csv = open(CSV_LOCATION, "w")
csv.write(",".join(["Date", "Name", "Text"]))
csv.write("\n")
with open(TEXT_LOCATION) as f:
    for line in f:
        try:
            date_content = line.split(" - ")
        except Exception as err:
            print("Error date_content")
            print(err)
            print(line)
        else:
            if len(date_content) == 1:
                continue
            date = date_content[0]
            date = date.replace(",", "")
            content = "".join(date_content[1:])
            try:
                name_text = content.split(":")
            except Exception as err:
                print("Error name_text")
                print(err)
                print(line)
            else:
                if len(name_text) == 1:
                    continue
                name = name_text[0]
                text = "".join(name_text[1:])
                text = text.replace(",", "")
                csv.write(",".join([date, name, text]))
    f.close()
csv.close()
