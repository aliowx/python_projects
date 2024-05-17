from typing import Any


class Persoon:
    
    def __init__(self,name,age):
        self.name= name
        self.age = age
    
    def __del__ (self):
        print('object is being deconstructer!') 
    
    
    def __add__(self,other):
        return Persoon(self.name+other.name,self.age + other.age )
    
    
    def __repr__(self):
        return f'Name:{self.name},Aage : {self.age}'
    
    def __len__(self):
        return 10 
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print('Hi I was called!')
        
        
        
    