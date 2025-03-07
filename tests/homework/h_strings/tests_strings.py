import unittest
from src.homework.h_strings.strings import get_hamming_distance, get_dna_complement

class TestStrings(unittest.TestCase):

    def test_get_hamming_distance(self):
        "Test Hamming Distance Calculation"
        self.assertEqual(get_hamming_distance("GACCTACTAACGGGAT", "CATCGTAATGACGGCCT"), 7)

    def test_get_dna_complement(self):
        "Test DNA Complement Calculation"
        self.assertEqual(get_dna_complement("AAAACCCGGT"), "ACCGGGTTTT")

if __name__ == "__main__":
    unittest.main()