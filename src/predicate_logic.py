"""
Contains definitions of FORMULA format
"""


class FORMULA:
    """
    Represents a formula in predicat logic.
    """

    def __init__(self) -> None:
        pass

    def find_unit_clause():
        raise NotImplementedError 

    def unit_propagate(unit_clause):
        raise NotImplementedError 

    def find_pure_literal():
        raise NotImplementedError 

    def pure_literal_assign(pure_literal):
        raise NotImplementedError 

    def is_empty():
        raise NotImplementedError 

    def find_empty_clause():
        raise NotImplementedError 

class CON(FORMULA):
    """
    Represents conjunction (logical and) in predicate logic. 
    """

    def __init__(self, left: FORMULA, right: FORMULA) -> None:
        '''
        Creates a formula `left AND right`
        '''
        self.left = left
        self.right = right 

    def find_unit_clause():
        pass

    def unit_propagate(unit_clause):
        pass

    def find_pure_literal():
        pass

    def pure_literal_assign(pure_literal):
        pass

    def is_empty():
        pass

    def find_empty_clause():
        pass


class DIS(FORMULA):
    """
    implementira ali
    """

    def __init__(self, f: FORMULA, g: FORMULA) -> None:
        pass


class NEG(FORMULA):
    """
    implementira ali
    """

    def __init__(self, f: FORMULA) -> None:
        '''
        Creates an object that represents NOT f
        '''
        self.f = f 


class VAR(FORMULA):
    """
    implementira ali
    """

    def __init__(self, id : int) -> None:
        '''
        Creates object that represents variable.

        Parameters
        ---------
        `id` : integer (or any other object), that identifies the variable. VAR(1) always represents the same variable 1.  
        '''
        pass


