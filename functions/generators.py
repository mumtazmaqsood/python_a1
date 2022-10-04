
def square_no(nos):
    result = []
    for i in nos:
        result.append(i*i)
    return result

print(square_no([1,2,3,4]))
#above function is simple function, its calculating sq of the no

def sq_no(nos):
    for i in nos:
        yield (i*i)
my_no = sq_no([1,2,3,4,5])
print(my_no)
print(next(my_no))