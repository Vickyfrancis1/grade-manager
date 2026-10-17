import unittest

def average_score(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)

def grade(score):
    if score >= 70:
        return "A"
    elif score > 60:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "F"
    
class TestGradeManager(unittest.TestCase):
    
    def test_average(self):
        self.assertEqual(average_score([60, 70, 80]), 70)
    
    def test_average_empty(self):
        self.assertEqual(average_score([]), 0)
        
    def test_grade_a_boundary(self):
        self.assertEqual(grade(70), "A")
        
    def test_grade_b_boundary(self):
        self.assertEqual(grade(60), "B")
        
    def test_grade_c_boundary(self):
        self.assertEqual(grade(50), "C")
        
    def test_grade_f(self):
        self.assertEqual(grade(49.9), "F")
        
unittest.main(exit=False)
        
    
    