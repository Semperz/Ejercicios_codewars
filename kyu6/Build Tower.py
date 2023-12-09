#Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

# example, a tower with 3 floors looks like this:

#[
#  "  *  ",
# " *** ",
#  "*****"
#]
#And a tower with 6 floors looks like this:

#[
#  "     *     ",
#  "    ***    ",
#  "   *****   ",
# "  *******  ",
#  " ********* ",
#  "***********"
#]


#1st try
def tower_builder(npisos):
    solucion=[]
    for piso_actual in range(npisos):
        solucion.append(" "*(npisos-piso_actual-1)+"*"*piso_actual+"*"+"*"*piso_actual+" "*(npisos-piso_actual-1))
    return solucion

#Refactor
def tower_builder(npisos):
    return [(" "*(npisos-piso_actual-1)+"*"*piso_actual+"*"+"*"*piso_actual+" "*(npisos-piso_actual-1)) for piso_actual in range(npisos)]