print("String operations are one of the most common operations used in python. These operations allow you to do many different things to sections of text within your code. One of the most common string operations is the strip operation. The string operation removes white space characters within a string of code. There are also the lstrip and rstrip commands which will remove white space characters either on the right or the left of a string. Another common string command is the replace command. replace will return a copy of a string of code with all the occurences of a defined old part of a string to a defined new part of the string. For example, replacing all instances of the word apple with the word banana in a string."

      
#example of str.strip 
      banana = '  banana  '.strip()
      print(banana)
     
#example of str.replace
        apples = ' apples '.replace('pp','oo')
        print(apples)
