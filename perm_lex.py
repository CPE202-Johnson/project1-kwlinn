#string -> list of strings
#generate all permutations of the characters in a string
#import sys

def perm_gen_lex(input):
    result = []
    if len(input) == 0:
        return result
    if len(input) == 1:
        result.append(input)
    else: 
        for character in input: #loop through every letter
            remaining_string = input.replace(character, '', 1) #a string of all the letters except the current one
            
            x = perm_gen_lex(remaining_string) #x is a list of all permutations of this remaining_string
            
            for chr in x: #then for each of those permutations, we prepend the current character in the outer loop
                result.append(character + chr)
                
        #     result = list(dict.fromkeys(result)) #removes duplicates from the list
        # result.sort()
    return result
    
# print(perm_gen_lex(' '.join(sys.argv[1:])))