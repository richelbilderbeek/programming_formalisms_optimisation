"""Test the functions in src.pfoptimisation_richelbilderbeek.lekberg."""
import unittest

from src.pfoptimisation_richelbilderbeek.lekberg import (
    align_bf,
    align_fast,
    alignment_score,
    all_alignments,
    needleman_wunsch,
    print_alignment,
)


class TestLekman(unittest.TestCase):

    """Class to test the functions in 'lekman.py'.
    
    These tests are taken from the website at 
    https://johnlekberg.com/blog/2020-10-25-seq-align.html.

    No tests have been added to preserve the originality of the code.
    """

    def test_align_bf(self):
        """Test the 'align_bf' function."""
        created = align_bf("CAT", "CT")
        expected = [(0, 0), (1, None), (2, 1)]
        self.assertEqual(created, expected)

    def test_align_fast(self):
        """Test the 'align_fast' function."""
        created = align_fast("CAT", "CT")
        expected = [(0, 0), (1, None), (2, 1)]
        self.assertEqual(created, expected)

    def test_alignment_score(self):
        """Test the 'alignment_score' function."""
        x = "CAT"
        y = "CT"
        alignment = [(0, 0), (1, None), (2, 1)]
        score = alignment_score(x, y, alignment)
        expected_score = 1.0
        self.assertEqual(score, expected_score)

    def test_all_alignments(self):
        """Test the 'all_alignments' function."""
        n_alignments = len(list(all_alignments("CAT", "CT")))
        n_alignments_expected = 25
        self.assertEqual(n_alignments, n_alignments_expected)

    def test_needleman_wunsch(self):
        """Test the 'needleman_wunsch' function."""
        expected = [(0, 0), (1, None), (2, 1)]
        created = needleman_wunsch("CAT", "CT")
        self.assertEqual(created, expected)

    def test_print_alignment(self):
        """Test the 'print_alignment' function."""
        x = "CAT"
        y = "CT"
        for alignment in all_alignments(x, y):
            print_alignment(x, y, alignment)
