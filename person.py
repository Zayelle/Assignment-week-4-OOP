class person:
      def __init__(self, name, age, gender):
            self.name= name
            self.age= age
            self.gender= gender

      def introduce(self): 
            print(f"Hello...My name is {self.name}.")
            print(f"l am {self.age} years old. ")
            print(f"l am {self.gender}.")

# Create an instance of the person
person1 = person("Adrian",3,"Male")  
person2 = person("Audrey", 12, "Female")
#Call the introduce method to display the person's information
person1.introduce()


