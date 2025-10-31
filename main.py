def total_salary(path):
    salary_list = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                salary = line.strip().split(",")[1]
                salary_list.append(int(salary))
        total = sum(salary_list)
        average = total / len(salary_list)
        return (total, average)
    except FileNotFoundError:
        print("⚠️  File not found:", path)
        return (0, 0)


def main():
    total, average = total_salary("src/list_employee_salarie3s.txt")
    print(
        f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}"
    )


if __name__ == "__main__":
    main()
