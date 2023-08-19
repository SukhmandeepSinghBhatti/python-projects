from playsound import playsound
while(True):
 print(" Choose from this list:- 1. 2 Ghore, 2. Akad, 3.Shoot Da Order, 4. We Rollin, 5. BANDOOK, 6. Tora,")
 a = input(("Enter the name of song you want to play: "))
 if "2 Ghore" in a:
     playsound("D:\\Coding\\python projects\\music player\songs\\2 Ghore.mp3")
 elif "Akad" in a:
     playsound("D:\\Coding\\python projects\\music player\songs\\Akad.mp3")
 elif "Shoot Da Order" in a:
     playsound("D:\\Coding\\python projects\\music player\songs\\Shoot Da Order.mp3")
 elif "We Rollin" in a:
       playsound("D:\\Coding\\python projects\\music player\songs\\We Rollin.mp3")
 elif "BANDOOK" in a:
      playsound("D:\\Coding\\python projects\\music player\songs\\BANDOOK.mp3")
 elif "Tora" in a:
      playsound("D:\\Coding\\python projects\\music player\songs\\Tora.mp3")
 elif "Q" in a:
      exit()     
     


