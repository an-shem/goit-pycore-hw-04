def get_cats_info(path):
    res = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                cat_info = line.strip().split(",")
                cat = {
                    "id": cat_info[0],
                    "name": cat_info[1],
                    "age": cat_info[2],
                }
                res.append(cat)
        return res
    except FileNotFoundError:
        print("⚠️  File not found:", path)
        return []


def main():
    cats_info = get_cats_info("src/cats_file.txt")
    print(cats_info)


if __name__ == "__main__":
    main()
