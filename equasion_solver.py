from sympy import *

try:
    from ipywidgets import interact
except ImportError:
    print("interact is not supported not in ipython notebook")

ARITHMETIC_OPERATIONS = ['+', '=', '-', '*', '/', '%', '!', '**']


def is_symbol(symbol_str):
    """
    check if string is sepoesd to be symbols
    the current define to a symbols is something which does not contains:
        () - this represent functions
        only digits - represent number
    :return: True if is symbols, false if not
    """
    if symbol_str[0].isdigit():
        return False

    if symbol_str.find('(') != -1 or symbol_str.find('(') != -1:
        return False

    if symbol_str in ARITHMETIC_OPERATIONS:
        return False

    return True


class Equation:

    def __init__(self, equation_string, interact_range=(-1000.0, 1000.0)):
        """
        :param equation_sring:
            string which represent equation
            can contains symbols, number, math operations.

            It must contains a "=" sign for separating between the equation sides
        """

        self._equation_string = equation_string
        self.interact_range = interact_range
        self._add_symbols_to_globals()
        self._init_equation()

    def _init_equation(self):
        # print("init")
        self._left_side_string, self._right_side_string = self._equation_string.split("=")
        self._left_side = eval(self._left_side_string)
        self._right_side = eval(self._right_side_string)

    def prepare_equation(self, var_to_solve, equation_params):
        del equation_params[var_to_solve]

        left_side = self._left_side
        right_side = self._right_side

        if isinstance(self._left_side, Expr):
            left_side = self._left_side.subs(equation_params)

        if isinstance(self._right_side, Expr):
            right_side = self._right_side.subs(equation_params)

        return left_side, right_side

    def update_equation(self, var_to_solve, **equation_params):
        left_side, right_side = self.prepare_equation(var_to_solve, equation_params)
        return self.solve(var_to_solve, left_side, right_side)
        # return equation_params
        # return self.solve(var_to_solve)

    def solve(self, var_to_solve, left_side, right_side):
        """
        init the symbols for symay equation solver
        :return:
        """
        # print("solve")

        eq = Eq(
            left_side,
            right_side
        )
        print('solve eq: ', eq)

        return solve(eq, var_to_solve)

    def _add_symbols_to_globals(self):
        self._splited_symbols = self._equation_string.split(' ')
        sympy_symbols = symbols(self._equation_string)

        # for sym in sympy_symbols:
        #     print(sym, type(sym))

        dict_symbols = dict(zip(self._splited_symbols, sympy_symbols))
        print("dict_symbols: ", dict_symbols)

        globals().update(dict_symbols)

    def generate_interacts(self):
        self._symbols_for_interact = filter(is_symbol, self._splited_symbols)
        symbols_for_interact_dict = {}

        var_to_solve_list = list(self._symbols_for_interact)
        # print("v", var_to_solve_list)

        # add the
        for sym in var_to_solve_list:
            symbols_for_interact_dict[sym] = self.interact_range

            # symbols_for_interact_dict["solve_for_" + sym] = False
        self.interact = interact(self.update_equation, var_to_solve=var_to_solve_list, **symbols_for_interact_dict)
