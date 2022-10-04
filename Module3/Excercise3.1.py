hrs = input("Enter Hours:")
h = float(hrs)

rte = input("Enter Rate:")
r = float(rte)

if h>40.0:
    reg = r*h
    otp = (h-40.0)*(r*0.5)
    tp = (reg + otp)
    print(tp)
else:
    tp = (r*h)
    print(tp)
