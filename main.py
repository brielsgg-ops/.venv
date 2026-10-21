import math

# функции ввода и валидации
def get_valid_number(promt, min_val, max_val, is_integer=False):
    # функция для ввода и проверки вещественного числа. цикл продолжается, пока не будет введено верное значение
    while True:
        try:
            user_input = input(promt)
            if is_integer:
                value = int(user_input)
            else:
                value = float(user_input)

            if min_val <= value <= max_val:
                return value
            else:
                print(f"Ошибка! значение должно быть в диапазоне от {min_val} до {max_val}. Попробуйте снова.")
        except ValueError:
            print(f"Ошибка! Введите корректное значение число, без лишних букв и иных символов.")

def calculate_drying(mass, w1, w2, k_coeff, temp):
    # расчет массы удаляемой воды
    m_w = mass * mass * (w1 - w2) / (100 - w2)

    # расчет времени сушки
    # используем math.log для натурального логарифма
    tau = (1 / k_coeff) * math.log(w1 / w2)

    # классификация времени сушки
    if tau < 2:
        class_tau = "быстрая сушка"
    elif 2 <= tau <= 12:
        class_tau = "нормальная"
    else:
        class_tau = "длительная"

    return m_w, tau, class_tau

# главная функция
def main():
    print("---> Время сушки влажного материала. <---")
    print("Меню выбора материала:")
    print("1 - древесина (k = 0.008 1/ч)")
    print("2 - керамика (k = 0.004 1/ч)")
    print("3 - зерно (k = 0.012 1/ч)")

    # 1) ввод режима (только целые числа от 1 до 3)
    choice = get_valid_number("Выберите материал (1-3): ", 1, 3, is_integer=True)

    # 2) маршрутизация через match-case
    match choice:
        case 1:
            material_name = "древесина"
            k_coeff = 0.008
        case 2:
            material_name = "керамика"
            k_coeff = 0.004
        case 3:
            material_name = "зерно"
            k_coeff = 0.012
        case _:
    # не работает из-за валидации в get_valid_number,  но нужен для полноты match-case
            print("Ошибка выбора")
            return

    # 3) ввод остальных данных вместе с проверкой диапазонов
    mass = get_valid_number("Введите массу влажного материала в кг [1.5 - 10000]: ", 1.5, 10000.0)

    # w1 - начальная влажность, от 5 до 60
    w1 = get_valid_number("Введите начальную влажность w1 в процентах [5.0 - 60.0]: ", 5.0, 60.0)

    # w1 - начальная влажность, от 5 до 60. цикл, пока в2 меньше в1
    while True:
       w2 = get_valid_number("Введите конечную влажность w2 в процентах [0.1 - 59.9]: ", 0.1, 59.9)
       if w2 < w1:
           break
       else:
           print("Ошибка! Конечная влажность w2={w2} должна быть меньше начальной w1={w1}. Повторите ввод.")

    # t - температура, 40 - 250
    temp = get_valid_number("Введите температуру сушильного агента в градусах Цельсия [40 - 250]: ", 40.0, 250.0)
    # 4) вывод расчета
    m_w, tau, class_tau = calculate_drying(mass, w1, w2, k_coeff, temp)

    # 5) вывод результатов
    print("\n" + "="*40)
    print(f"Выбранный материал: {material_name}")
    print(f"Масса удаляемой воды: {m_w:.2f} кг")
    print(f"Время сушки: {tau:.2f} ч")
    print(f"Класс сушки: {class_tau}")
    print("="*40)

if __name__ == "__main__":
    main()


            
