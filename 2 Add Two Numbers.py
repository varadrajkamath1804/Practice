def addTwoNumbers(l1, l2):
    a = int(''.join(map(str,l1)))
    b = int(''.join(map(str,l2)))
 
    reva = reverse_number(a)
    revb =reverse_number(b)
    print("Rev a",reva)
    print("Rev b",revb)

    sum= reva + revb
    print("reva + revb",sum)

    revsum=reverse_number(sum)
    output= list(map(int,str(revsum)))
    print("OP",output)
    return output


def reverse_number(n):
    reversed_number=0
    while n>0:
        digit = n % 10
        reversed_number = reversed_number * 10 + digit
        n = n//10
    return reversed_number


l1 = [2,4,3]
l2 = [5,6,4]
result= addTwoNumbers(l1,l2)
print("Final",result)

