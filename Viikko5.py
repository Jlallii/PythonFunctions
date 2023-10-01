# template
import tkinter as tk
import winsound
import time
from PIL import Image, ImageTk
import numpy as np
import os
import threading

ikkuna=tk.Tk()
ikkuna.title("Exercise 5")
ikkuna.geometry("700x700")

autiosaari_image=Image.open(os.path.join('KOULU\Python','autiosaari.png'))
print(autiosaari_image)
width, height = autiosaari_image.size

new_width = width // 2
new_height = height // 2

resized_autiosaari_image = autiosaari_image.resize((new_width, new_height))
resized_autiosaari_image.save("autiosaari.png")
autiosaari_image.close()
autiosaari_photo=ImageTk.PhotoImage(resized_autiosaari_image)

sivilisaatio_image=Image.open(os.path.join('KOULU\Python','sivilisaatio.png'))
print(sivilisaatio_image)
width, height = sivilisaatio_image.size

new_width = width // 2
new_height = height // 2

resized_sivilisaatio_image = sivilisaatio_image.resize((new_width, new_height))
resized_sivilisaatio_image.save("sivilisaatio.png")
sivilisaatio_image.close()
sivilisaatio_photo=ImageTk.PhotoImage(resized_sivilisaatio_image)

apina_image=Image.open(os.path.join('KOULU\Python','Apina.png'))
print(apina_image)
apina_photo=ImageTk.PhotoImage(apina_image)

ship_image=Image.open(os.path.join('KOULU\Python','Ship.png'))
print(ship_image)
ship_photo=ImageTk.PhotoImage(ship_image)

# add five buttons to the top line of the window
koristetta=tk.Label(ikkuna,text="").grid(row=0,column=0)
point_button=[]
for i in range(5):
    button_temp=tk.Button(ikkuna,text="Points: "+str(i+1),padx=40)
    button_temp.grid(row=0,column=i+1)
    point_button.append(button_temp)
def i_suppose_i_have_earned_so_much_points(amount_of_points):
    for i in range(5):
        point_button[i].configure(bg='gray')
    time.sleep(1)    
    for i in range(amount_of_points):
        point_button[i].configure(bg='green')
        winsound.Beep(440+i*100,500)

class apinaE:

    apinaE_survived_count = 0 # a counter to keep track of how many apinaE's have been sent
    arrived_wordE_list = []

