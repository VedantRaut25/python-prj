class Employee:
    def __init__ (
            self,
            designation : str = 'Developer',
            frontend : bool = False,
            backend : bool = False
    ):
        self.designation = designation
        self.frontend = frontend
        self.backend = backend

    def __repr__ (self):
        return '{}'.format(self.designation)

    def verifier(self):
        Dev = {
            (True, True): "He is a Fullstack Dev",
            (True, False): "He is a Frontend Dev",
            (False, True): "He is a Backend Dev",
            (False, False): "He is a Not a developer"
        }
        return Dev.get((self.frontend, self.backend), "Not a developer")

if __name__ == '__main__':
    firstEmployee = Employee()
    print(firstEmployee.verifier())
    
    secondEmployee = Employee(frontend=True)
    print(secondEmployee.verifier())
    
    thirdEmployee = Employee(backend=True)
    print(thirdEmployee.verifier())
    
    fourthEmployee = Employee(frontend=True, backend=True)
    print(fourthEmployee.verifier())
