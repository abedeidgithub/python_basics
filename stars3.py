''' 

  By Eng.Abed Eid 
  
'''
'''
          *
         **
        ***
      *****
     ******
    *******
   ********
 **********
***********

'''
# -----------------------------------code ----------------------

i = 1
while i <= 10:
    j = 10
    while j <= 1:
        if j >= i:
            print " ",
        else:
            print "*",
        j -= 1
    print ""
    i += 1
