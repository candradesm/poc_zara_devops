import json

def read():
    with open("./catalog/partial.txt") as file:
        raw_data = {}
        last_key = ""
        while True:
            line = file.readline()
            if not line:
                break
            if not line.startswith("    "):
                last_key = line.strip()
                raw_data[line.strip()] = []
                continue
            raw_data[last_key].append(line.strip())
        with open("./catalog/partial.json", "w") as file_write:
            json.dump(raw_data, file_write, indent=4)


def proccess():
    data = {}
    with open("./catalog/partial.json") as file:
        data = json.load(file)

    with open("./catalog/java_files.txt", "w") as file_write:
        for key, values in data.items():
            java_files = list(filter(lambda x: x.endswith(".java"), values))
            if len(java_files) > 0:
                # file_write.write(f"{key}\n")
                for java_file in java_files:
                    file_write.write(f"{java_file}\n")


if __name__ == "__main__":
    proccess()
                