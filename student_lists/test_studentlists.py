"""
Practice using

 assertTrue
 assertFalse
 assertIsNone
 assertIsNotNone
 assertIn
 assertNotIn

"""

from re import fullmatch
from studentlists import ClassList, StudentError
from unittest import TestCase

class TestStudentLists(TestCase):

    def test_add_student_check_student_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        self.assertIn('Test Student', test_class.class_list)

        test_class.add_student('Another Test Student')
        self.assertIn('Test Student', test_class.class_list)
        self.assertIn('Another Test Student', test_class.class_list)


    def test_add_student_already_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        with self.assertRaises(StudentError):
            test_class.add_student('Test Student')


    ## TODO write a test that adds and removes a student, 
    # and asserts the student is removed. Use assertNotIn
    def test_add_remove_student_ensure_removed(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        test_class.remove_student('Test Student')
        self.assertNotIn('Test Student', test_class.class_list)


    ## TODO write a test that adds some example students, 
    # then removes a student not in the list, and asserts a StudentError is raised
    def test_removing_student_from_populated_list_raises_student_error(self):
        test_class =ClassList(4)
        test_class.add_student('Jessie ')
        test_class.add_student('Sofia')
        with self.assertRaises(StudentError):
            test_class.remove_student('Ana')

    ## TODO write a test that removes a student from an 
    # empty list, and asserts a StudentError is raised



    def test_is_enrolled_when_student_present(self):
        test_class = ClassList(2)
        test_class.add_student('Snoop Dogg')
        test_class.add_student('Martha Stewart')
        self.assertTrue(test_class.is_enrolled('Snoop Dogg'))
        self.assertTrue(test_class.is_enrolled('Martha Stewart'))


    def test_is_enrolled_empty_class_list(self):
        test_class = ClassList(2)
        self.assertFalse(test_class.is_enrolled('Snoop Dogg'))


    ## TODO write a test that adds some example students to a test class,
    ## then, call is_enrolled for a student who is not enrolled. 
    # Use assertFalse to verify is_enrolled returns False.

    def test_is_enrolled_returns_false_if_student_not_enrolled(self):
        test_class = ClassList(4)
        test_class.add_student('Example 1')
        test_class.add_student('Example 2')
        test_class.add_student('Example 3')
        example_4_is_enrolled = test_class.is_enrolled('Exampled 4') # not there, expect False
        self.assertFalse(example_4_is_enrolled)

    def test_string_with_students_enrolled(self):
        test_class = ClassList(2)
        test_class.add_student('Taylor Swift')
        test_class.add_student('Kanye West')
        self.assertEqual('Taylor Swift, Kanye West', str(test_class))


    def test_string_empty_class(self):
        test_class = ClassList(2)
        self.assertEqual('', str(test_class))


    def test_index_of_student_student_present(self):
        test_class = ClassList(3)
        test_class.add_student('Harry')
        test_class.add_student('Hermione')
        test_class.add_student('Ron')

        self.assertEqual(1, test_class.index_of_student('Harry'))
        self.assertEqual(2, test_class.index_of_student('Hermione'))
        self.assertEqual(3, test_class.index_of_student('Ron'))

        # This assert passes, but it's redundant - the first assert statement will fail if
        # the method call returns None
        self.assertIsNotNone(test_class.index_of_student('Harry'))


  
    ## TODO write a test for index_of_student when the class_list list is empty.  
    # Assert index_of_student returns None for a student if the list is empty. 
    # use assertIsNone.
    def test_index_of_student_classlist_is_empty(self):
        test_class = ClassList(3)
        index = test_class.index_of_student()
        self.assertIsNone(index)
   
 
    ## TODO write another test for index_of_student. In the case when the 
    # class_list is not empty but has some students.
    # assert that searching for a student name that is not in the list, returns None.
    def test_index_of_student_classlist_is_not_empty_but_has_students(self):
        test_class = ClassList(3)
        test_class.add_student('Jessie')
        test_class.add_student('Sofia')
        test_class.add_student('JAIMY')
        index = test_class.index_of_student('Test Student')
        self.assertIsNone(index)
   
    ## TODO write a test for your new is_class_full method when the class is full. 
    # use assertTrue.
    def test_classfull_is_full(self):
        test_class = ClassList(3)
        test_class.add_student('Jessie')
        test_class.add_student('Sofia')
        test_class.add_student('Ana')
        index = test_class.is_class_full()
        self.assertTrue(index)
    
    ## TODO write a test for your new is_class_full method for when is empty, 
    # and when it is not full. Use assertFalse.
    def test_classfull_is_empty(self):
        test_class = ClassList(2)
        index = test_class.is_class_full()
        self.assertFalse(index)
        test_class.add_student('Jessie')
        index = test_class.is_class_full()
        self.assertFalse(index)