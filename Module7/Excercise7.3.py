fname = input('Input file name: ')
if fname == 'na na boo boo':
    print("NA NA NA BOO BOO TO YOU - You have been punk'd")
else:
    try:
        with open(fname) as finame
    except:
        print('File could not be opened')
        quit()
    count = 0
    for line in fname:
        if line.startswith('Subject:'):
            count = count + 1
    print('There were', count, 'subject lines in', fname)
