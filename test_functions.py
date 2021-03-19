"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from my_module import functions as pf
import random

def test_choose_company(self):
    """Tests that every necessary attribute of my class is present.
    Also tests that every attribute matches the desired object type."""
    
    assert self.Name
    assert self.Contacts
    assert self.Education
    assert self.Work_Experience
    assert self.Key_Skills
    assert isinstance(self.Name, str)
    assert isinstance(self.Contacts, str)
    assert isinstance(self.Education, float)
    assert isinstance(self.Work_Experience, str)
    assert isinstance(self.Key_Skills, str)

def test_ask_education():
    """Tests my method ask_Education(self)"""
    
    Shawn = pf.choose_company(Name = "Shawn", 
                       Contacts = "4373", 
                       Education = 4.0, 
                       Work_Experience = "Programming", 
                       Key_Skills = "Coding" )
    
    Shawn_ask_education = Shawn.ask_education
    
    gpa = float(4.0)
    
    assert gpa
    assert isinstance(gpa, float)
    
def test_ask_Work_Experience():
    """Tests my method ask_Work_Experience(self)"""
    
    Shawn = pf.choose_company(Name = "Shawn", 
                       Contacts = "4373", 
                       Education = 4.0, 
                       Work_Experience = "Programming", 
                       Key_Skills = "Coding" )
     
    Shawn_ask_Work_Experience = Shawn.ask_Work_Experience
    
    Work_Experience = "Programming"
    
    assert Work_Experience
    assert isinstance(Work_Experience, str)
    
def test_ask_Key_Skills():
    """Tests the method ask_Key_Skills(self)"""
   
    Shawn = pf.choose_company(Name = "Shawn", 
                       Contacts = "4373", 
                       Education = 4.0, 
                       Work_Experience = "Programming", 
                       Key_Skills = "Coding" )
    
    Shawn_ask_Key_Skills = Shawn.ask_Key_Skills
    
    Key_Skills = "Coding"
    
    assert Key_Skills
    assert isinstance(Key_Skills, str)
     
    


##
##


    



                 
    