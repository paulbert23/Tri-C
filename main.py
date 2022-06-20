
# Online Python - IDE, Editor, Compiler, Interpreter



class Shark: # defines a class called shark
    def __init__(self, name): # the first definition of the class shark.  The constructor method.  Uses a name variable that will be used to assign names to objects. 
        self.name = name # passes name as a parameter and sets self.name equal to name. 

    def swim(self): # defines the method swim, which is a special function of the class shark, because it is indented under the class.
        print(self.name + " is swimming.") # prints the line "'self.name' is swimming."

    def be_awesome(self): # defines the method be_awesome, which is a special function of the class shark, because it is indented under the class.
        print(self.name + " is being awesome.") # prints the line "'self.name' is being awesome."
    
    def be_scary(self): # defines the method be_scary, which is a special function of the class shark, because it is indented under the class.
        print(self.name + " is scary.") # prints the line "'self.name' is scary."

def main(): # Sets name of the shark object.
    sammy = Shark("Sammy") # Names one object of the class shark as sammy and equal to "Sammy".
    sammy.be_awesome() # Attaches the be.awesome method to sammy.
    stevie = Shark("Stevie") # Names one object of the class shark as stevie and equal to "Stevie".
    stevie.swim() # Attaches the swim method to stevie.
    paul = Shark("Paul") # Names one object of the class shark as paul and equal to "Paul".
    paul.be_scary() # Attaches the be_scary method to paul. 

if __name__ == "__main__": # States that if a name = one of the defined object names, execute the code.
  main()