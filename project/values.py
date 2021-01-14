from dataclasses import dataclass

@dataclass
class Number:
    value: float
    
    def __repr__(self):
        try:   
            return f"{self.value}"
        except:
            # raise Exception("Error in Calculation")
            return "Error in Value Calculation"
        