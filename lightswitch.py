import tkinter as tk
window = tk.Tk()



print('De lamp is uit..')

# schijf hier tussen je code
window.configure (background="black")

currentState = 'off'
# currentStateSwitch = True

# while currentStateSwitch == True:

text = 'off'
def onclick():
    global currentState
    if currentState == 'on':
        button['text'] = 'Switch light on'
        print('De lamp is uit..')
        window.configure (background="black")
        currentState = 'off' 
    elif currentState == 'off':   
        button['text'] = 'Switch light off'
        print('De lamp is aan..')
        window.configure (background="yellow")
        currentState = 'on'  
                    
button = tk.Button(text=f'Switch light on', bg="white", fg="black", command=onclick)
button.pack(pady = 20, padx = 20)


# schijf hier tussen je code

window.mainloop()