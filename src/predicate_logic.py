"""
Contains definitions of FORMULA format
"""


class FORMULA:
    """
    Represents a formula in predicat logic.
    """

    def __init__(self) -> None:
        pass

    def find_unit_literal():
        raise NotImplementedError 

    def unit_propagate(unit_literal):
        raise NotImplementedError 

    def find_pure_literal():
        raise NotImplementedError 

    def pure_literal_assign(pure_literal):
        raise NotImplementedError 

    def is_empty():
        raise NotImplementedError 

    def find_empty_clause():
        raise NotImplementedError 

class TRUE(FORMULA):
    def __init__(self) -> None:
        super().__init__()

class FALSE(FORMULA):
    def __init__(self) -> None:
        super().__init__()

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

    def find_unit_literal():
        pass

    def unit_propagate(unit_literal):
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
    def __new__(cls, f : FORMULA):
        #  transforms NEG(NEG(f)) to f
        if isinstance(f, NEG):
            return f.f 
        return super().__new__(cls)
    
    def __init__(self, f: FORMULA) -> None:
        '''
        Creates an object that represents NOT f
        '''
        self.f = f 
    def __hash__(self) -> int:
        return hash(str(self))
    

            
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, NEG):
            if self.f == value.f:
                return True
        return False
    def __str__(self) -> str:
        return f'!({str(self.f)})'
    def __repr__(self):
        return f'!({repr(self.f)})' 


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
        self.id = id
    
    # VARIABLES should be in 1:1 correspondance with ids. 
    def __eq__(self, value: object) -> bool:
        if isinstance(value, VAR):
            if value.id == self.id:
                return True
        return False

    def __str__(self) -> str:
        return 'v' + str(self.id)
    def __repr__(self):
        return 'v' +  str(self.id)
    def __hash__(self) -> int:
        return hash(str(self))