#create a function that gives random one word from hätäviesti to a apina.
    def word_for_apinaE():
        print("ApinaE are given a word from hätäviesti")
        hätäviesti = "Ernesti ja Kernesti tässä terve! Olemme autiolla saarella, ja voisitteko tulla sieltä sivistyksestä joku hakemaan meidät pois! Kiitos!"
        sanat = hätäviesti.split()
        apinaE_sana = sanat[np.random.randint(0,len(sanat))]
        print("ApinaE's word is: "+apinaE_sana)
        return apinaE_sana
    
    # function for sending apina from autiosaari to sivilisaatio
    def send_apinaE():
        apinaE_sana = apinaE.word_for_apinaE()
        apinaE_image=tk.Label(ikkuna,image=apina_photo)
        print("ApinaE is sent from autiosaari to sivilisaatio")
        sivilisaatio_x = 550
        sivilisaatio_y = 250
        duration = 100
        start_x = 50
        start_y = 250
        apinaE_aani = np.random.randint(300,3000)
        sound_file = "KOULU\Python\swim.wav"
        sound_file2= "KOULU\Python\Failure.wav"
        for i in range(duration):
            new_x = start_x + (sivilisaatio_x - start_x) * (i / duration)
            new_y = start_y + (sivilisaatio_y - start_y) * (i / duration)

            new_x = 75+i*5
            new_y = 240+np.random.randint(-10,10)
            apinaE_image.place(x=new_x, y=new_y)
            winsound.Beep(apinaE_aani,100)
            ikkuna.update()
            time.sleep(0.1)

            #theres a 1% chance that apinaE will drown
            if np.random.randint(0,100)==1:
                winsound.PlaySound(sound_file2, winsound.SND_FILENAME | winsound.SND_ASYNC)
                print("ApinaE drowned")
                break

            #when apinaE arrives to sivilisaatio, it will play a sound
            if i == duration-1:
                apinaE.apinaE_survived_count += 1 # Increment the counter every time an apinaE is sent.
                i_suppose_i_have_earned_so_much_points(1)
                winsound.PlaySound(sound_file, winsound.SND_FILENAME | winsound.SND_ASYNC)
                print("ApinaE has arrived to sivilisaatio")
                apinaE.arrived_wordE_list.append(apinaE_sana)
                print(f"Arrived words so far: {apinaE.arrived_wordE_list}")  # Debugging print
    

    def luo_saie_apinaE():
        t=threading.Thread(target=apinaE.send_apinaE)
        t.start()
        return t
    
    def useita_apinoitaE():
        #apinaE.arrived_wordE_list.clear()
        def wait_for_threads():
            threads = []
            for i in range(10):
                t = threading.Thread(target= apinaE.send_apinaE)
                threads.append(t)
                time.sleep(1)
           
            for thread in threads:
                thread.start()

            for thread in threads:
                thread.join()

            apinaE.count_different_words()
            if np.random.randint(0,100)<50:
                print("Only about half of the words arrived to sivilisaatio")
                i_suppose_i_have_earned_so_much_points(2)

        counting_thread = threading.Thread(target=wait_for_threads)
        counting_thread.start()

    @staticmethod
    def count_different_words():
        unique_words = set(apinaE.arrived_wordE_list)
        print(f"Number of different words: {len(unique_words)}")
        print("Different words: ")
        for word in unique_words:
            print(word)

        if len(unique_words) >= 10:
            apinaE.send_shipE()
            i_suppose_i_have_earned_so_much_points(3)

    def animate_shipE(i, ship_image, start_x, autiosaari_x, start_y, autiosaari_y, duration):
        if i < duration:
            new_x = start_x + (autiosaari_x - start_x) * (i / duration)
            new_y = start_y + (autiosaari_y - start_y) * (i / duration)
        
            new_x = 600 - i * 5
            new_y = 240 + np.random.randint(-10, 10)
            ship_image.place(x=new_x, y=new_y)

            ikkuna.after(100, apinaE.animate_shipE, i+1, ship_image, start_x, autiosaari_x, start_y, autiosaari_y, duration)  # 100 milliseconds delay
        else:
            print("Ship has arrived to north of autiosaari")
            winsound.PlaySound("KOULU\Python\Taputukset.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
            ikkuna.after(1000, lambda: [send_ship_backE(ship_image), ship_image.place_forget()])
    @staticmethod
    def send_shipE():
        ship_image = tk.Label(ikkuna, image=ship_photo)
        print("10 different words arrived to sivilisaatio, so ship is sent to north of autiosaari")
    
        autiosaari_x = 5
        autiosaari_y = 250
        start_x = 600
        start_y = 250
        duration = 100
    
        apinaE.animate_shipE(0, ship_image, start_x, autiosaari_x, start_y, autiosaari_y, duration)
        i_suppose_i_have_earned_so_much_points(4)

    def animate_ship_backE(i, ship_image, start_x, sivilisaatio_x, start_y, sivilisaatio_y, duration):
        if i < duration:
            new_x = start_x + (sivilisaatio_x - start_x) * (i / duration)
            new_y = start_y + (sivilisaatio_y - start_y) * (i / duration)
        
            new_x = 75 + i * 5
            new_y = 250 + np.random.randint(-10, 10)
            ship_image.place(x=new_x, y=new_y)
        
            ikkuna.after(100, apinaE.animate_ship_backE, i+1, ship_image, start_x, sivilisaatio_x, start_y, sivilisaatio_y, duration)  # 100 milliseconds delay
        else:
            print("Ship has arrived to north of sivilisaatio")
            winsound.PlaySound("KOULU\Python\Taputukset.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

    
class apinaK:
    apinaK_survived_count = 0 # a counter to keep track of how many apinaK's have been sent
    arrived_wordK_list = []

    # create a funtion that sends apina everytime button is pressed.
    def send_apinaK():
        apinaK_sana = apinaK.word_for_apinaK()
        apinaK_image=tk.Label(ikkuna,image=apina_photo)
        print("ApinaK is sent from autiosaari to sivilisaatio")
        sivilisaatio_x = 550
        sivilisaatio_y = 450
        duration = 100
        start_x = 50
        start_y = 450

        apinaK_aani = np.random.randint(300,3000)

        sound_file = "KOULU\Python\swim.wav"
        sound_file2= "KOULU\Python\Failure.wav"

        for i in range(duration):
            new_x = start_x + (sivilisaatio_x - start_x) * (i / duration)
            new_y = start_y + (sivilisaatio_y - start_y) * (i / duration)

            new_x = 75+i*4.5
            new_y = 450+np.random.randint(-10,10)
            apinaK_image.place(x=new_x, y=new_y)
            winsound.Beep(apinaK_aani,100)
            ikkuna.update()
            time.sleep(0.1)

            if np.random.randint(0,100)==1:
                winsound.PlaySound(sound_file2, winsound.SND_FILENAME | winsound.SND_ASYNC)
                print("ApinaK drowned")
                break

            #when apinaK arrives to sivilisaatio, it will play a sound
            if i == duration-1:
                apinaK.apinaK_survived_count += 1 # Increment the counter every time an apinaK is sent.
                winsound.PlaySound(sound_file, winsound.SND_FILENAME | winsound.SND_ASYNC)
                print("ApinaK has arrived to sivilisaatio")
                apinaK.arrived_wordK_list.append(apinaK_sana)
                print(f"Arrived words so far: {apinaK.arrived_wordK_list}")  # Debugging print

        #create a function that gives random one word from hätäviesti to a apina.
    def word_for_apinaK():
        print("ApinaK are given a word from hätäviesti")
        hätäviesti = "Ernesti ja Kernesti tässä terve! Olemme autiolla saarella, ja voisitteko tulla sieltä sivistyksestä joku hakemaan meidät pois! Kiitos!"
        sanat = hätäviesti.split()
        apinaK_sana = sanat[np.random.randint(0,len(sanat))]
        print("ApinaK's word is: "+apinaK_sana)
        return apinaK_sana
    

    def luo_saie_apinaK():
        t=threading.Thread(target=apinaK.send_apinaK)
        t.start()
        return t

    def useita_apinoitaK():
        #apinaK.arrived_wordK_list.clear()
        def wait_for_threads():
            threads = []
            for i in range(10):
                t = threading.Thread(target= apinaK.send_apinaK)
                threads.append(t)
                time.sleep(1)
           
            for thread in threads:
                thread.start()

            for thread in threads:
                thread.join()

            apinaK.count_different_words()
            if np.random.randint(0,100)<50:
                print("Only about half of the apinaK's arrived to sivilisaatio")


        counting_thread = threading.Thread(target=wait_for_threads)
        counting_thread.start()

    @staticmethod
    def count_different_words():
        unique_words = set(apinaK.arrived_wordK_list)
        print(f"Number of different words: {len(unique_words)}")
        print("Different words: ")
        for word in unique_words:
            print(word)

        if len(unique_words) >= 10:
            apinaK.send_shipK()

    def animate_shipK(i, ship_image, start_x, autiosaari_x, start_y, autiosaari_y, duration):
        if i < duration:
            new_x = start_x + (autiosaari_x - start_x) * (i / duration)
            new_y = start_y + (autiosaari_y - start_y) * (i / duration)
        
            new_x = 600 - i * 5
            new_y = 440 + np.random.randint(-10, 10)
            ship_image.place(x=new_x, y=new_y)
        
            ikkuna.after(100, apinaK.animate_shipK, i+1, ship_image, start_x, autiosaari_x, start_y, autiosaari_y, duration)  # 100 milliseconds delay
        else:
            print("Ship has arrived to south of autiosaari")
            winsound.PlaySound("KOULU\Python\Taputukset.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
            ikkuna.after(1000, lambda: [send_ship_backK(ship_image), ship_image.place_forget()])
    @staticmethod
    def send_shipK():
        ship_image = tk.Label(ikkuna, image=ship_photo)
        print("10 different words arrived to sivilisaatio, so ship is sent to south of autiosaari")
    
        autiosaari_x = 5
        autiosaari_y = 250
        start_x = 525
        start_y = 450
        duration = 100
    
        apinaK.animate_shipK(0, ship_image, start_x, autiosaari_x, start_y, autiosaari_y, duration)

    def animate_ship_backK(i, ship_image, start_x, sivilisaatio_x, start_y, sivilisaatio_y, duration):
        if i < duration:
            new_x = start_x + (sivilisaatio_x - start_x) * (i / duration)
            new_y = start_y + (sivilisaatio_y - start_y) * (i / duration)
        
            new_x = 75 + i * 5
            new_y = 450 + np.random.randint(-10, 10)
            ship_image.place(x=new_x, y=new_y)
        
            ikkuna.after(100, apinaK.animate_ship_backK, i+1, ship_image, start_x, sivilisaatio_x, start_y, sivilisaatio_y, duration)  # 100 milliseconds delay
        else:
            print("Ship has arrived to south of sivilisaatio")
            winsound.PlaySound("KOULU\Python\Taputukset.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)


def send_ship_backE(ship_image):
    ship_image = tk.Label(ikkuna, image=ship_photo)
    print("Ship is sent back to sivilisaatio from north of autiosaari")

    sivilisaatio_x = 550
    sivilisaatio_y = 250
    start_x = 5
    start_y = 250
    duration = 100

    apinaE.animate_ship_backE(0, ship_image, start_x, sivilisaatio_x, start_y, sivilisaatio_y, duration)    

    ship_image.place_forget()

    print(f"Number of apinaE's survived: {apinaE.apinaE_survived_count}")
    print(f"Number of apinaK's survived: {apinaK.apinaK_survived_count}")

    if apinaE.apinaE_survived_count < apinaK.apinaK_survived_count:
        print("Kernesti made the food last longer.")
        print(f"Food lasted for {apinaK.apinaK_survived_count * 4} days.")

    else:
        print("Ernesti made the food last longer.")
        print(f"Food lasted for {apinaE.apinaE_survived_count * 4} days.")
    i_suppose_i_have_earned_so_much_points(5)
def send_ship_backK(ship_image):
    ship_image = tk.Label(ikkuna, image=ship_photo)
    print("Ship is sent back to sivilisaatio from south of autiosaari")

    sivilisaatio_x = 550
    sivilisaatio_y = 450
    start_x = 5
    start_y = 450
    duration = 100

    apinaK.animate_ship_backK(0, ship_image, start_x, sivilisaatio_x, start_y, sivilisaatio_y, duration)

    ship_image.place_forget()

    print(f"Number of apinaE's survived: {apinaE.apinaE_survived_count}")
    print(f"Number of apinaK's survived: {apinaK.apinaK_survived_count}")

    if apinaE.apinaE_survived_count < apinaK.apinaK_survived_count:
        print("Kernesti made the food last longer.")
        print(f"Food lasted for {apinaK.apinaK_survived_count * 4} days.")

    else:
        print("Ernesti made the food last longer.")
        print(f"Food lasted for {apinaE.apinaE_survived_count * 4} days.")
    i_suppose_i_have_earned_so_much_points(5)

def start_competition():
    apinaE.useita_apinoitaE()
    apinaE.count_different_words()
    apinaK.useita_apinoitaK()
    apinaK.count_different_words()

#send 10 monkeys button
start_competition_button=tk.Button(ikkuna,text="Send 10 monkeys",padx=40,command=start_competition)
start_competition_button.place(x=270, y=70)

#send apinaE button
apinaE_button=tk.Button(ikkuna,text="Send apinaE",padx=40,command=lambda: [apinaE.word_for_apinaE(),apinaE.luo_saie_apinaE()])
apinaE_button.grid(row=2,column=1)

#send apinaK button
apinaK_button=tk.Button(ikkuna,text="Send apinaK",padx=40,command=lambda: [apinaK.word_for_apinaK(),apinaK.luo_saie_apinaK()])
apinaK_button.grid(row=2,column=2)

#images
autiosaari_image=tk.Label(ikkuna,image=autiosaari_photo)
autiosaari_image.place(x=5, y=250)

sivilisaatio_image=tk.Label(ikkuna,image=sivilisaatio_photo)
sivilisaatio_image.place(x=550, y=250)

ikkuna.mainloop()
