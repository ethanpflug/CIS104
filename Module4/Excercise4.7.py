score = input("Enter Score:")
scr = float(score)

def computegrade(score):
    if 0.0<scr<0.6:
        print("F")
    elif 0.6<=scr<0.7:
        print("D")
    elif 0.7<=scr<0.8:
        print("C")
    elif 0.8<=scr<0.9:
        print("B")
    elif 0.9<=scr<=1.0:
        print("A")
    else:
        print("Error")
computegrade(score)
