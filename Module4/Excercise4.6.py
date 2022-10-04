def computepay(h, r):
    if h>40:
        reg = r*h
        otp = (h-40.0)*(r*0.5)
        tp = (reg + otp)
    else:
        tp = (r*h)
    return tp    

hrs = input("Enter Hours:")
fh = float(hrs)

rte = input("Enter Rate:")
fr = float(rte)

p = computepay(fh, fr)
print("Pay", p)
