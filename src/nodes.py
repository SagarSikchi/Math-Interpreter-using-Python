from dataclasses import dataclass

@dataclass
class NumberNode:
    value: float

    def __repr__(self):
        try:   
            return f"{self.value}"
        except:
            # raise Exception("Error in Calculation")
            return "Error in TreeNode"

@dataclass
class AddNode:
    node_a: any
    node_b: any

    def __repr__(self):
        try:   
            return f"({self.node_a}+{self.node_b})"
        except:
            # raise Exception("Error in Calculation")
            return "Error in TreeNode"

@dataclass
class SubtractNode:
    node_a: any
    node_b: any

    def __repr__(self):
        try:   
            return f"({self.node_a}-{self.node_b})"
        except:
            # raise Exception("Error in Calculation")
            return "Error in TreeNode"

@dataclass
class MultiplyNode:
    node_a: any
    node_b: any

    def __repr__(self):
        try:   
            return f"({self.node_a}*{self.node_b})"
        except:
            # raise Exception("Error in Calculation")
            return "Error in TreeNode"
    
@dataclass
class DivideNode:
    node_a: any
    node_b: any

    def __repr__(self):
        try:   
            return f"({self.node_a}/{self.node_b})"
        except:
            # raise Exception("Error in Calculation")
            return "Error in TreeNode"

@dataclass
class ModuloNode:
    node_a: any
    node_b: any

    def __repr__(self):
        try:   
            return f"({self.node_a}%{self.node_b})"
        except:
            # raise Exception("Error in Calculation")
            return "Error in TreeNode"

@dataclass
class ExponentNode:
    node_a: any
    node_b: any

    def __repr__(self):
        try:   
            return f"({self.node_a}^{self.node_b})"
        except:
            # raise Exception("Error in Calculation")
            return "Error in TreeNode"

@dataclass
class PlusNode:
    node_t: any  

    def __repr__(self):
        try:   
            return f"(+{self.node})"
        except:
            # raise Exception("Error in Calculation")
            return "Error in TreeNode"

@dataclass
class MinusNode:
    node_t: any

    def __repr__(self):
        try:   
            return f"(-{self.node})"
        except:
            # raise Exception("Error in Calculation")
            return "Error in TreeNode"

