a=int(input("enter the number"))
s=0
t=a
b=len(str(a))
for i in range(b):
    x=(a%10)**b
    s=s+x
    a=a//10
if s==t:
    print("armstrong",t)
else:
    print("not armstrong",t)