#!/usr/bin/env python3
"""
Unit tests for get_effective_nuclear_charge function using Slater's rules.
"""

import unittest
from mendeleev import element
from research_inertia import get_effective_nuclear_charge


class TestSlaterRules(unittest.TestCase):
    """Test cases for Slater's rules implementation."""

    def test_nitrogen(self):
        """
        Test Nitrogen (Z=7).
        Configuration: 1s² 2s² 2p³
        Expected: S = (4 * 0.35) + (2 * 0.85) = 3.1
        Expected: Z_eff = 7 - 3.1 = 3.9
        """
        N = element(7)
        Z_eff = get_effective_nuclear_charge(N)
        self.assertAlmostEqual(Z_eff, 3.9, places=2,
                               msg=f"Nitrogen Z_eff should be 3.9, got {Z_eff}")

    def test_zinc(self):
        """
        Test Zinc (Z=30).
        Configuration: [Ar] 3d¹⁰ 4s²
        For outermost 4s electron:
        - Same group [4s]: 1 × 0.35 = 0.35
        - Group [3s, 3p] (n-1 s,p): 8 × 0.85 = 6.8
        - Group [3d] (n-1 d, counts as inner): 10 × 1.00 = 10.0
        - Deeper [2s, 2p, 1s]: 10 × 1.00 = 10.0
        Expected: S = 0.35 + 6.8 + 10.0 + 10.0 = 27.15
        Expected: Z_eff = 30 - 27.15 = 2.85
        """
        Zn = element(30)
        Z_eff = get_effective_nuclear_charge(Zn)
        expected_S = (1 * 0.35) + (8 * 0.85) + (10 * 1.00) + (10 * 1.00)  # 27.15
        expected_Z_eff = 30 - expected_S  # 2.85
        self.assertAlmostEqual(Z_eff, expected_Z_eff, places=2,
                               msg=f"Zinc Z_eff should be {expected_Z_eff:.2f}, got {Z_eff}")

    def test_hydrogen(self):
        """
        Test Hydrogen (Z=1).
        Configuration: 1s¹
        Expected: S = 0 (no other electrons to shield)
        Expected: Z_eff = 1 - 0 = 1.0
        """
        H = element(1)
        Z_eff = get_effective_nuclear_charge(H)
        self.assertAlmostEqual(Z_eff, 1.0, places=2,
                               msg=f"Hydrogen Z_eff should be 1.0, got {Z_eff}")

    def test_helium(self):
        """
        Test Helium (Z=2).
        Configuration: 1s²
        Expected: S = 1 * 0.30 = 0.30 (one other 1s electron)
        Expected: Z_eff = 2 - 0.30 = 1.70
        """
        He = element(2)
        Z_eff = get_effective_nuclear_charge(He)
        self.assertAlmostEqual(Z_eff, 1.70, places=2,
                               msg=f"Helium Z_eff should be 1.70, got {Z_eff}")

    def test_oxygen(self):
        """
        Test Oxygen (Z=8).
        Configuration: 1s² 2s² 2p⁴
        For outermost 2p electron:
        Expected: S = (5 * 0.35) + (2 * 0.85) = 1.75 + 1.70 = 3.45
        Expected: Z_eff = 8 - 3.45 = 4.55
        """
        O = element(8)
        Z_eff = get_effective_nuclear_charge(O)
        expected_S = (5 * 0.35) + (2 * 0.85)  # 3.45
        expected_Z_eff = 8 - expected_S  # 4.55
        self.assertAlmostEqual(Z_eff, expected_Z_eff, places=2,
                               msg=f"Oxygen Z_eff should be {expected_Z_eff:.2f}, got {Z_eff}")

    def test_sodium(self):
        """
        Test Sodium (Z=11).
        Configuration: [Ne] 3s¹
        For outermost 3s electron:
        Expected: S = (0 * 0.35) + (8 * 0.85) + (2 * 1.00) = 0 + 6.8 + 2 = 8.8
        Expected: Z_eff = 11 - 8.8 = 2.2
        """
        Na = element(11)
        Z_eff = get_effective_nuclear_charge(Na)
        expected_S = (0 * 0.35) + (8 * 0.85) + (2 * 1.00)  # 8.8
        expected_Z_eff = 11 - expected_S  # 2.2
        self.assertAlmostEqual(Z_eff, expected_Z_eff, places=2,
                               msg=f"Sodium Z_eff should be {expected_Z_eff:.2f}, got {Z_eff}")

    def test_chlorine(self):
        """
        Test Chlorine (Z=17).
        Configuration: [Ne] 3s² 3p⁵
        For outermost 3p electron:
        Expected: S = (6 * 0.35) + (8 * 0.85) + (2 * 1.00) = 2.1 + 6.8 + 2 = 10.9
        Expected: Z_eff = 17 - 10.9 = 6.1
        """
        Cl = element(17)
        Z_eff = get_effective_nuclear_charge(Cl)
        expected_S = (6 * 0.35) + (8 * 0.85) + (2 * 1.00)  # 10.9
        expected_Z_eff = 17 - expected_S  # 6.1
        self.assertAlmostEqual(Z_eff, expected_Z_eff, places=2,
                               msg=f"Chlorine Z_eff should be {expected_Z_eff:.2f}, got {Z_eff}")

    def test_iron(self):
        """
        Test Iron (Z=26).
        Configuration: [Ar] 3d⁶ 4s²
        For outermost 4s electron:
        - Same group [4s]: 1 × 0.35 = 0.35
        - Group [3s, 3p] (n-1 s,p): 8 × 0.85 = 6.8
        - Group [3d] (n-1 d, counts as inner): 6 × 1.00 = 6.0
        - Deeper [2s, 2p, 1s]: 10 × 1.00 = 10.0
        Expected: S = 0.35 + 6.8 + 6.0 + 10.0 = 23.15
        Expected: Z_eff = 26 - 23.15 = 2.85
        """
        Fe = element(26)
        Z_eff = get_effective_nuclear_charge(Fe)
        # For 4s: same shell (1 other 4s), [3s,3p] (8), [3d] (6), deeper (10)
        expected_S = (1 * 0.35) + (8 * 0.85) + (6 * 1.00) + (10 * 1.00)  # 23.15
        expected_Z_eff = 26 - expected_S  # 2.85
        self.assertAlmostEqual(Z_eff, expected_Z_eff, places=2,
                               msg=f"Iron Z_eff should be {expected_Z_eff:.2f}, got {Z_eff}")

    def test_scandium_d_orbital(self):
        """
        Test Scandium (Z=21) - testing d orbital rules.
        Configuration: [Ar] 3d¹ 4s²
        For outermost 4s electron:
        - Same group [4s]: 1 × 0.35 = 0.35
        - Group [3s, 3p] (n-1 s,p): 8 × 0.85 = 6.8
        - Group [3d] (n-1 d, counts as inner): 1 × 1.00 = 1.0
        - Deeper [2s, 2p, 1s]: 10 × 1.00 = 10.0
        Expected: S = 0.35 + 6.8 + 1.0 + 10.0 = 18.15
        Expected: Z_eff = 21 - 18.15 = 2.85
        """
        Sc = element(21)
        Z_eff = get_effective_nuclear_charge(Sc)
        # For 4s: same shell (1 other 4s), [3s,3p] (8), [3d] (1), deeper (10)
        expected_S = (1 * 0.35) + (8 * 0.85) + (1 * 1.00) + (10 * 1.00)  # 18.15
        expected_Z_eff = 21 - expected_S  # 2.85
        self.assertAlmostEqual(Z_eff, expected_Z_eff, places=2,
                               msg=f"Scandium Z_eff should be {expected_Z_eff:.2f}, got {Z_eff}")

    def test_argon(self):
        """
        Test Argon (Z=18).
        Configuration: [Ne] 3s² 3p⁶
        For outermost 3p electron:
        Expected: S = (7 * 0.35) + (8 * 0.85) + (2 * 1.00) = 2.45 + 6.8 + 2 = 11.25
        Expected: Z_eff = 18 - 11.25 = 6.75
        """
        Ar = element(18)
        Z_eff = get_effective_nuclear_charge(Ar)
        expected_S = (7 * 0.35) + (8 * 0.85) + (2 * 1.00)  # 11.25
        expected_Z_eff = 18 - expected_S  # 6.75
        self.assertAlmostEqual(Z_eff, expected_Z_eff, places=2,
                               msg=f"Argon Z_eff should be {expected_Z_eff:.2f}, got {Z_eff}")

    def test_lead(self):
        """
        Test Lead (Z=82) - testing proper handling of (n-1) d/f orbitals.
        Configuration: [Xe] 4f¹⁴ 5d¹⁰ 6s² 6p²
        For outermost 6p electron:
        - Same group (6s, 6p): 4 electrons, excluding one = 3 × 0.35 = 1.05
        - Layer (n-1=5) s,p orbitals (5s² 5p⁶): 8 × 0.85 = 6.8
        - Layer (n-1=5) d orbital (5d¹⁰): 10 × 1.00 = 10.0 (counts as inner)
        - Layers (n-2) and deeper (levels 1,2,3,4): 60 × 1.00 = 60.0
        Expected: S = 1.05 + 6.8 + 10.0 + 60.0 = 77.85
        Expected: Z_eff = 82 - 77.85 = 4.15
        """
        Pb = element(82)
        Z_eff = get_effective_nuclear_charge(Pb)
        expected_S = (3 * 0.35) + (8 * 0.85) + (10 * 1.00) + (60 * 1.00)  # 77.85
        expected_Z_eff = 82 - expected_S  # 4.15
        self.assertAlmostEqual(Z_eff, expected_Z_eff, places=2,
                               msg=f"Lead Z_eff should be {expected_Z_eff:.2f}, got {Z_eff}")

    def test_z_eff_positive(self):
        """Test that Z_eff is always positive for all elements."""
        for atomic_number in range(1, 100):
            elem = element(atomic_number)
            Z_eff = get_effective_nuclear_charge(elem)
            self.assertGreater(Z_eff, 0,
                               msg=f"Element {elem.symbol} (Z={atomic_number}) has non-positive Z_eff: {Z_eff}")

    def test_z_eff_less_than_z(self):
        """Test that Z_eff is always less than Z (shielding reduces effective charge)."""
        for atomic_number in range(2, 100):  # Skip hydrogen which has Z_eff = Z
            elem = element(atomic_number)
            Z_eff = get_effective_nuclear_charge(elem)
            self.assertLess(Z_eff, atomic_number,
                            msg=f"Element {elem.symbol} (Z={atomic_number}) has Z_eff >= Z: {Z_eff}")


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)
