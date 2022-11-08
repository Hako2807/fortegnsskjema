import math
import pg
from calculations import Calculate


def main():
    print("\n———————————————————————————————————————————")
    calc = Calculate()
    #calc.make_function(calc)
    #calc.calculate_fortegn(calc, calc.factorize_second_degree(calc))

    disp = pg.Display(700, 500, calc)
    while True:
        disp.tick()
    

main()