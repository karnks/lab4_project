import sys

def main():
    # Проверяем, переданы ли аргументы командной строки
    if len(sys.argv) > 1:
        # sys.argv[0] - это имя скрипта, sys.argv[1] - первый аргумент
        first_arg = sys.argv[1]
        print(f"Первый переданный аргумент: '{first_arg}'")
        print(f"Тип аргумента (в виде строки): {type(first_arg).__name__}")
    else:
        print("Аргументы командной строки не переданы.")

if __name__ == "__main__":
    main()