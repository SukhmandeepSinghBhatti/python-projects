from playsound import playsound
while(True):
  print('Press "Q" for exit.')
  print(" Choose from this list:- \n 1. 2 Ghore \n 2. Akad \n 3.Shoot Da Order \n 4. We Rollin \n 5. BANDOOK \n 6. Tora \n ")
  a = input(("Enter the name of song you want to play: "))
  if "2 Ghore" in a:
     playsound("2 Ghore.mp3")
  elif "Akad" in a:
     playsound("Akad.mp3")
  elif "Shoot Da Order" in a:
     playsound("Shoot Da Order.mp3")
  elif "We Rollin" in a:
       playsound("We Rollin.mp3")
  elif "BANDOOK" in a:
      playsound("BANDOOK.mp3")
  elif "Tora" in a:
      playsound("Tora.mp3")
  elif "Q" in a:
      exit()     
     


