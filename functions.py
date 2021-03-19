"""A collection of function for doing my project."""
import random


class choose_company(): #Used to break the chat into multiple small questions
    
    def __init__(self, Name, Contacts, Education, Work_Experience, Key_Skills):
        self.Name = Name
        self.Contacts = Contacts
        self.Education = Education
        self.Work_Experience = Work_Experience
        self.Key_Skills = Key_Skills
    
    def interview_begin(self):
        """Ask users to input their names
        
        Parameters
        ----------
        from self, self.name (string)
        
        Returns
        ----------
        output_1 : string
            String introducing self.name and starting the conversation
       """
        
        greetings = input("Hello, Welcome to the interview, what is your name?\n")
         
        output_1 = ("Hi " + self.Name + " Please answering the following questions!\n")
          
        return output_1
        
    def ask_contacts(self):
        """Ask users to input their contacts
        
        Parameters
        ----------
        from self, self.Contacts (string)
        
        Returns
        ----------
        output_1 : string
            String introducing self.contacts and continuing the conversation
       """
        
        a = input("Would you please give me your contacts? (Please repsonds with a str!)\n")
        
        return ("My contact is " + self.Contacts + ".")
    
    def ask_education(self):
        """Chatbot assesses users' GPA.
        
        Parameters
        ----------
        self.Education : float
            give a gpa in float
            
            
        Returns
        -------
        output_2 : string
            Delivers 1 of 4 possible statements depending on the user's GPA 
       """
        
        b = input("Would you please tell me your gpa at school? (Please repsonds with a decimal between 0.0-4.0.)\n")
        gpa = float(b)
        
        if float(b) >= 0.0 and float(b) <= 2.8:
            output_2 = print("Most companies need a higher GPA, but I will still try to match you with the right company.\n")
        elif float(b) >= 2.8 and float(b) <= 3.3:
            output_2 = print("Good! Your GPA has met most of our companies' requirements.\n")
        elif float(b) >= 3.3 and float(b) <= 4.0:
            output_2 = print("Nice! Your GPA has met all of our companies' requirements.\n")
        else:
            output_2 = print("ERROR!\n")
            
    def ask_Work_Experience(self):
        """Chatbot assesses users' work experience.
        
        Parameters
        ----------
        self.Work_Experience : string
            answer the question with "Programming", "Sales", "Engineering"
            
            
        Returns
        -------
        output_3 : string
            Delivers 1 of 4 possible statements depending on the user's work experience
       """
        
        c = input("What kind of work experience do you have? (Please repsonds with following words: Programming, Sales, Engineering)\n")
        if c == "Programming":
            output_3 = input("Nice, I think you are are better suited to work in an Internet company.\n")
        elif c == "Sales":
            output_3 = input("Nice, I think you are are better suited to work in a large market.\n")
        elif c == "Engineering":
            output_3 = input("Nice, I think you are are better suited to work in a large machine manufacturer.\n")
        
        else:
            print("ERROR!\n")
    def ask_Key_Skills(self):
        """Chatbot assesses users' key skills.
        
        Parameters
        ----------
        self.Key_Skills : string
            answer the question with "Coding", "Management", "Service oriented"
            
            
        Returns
        -------
        output_4 : string
            Delivers 1 of 4 possible statements depending on the user's work experience
       """
        
        d = input("Do you have any special skills? (Please repsonds with following words: Coding, Management, service oriented)\n")
        if d == "Coding":
            output_4 = input("Your repsonse has been recorded.\n")
        elif d == "Management":
            output_4 = input("Your repsonse has been recorded.\n")
        elif d == "service oriented":
            output_4 = input("Your repsonse has been recorded.\n")
        
        else:
            print("ERROR!\n")
    def match_company(self):
        """Chatbot gives users' final results.
        
        Parameters
        ----------
        None
            
            
        Returns
        -------
        output_5 : string
            Delivers three types of random companies results from the list
       """
        
        Internet_company_names = ["Google", "Facebook", "Bytedance", "Lenovo", "Microsoft", "Baidu", "Qualcomm", "Xiaomi"]

        large_market_names = ["Walmart", "Target", "Costco", "Tesco"]

        large_machine_manufacturer_names = ["BMW", "Ford", "Buick", "IBM", "SpaceX", "General Electric", "NXP", "Apple", "Tesla"]
        
        e = input("Please tell me again about your work experience and key skills.\n")
        
        if e == "Programming and Coding":
            output_5 = input("You would be best suited to work in " + random.choice(Internet_company_names) + ".")
        elif e == "Sales and Service oriented":
            output_5 = input("You would be best suited to work in " + random.choice(large_market_names) + ".")
        elif e == "Engineering and Management":
            output_5 = input("You would be best suited to work in " + random.choice(large_machine_manufacturer_names) + ".")
        
        else:
            print("Sorry, our system cannot help you. Have a good day!\n")

            