"""
Эксперимент для проверки расчета Слейтера для свинца (Pb)
"""
from mendeleev import element

def test_lead_manually():
    """Ручной расчет для свинца по правилам Слейтера"""
    pb = element(82)
    print(f"Элемент: {pb.name} ({pb.symbol}), Z = {pb.atomic_number}")
    print(f"Электронная конфигурация: {pb.econf}")
    print(f"\nДетальная конфигурация из ec.conf:")

    ec_conf = pb.ec.conf
    for (n, orb), count in ec_conf.items():
        print(f"  {n}{orb}: {count} электронов")

    # Преобразуем в список
    config = [(n, orb, count) for (n, orb), count in ec_conf.items()]

    # Внешний электрон
    n_outer, orb_outer, count_outer = config[-1]
    print(f"\nВнешний электрон: {n_outer}{orb_outer} (всего {count_outer} электронов)")

    # Вычисляем S
    print("\n--- Расчет экранирования S ---")
    S = 0.0

    print(f"\nДля внешнего электрона на {n_outer}{orb_outer} орбитали:")

    # Группируем электроны по слоям
    layer_n = []  # Слой n (та же группа)
    layer_n_minus_1_sp = []  # Слой n-1 (s,p)
    layer_n_minus_1_df = []  # Слой n-1 (d,f)
    layer_deeper = []  # Слои n-2 и глубже

    for n, orb, count in config:
        if n == n_outer:
            if (n, orb) == (n_outer, orb_outer):
                # Та же орбиталь - исключаем экранируемый электрон
                layer_n.append((n, orb, count - 1))
            elif orb in ['s', 'p']:
                layer_n.append((n, orb, count))
        elif n == n_outer - 1:
            if orb in ['s', 'p']:
                layer_n_minus_1_sp.append((n, orb, count))
            elif orb in ['d', 'f']:
                layer_n_minus_1_df.append((n, orb, count))
        elif n < n_outer - 1:
            layer_deeper.append((n, orb, count))

    print("\n1. Та же группа (n={}, s/p орбитали):".format(n_outer))
    for n, orb, count in layer_n:
        contrib = count * 0.35
        S += contrib
        print(f"   {n}{orb}: {count} × 0.35 = {contrib}")

    print("\n2. Слой (n-1={}) (s,p орбитали):".format(n_outer - 1))
    for n, orb, count in layer_n_minus_1_sp:
        contrib = count * 0.85
        S += contrib
        print(f"   {n}{orb}: {count} × 0.85 = {contrib}")

    print("\n3. Слой (n-1={}) (d,f орбитали - считаются как внутренние):".format(n_outer - 1))
    for n, orb, count in layer_n_minus_1_df:
        contrib = count * 1.00
        S += contrib
        print(f"   {n}{orb}: {count} × 1.00 = {contrib}")

    print("\n4. Слои (n-2={}) и глубже:".format(n_outer - 2))
    deeper_total = sum(count for _, _, count in layer_deeper)
    for n, orb, count in layer_deeper:
        print(f"   {n}{orb}: {count} электронов")
    contrib = deeper_total * 1.00
    S += contrib
    print(f"   Всего: {deeper_total} × 1.00 = {contrib}")

    Z_eff = pb.atomic_number - S

    print(f"\n--- Результат ---")
    print(f"S = {S}")
    print(f"Z_eff = {pb.atomic_number} - {S} = {Z_eff}")
    print(f"\nОжидаемое значение: Z_eff = 4.15")
    print(f"Совпадение: {'✓' if abs(Z_eff - 4.15) < 0.01 else '✗'}")

    return Z_eff

if __name__ == "__main__":
    test_lead_manually()
