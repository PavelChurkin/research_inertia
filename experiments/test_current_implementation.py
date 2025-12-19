"""
Проверка текущей реализации для свинца
"""
from mendeleev import element
import sys
sys.path.insert(0, '/tmp/gh-issue-solver-1766138101227')
from research_inertia import get_effective_nuclear_charge

def test_current_implementation():
    pb = element(82)
    z_eff = get_effective_nuclear_charge(pb)
    print(f"Текущая реализация для Pb (Z=82): Z_eff = {z_eff}")
    print(f"Ожидаемое значение: Z_eff = 4.15")
    print(f"Разница: {abs(z_eff - 4.15):.4f}")
    print(f"Совпадение: {'✓' if abs(z_eff - 4.15) < 0.01 else '✗'}")

if __name__ == "__main__":
    test_current_implementation()
