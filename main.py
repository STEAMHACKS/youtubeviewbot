import webbrowser, time
print("Made By STEAMHACKS") 
url = input("Enter Youtube url:")
duration = input("Enter duration befor a new tab: ")
for i in range (20):
    webbrowser.open_new(url)
    time.sleep(int(duration))