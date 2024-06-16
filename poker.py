import psutil   
name = "PokerStars" 
found = any(name in p.name() for p in psutil.process_iter())
print(found)