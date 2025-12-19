"""
Проверка электронных конфигураций для проваливших тесты элементов
"""
from mendeleev import element

def check_element(z, name):
    elem = element(z)
    print(f"\n{name} (Z={z}):")
    print(f"  Конфигурация: {elem.econf}")
    print(f"  Детально:")
    for (n, orb), count in elem.ec.conf.items():
        print(f"    {n}{orb}: {count}")
    # Внешний электрон
    config = [(n, orb, count) for (n, orb), count in elem.ec.conf.items()]
    n_outer, orb_outer, count_outer = config[-1]
    print(f"  Внешний электрон: {n_outer}{orb_outer}")

# Проверим проваливающие тесты
check_element(21, "Scandium")
check_element(26, "Iron")
check_element(30, "Zinc")
