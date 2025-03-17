# escape sequence (always comes in " " ' ')
"""
\n -> new line
\t -> tab 
\\ -> \
\" -> "
\' -> '
\b -> backspace
"""
print("hello world \n good bye\n  we are learning python")
print(" HELLO WORLD\T WE ARE LEARNINH PYTHON GOOD BYE ")
print(" HELLO WORLD\T WE ARE LEARNINH PYTHON\n\n GOOD BYE ")
print(" HELLO WORLD\t WE ARE LEARNINH PYTHON\t\t GOOD BYE ")
print("my name is soni \n my age is 20\n my gender is female)")
# output :- my name is a\nirudh
print("my name is a\\nirudh")
# output :- my name is a\\nirudh
print("my name is a\\\\nirudh")
# output :- my name is "anirudh
print('my name is "anirudh"')
# output:- my name is 'anirudh'
print("my name is 'anirudh'")
# output :- my name is "anirudh"
print('my name is a"nirudh')


# a"\\"xyz'"\
print('# a"\\\\"xyz\'"\\')
