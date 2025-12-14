def main():
    if len(sys.argv) > 1:
        first_arg = sys.argv[1]
        print(f"Аргумент: '{first_arg}'")
        print(f"Тип: {type(first_arg).__name__}")

        # НОВАЯ ПРОВЕРКА: если аргумент --type, то следующий должен быть допустимым типом
        if first_arg == "--type":
            if len(sys.argv) > 2:
                allowed_types = ["int", "str", "bool"]
                param_value = sys.argv[2]
                if param_value in allowed_types:
                    print(f"Корректный тип параметра: {param_value}")
                else:
                    print(f"Ошибка: '{param_value}' не является допустимым типом. Допустимо: {allowed_types}")
            else:
                print("Ошибка: после --type необходимо указать значение.")
    else:
        print("Аргументы не переданы.")