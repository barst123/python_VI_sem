def licznik_nonlocal():
   licznik=0
   def liczenie():
       nonlocal licznik
       licznik+=1
       return licznik
   return liczenie