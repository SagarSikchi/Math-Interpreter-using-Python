from nodes import *
from values import Number

class Interpreter:
    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)
        return method(node)

    def visit_NumberNode(self, node):
        try:   
            return Number(node.value)
        except:
            # raise Exception("Error in Calculation")
            return "Error in Calculation"

    def visit_AddNode(self, node):
        try:   
            return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)
        except:
            # raise Exception("Error in Calculation")
            return "Error in Calculation"

    def visit_SubtractNode(self, node):
        try:   
            return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)
        except:
            # raise Exception("Error in Calculation")
            return "Error in Calculation"

    def visit_MultiplyNode(self, node):
        try:   
            return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)
        except:
            # raise Exception("Error in Calculation")
            return "Error in Calculation"

    def visit_DivideNode(self, node):
        try:   
            return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
        except:
            # raise Exception("Error in Calculation")
            return "Error in Calculation"
    def visit_ModuloNode(self, node):
        try:   
            return Number(self.visit(node.node_a).value % self.visit(node.node_b).value)
        except:
            # raise Exception("Error in Calculation")
            return "Error in Calculation"

    def visit_ExponentNode(self, node):
        try:   
            return Number(self.visit(node.node_a).value ** self.visit(node.node_b).value)
        except:
            # raise Exception("Error in Calculation")
            return "Error in Calculation"
    
    def visit_PlusNode(self, node):
        try:   
            return self.visit(node.node_t).value
        except:
            # raise Exception("Error in Calculation")
            return "Error in Calculation"

    def visit_MinusNode(self, node):
        try:   
           return Number(-self.visit(node.node_t).value)
        except:
            # raise Exception("Error in Calculation")
            return "Error in Calculation"