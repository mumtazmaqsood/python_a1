
#this file is call function_modules.py file

#import entire file
import function_modules

#import specific function and given short name to that funciton mp
from function_modules import make_pizza as mp

function_modules.make_pizza(10, 'test1', 'test2')
function_modules.make_pizza(20, 'test1', 'test2', 'module')