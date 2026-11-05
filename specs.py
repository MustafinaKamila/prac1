OIL_DENSITY = 850.0

N1 = 19
N2 = 14

N = N1 + N2
Q_LIQ_TEST = 50 + 3 * (N % 25)
W_PCT_TEST = 15 + 2 * (N % 35)
M_MIN_THRESHOLD = 8.0 + 0.5 * (N % 10)


def read_valid_param(prompt: str, min_val: float, max_val: float) -> float:
    """Запрашивает число в допустимом диапазоне."""
    while True:
        try:
            value = float(input(prompt))

            if min_val <= value <= max_val:
                return value

            print(f"Введите число от {min_val} до {max_val}.")

        except ValueError:
            print("Ошибка: введите число.")


def calc_oil_volume(q_liq: float, w_pct: float) -> float:
    """Расчёт объёма чистой нефти."""
    return q_liq * (1 - w_pct / 100)


def calc_oil_mass(q_oil: float, density: float = OIL_DENSITY) -> float:
    """Перевод объёма нефти в массу."""
    return q_oil * density / 1000


def evaluate_profitability(
        m_oil: float,
        m_min: float = M_MIN_THRESHOLD
) -> str:
    """Определяет статус рентабельности скважины."""
    if m_oil < m_min:
        return "Убыточная (стоп)"
    elif m_oil < 3 * m_min:
        return "Рентабельная (база)"
    else:
        return "Высокодебитная (приоритет)"


if __name__ == "__main__":
    print("Оценка рентабельности скважины")
    print(f"Индивидуальные значения: Qж = {Q_LIQ_TEST} м³/сут, "
          f"W = {W_PCT_TEST}%, M_min = {M_MIN_THRESHOLD:.1f} т/сут")

    q_liq = read_valid_param(
        "Введите дебит жидкости Qж, м³/сут: ",
        0,
        1000
    )

    w_pct = read_valid_param(
        "Введите обводнённость W, %: ",
        0,
        100
    )

    q_oil = calc_oil_volume(q_liq, w_pct)
    m_oil = calc_oil_mass(q_oil)
    status = evaluate_profitability(m_oil)

    print("\nРезультаты расчёта:")
    print(f"Объём нефти Qн: {q_oil:.2f} м³/сут")
    print(f"Масса нефти Mн: {m_oil:.2f} т/сут")
    print(f"Порог M_min: {M_MIN_THRESHOLD:.2f} т/сут")
    print(f"Статус: {status}")
