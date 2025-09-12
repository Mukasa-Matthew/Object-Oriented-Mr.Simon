class Profile:
   
    def __init__(self, name, favorite_language, hobby, tech_stack, github_username, fun_fact):
       

    
        """         
        name (string): name of a person
        favorite_language (string): favorite programming language
        hobby (string): hobby
        tech_stack (list): List of tools/technologies 
        github_username (str): GitHub username
        fun_fact (str): Something playful about me
        """


        # Store all the information passed to this Profile object
        self.name = name
        self.favorite_language = favorite_language
        self.hobby = hobby
        self.tech_stack = tech_stack
        self.github_username = github_username
        self.fun_fact = fun_fact
    



    # This Method prints a friendly introduction with my name, favorite language, and hobby
    def introduce(self):

        print(f"Hi, I'm {self.name}. I love {self.favorite_language} and my hobby is {self.hobby}.")
    


    # This display all technologies in a numbered list
    def show_stack(self):
        
        # Prints a title with the person's name
        print(f"\n{self.name}'s Tech Stack:")
        # Loop through each technology stack and number them starting from 1 according to what i included in the list 
        for i, tool in enumerate(self.tech_stack, 1):
            print(f"{i}. {tool}") 
    


        
    # this creates and return the GitHub profile URL
    def github_link(self):
       
        # Return the complete GitHub URL using the username
        return f"https://github.com/{self.github_username}"

# This section only runs when we run this file directly (not when importing)
if __name__ == "__main__":
    
    # This creates a new Profile object with my personal information
    my_profile = Profile(
        name="Matthew",
        favorite_language="Javascript",
        hobby="painting",
        tech_stack=["Python", "Django", "Git", "VS Code", "PostgreSQL", "Mysql"],
        github_username="Mukasa-Matthew",
        fun_fact="I love technology soo much, and am a quiet person!"
    )
    
  
    # This calls all the methods to demonstrate what the Profile can do
    my_profile.introduce()  # Prints the  introduction
    my_profile.show_stack()  # Shows my tech stack
    print(f"\nGitHub Profile: {my_profile.github_link()}")  # Shows my GitHub URL
    print(f"\nFun Fact: {my_profile.fun_fact}")  # Shows my fun fact