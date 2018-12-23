
import Draw
import random

Draw.setCanvasSize(650, 800)
colors=[(Draw.RED), (Draw.YELLOW), (Draw.GREEN), (Draw.BLUE), (Draw.PINK), (Draw.CYAN), (Draw.ORANGE)]
def board():
    Brown = Draw.color(192, 128, 64)
    Draw.setBackground(Brown)
    
    
    #The board of the game
    Draw.setColor(Draw.LIGHT_GRAY)
    Draw.filledRect(125, 25, 400, 690)
    
    #The top of the board with the mystery code
    Draw.setColor(Draw.BLACK)
    Draw.rect(135, 30, 365, 55)
    Draw.setFontSize(34)
    Draw.string("[?] [?] [?] [?] [?]",140, 35)
    Draw.setFontSize(22)
    Draw.setFontBold(True)
    Draw.setFontItalic(True)
    Draw.setFontFamily('Helvetica')
    Draw.string("Mystery \n        Code", 375, 35)
    
    #The black dots for the placement of the colors as the player guesses the code later on
    for i in range(95,718,42):
        for j in range(135,361,50):
            Draw.filledOval(j, i, 25, 25)
    
    #The black dots that the computer will fill in later on with feedback to the player
    for i in range(105, 718, 42):
        for j in range(400, 501, 25):
            Draw.filledOval(j, i, 10, 10)
    
    #The pallette of colors on the bottom of the canvas       
    
    
    i=0
    for n in colors:
        Draw.setColor(n)
        Draw.filledRect(80+i, 740, 70, 50)
        i+=70

def outcome():
    Draw.setColor(Draw.BLACK)
    Draw.setFontSize(24)
    Draw.filledRect(215, 450, 175, 50)
    Draw.setColor(Draw.WHITE)
    Draw.string("Play again?", 230,460) 
    Draw.setColor(Draw.CYAN)
    Draw.filledRect(280, 550, 45, 40)
    Draw.setColor(Draw.BLACK)
    Draw.setFontSize(16)
    Draw.string("Exit", 285, 560)
    if Draw.mousePressed():
        print("U")
        mouseU=Draw.mouseX()
        mouseI=Draw.mouseY()
        if mouseU >= 215 and mouseU <= 390 and mouseI <= 500 and mouseI >= 450:
            print("OPLOP")    
    
#Computer picks out a random code consisting of the colors that are in the color pallette
def SecretCode():
    board()
    code=[]
    j=0
    for i in range(5):
        a = random.choice(colors)
        code.append(a) #A list is created with the computer's code
    for n in code:
        Draw.setColor(n)
        Draw.filledOval(j+135, 35, 40, 40) 
        j+=50 
    return code
code = SecretCode()

tries=0
red=0
yay=0
while tries<15: 
    has=[]
    #The player clicks on five colors in the color palette to guess the computer's code
    def userClicked(): 
        clicked=0
        userCode = []
        j=0
        s=tries*42
        while clicked<5: #The player must click the color palette five times-the length of the code
            if Draw.mousePressed():
                mouseX=Draw.mouseX()
                mouseY=Draw.mouseY()
                if mouseX >= 80 and mouseX <= 570 and mouseY <= 790 and mouseY >= 740: #if the click is found within the color palette:
                    f = colors[(mouseX-80)//70] #This equation determines the color that was clicked when the palette was clicked
                    Draw.setColor(f) #the color of Draw is set to the color that the player clicked from the color palette
                    Draw.filledOval(133+j, 682-s, 30, 30) #the black dot is filled with the color that the player clicked
                    Draw.setColor(Draw.BLACK) #aesthetic reasons-to make the colored dot look more aesthetically pleasing, a black border was created around it
                    Draw.oval(133+j, 682-s, 30, 30)
                    j+=50    #the next color the player picks will fill up the dot that is 50 unit away from the previously filled dot            
                    userCode.append(f) #a list is created with the colors the user chooses-a total of five colors
                    clicked+=1 #increases the click after the player clicks
        return userCode          
    userCode = userClicked()
                
    def compareCode(): 
        #compares the computers code to the code that the player guesses and gives feedback to the player regarding the accuracy of his/her code
        k=0
        red=0
        d={}
        w={}
        aa={}
        wrong=0
        yay=0
        r=42*(tries-1) #formula to increase between small white and red circles
        
        #Evaluates the computers code and creates a dictionary of how many of each color is in the code
        for c in code:
            if c in d:
                d[c]+=1
            else:
                d[c]=1
        
        #Compares computer's code to player's code for instances where both the colors and the place of the color are the same in both codes
        for i in range(len(code)):
            if userCode[i]==code[i]:
                Draw.setColor(Draw.RED) #if it is true that the place and color are exactly the same, the color is turned to red
                Draw.filledOval(400+k, 693-r, 10, 10) #a small circle to the right of the big black circles on the Mastermind board turns red
                Draw.setColor(Draw.BLACK) #aesthetic reasons-created a black border for the red circle
                Draw.oval(400+k, 693-r, 10, 10)
                k+=25            
                d[code[i]]-=1 #subtracted from the dictionary of the computer's colors the color of the player's code that was in the same place as the same color of the computer's code. (so that finding the player's code that is the right color but not the right place will be easier)
                red+=1 #if there are five red, the player wins
                print(d[code[i]])
                print(userCode)
                print(userCode[i])
            else:
                has.append(userCode[i])
        if red==5:
           
        
        
        #Compares computer's code to player's code in instances where the color in the players code can be found in the computers code but it is not in the same place AND the color cannot be found in the computer's code if the player has that same color in the same place. Ex: players code: [1, 2, 1, 4] Computers code: [5, 6, 1, 7]. the 1 in the player's code in place 0 cannot be found in the computers code because the player's code also has the same color in a place that matches the computers code and would result in a red circle.
        for i in range(len(has)):
            if has[i] in d:
                if d[has[i]]>0: #if the color is found in the dictionary containing the computer's code and there arent more of that color in the players code than in the computers code:
                    Draw.setColor(Draw.WHITE) #fill in a small white circle to the right of the big circles
                    Draw.filledOval(400+k, 693-r, 10, 10)
                    Draw.setColor(Draw.BLACK) #aesthetic reasons-black border of the white circle
                    Draw.oval(400+k, 693-r, 10, 10)         
                    k+=25 
                    d[has[i]]-=1   #keep track of the number of colors found in players code to ensure it doesnt exceed the amount of times that color is found in the computers code.
        print(userCode)
        print(code)
    tries+=1    #the player receives 15 tries before he/she loses
    compareCode()
if compareCode()==100:
    Draw.clear()
    Draw.setBackground(Draw.CYAN)
    Draw.setFontBold(True)
    Draw.setFontFamily('Helvetica')
    Draw.setColor(Draw.RED)
    for i in range(0 , 20, 1):
        Draw.clear()                
        Draw.setFontSize((10*(i+1))//2)
        Draw.string("YOU WIN!", 200-7*i, 400-7*i)
        Draw.show()
    outcome()    
    while True:
        if Draw.mousePressed():
                mouseX=Draw.mouseX()
                mouseY=Draw.mouseY()
                if mouseX >= 215 and mouseX <= 390 and mouseY <= 500 and mouseY >= 450:
                    red==0
                    Draw.clear()
                    SecretCode()
                    compareCode()
j=0
for n in code:
    Draw.setColor(n)
    Draw.filledOval(j+135, 35, 40, 40) 
    j+=50
Draw.clear()
Draw.setBackground(Draw.CYAN)
Draw.setColor(Draw.BLACK)
Draw.setFontSize(60) 
Draw.string("YOU LOSE:-(", 130, 250)
outcome()
if Draw.mousePressed():
    mouseX=Draw.mouseX()
    mouseY=Draw.mouseY()
    if mouseX >= 215 and mouseX <= 390 and mouseY <= 500 and mouseY >= 450:
        Draw.clear()
        
        main()


def main():
    SecretCode()
    userCode()
    #compares the computers code to the code that the player guesses and gives feedback to the player regarding the accuracy of his/her code
    k=0
    red=0
    d={}
    w={}
    aa={}
    wrong=0
    r=42*(tries-1) #formula to increase between small white and red circles
    
    #Evaluates the computers code and creates a dictionary of how many of each color is in the code
    for c in code:
        if c in d:
            d[c]+=1
        else:
            d[c]=1
    
    #Compares computer's code to player's code for instances where both the colors and the place of the color are the same in both codes
    for i in range(len(code)):
        if userCode[i]==code[i]:
            Draw.setColor(Draw.RED) #if it is true that the place and color are exactly the same, the color is turned to red
            Draw.filledOval(400+k, 693-r, 10, 10) #a small circle to the right of the big black circles on the Mastermind board turns red
            Draw.setColor(Draw.BLACK) #aesthetic reasons-created a black border for the red circle
            Draw.oval(400+k, 693-r, 10, 10)
            k+=25            
            d[code[i]]-=1 #subtracted from the dictionary of the computer's colors the color of the player's code that was in the same place as the same color of the computer's code. (so that finding the player's code that is the right color but not the right place will be easier)
            red+=1 #if there are five red, the player wins
            print(d[code[i]])
            print(userCode)
            print(userCode[i])
        else:
            has.append(userCode[i])
    
    
    #Compares computer's code to player's code in instances where the color in the players code can be found in the computers code but it is not in the same place AND the color cannot be found in the computer's code if the player has that same color in the same place. Ex: players code: [1, 2, 1, 4] Computers code: [5, 6, 1, 7]. the 1 in the player's code in place 0 cannot be found in the computers code because the player's code also has the same color in a place that matches the computers code and would result in a red circle.
    for i in range(len(has)):
        if has[i] in d:
            if d[has[i]]>0: #if the color is found in the dictionary containing the computer's code and there arent more of that color in the players code than in the computers code:
                Draw.setColor(Draw.WHITE) #fill in a small white circle to the right of the big circles
                Draw.filledOval(400+k, 693-r, 10, 10)
                Draw.setColor(Draw.BLACK) #aesthetic reasons-black border of the white circle
                Draw.oval(400+k, 693-r, 10, 10)         
                k+=25 
                d[has[i]]-=1   #keep track of the number of colors found in players code to ensure it doesnt exceed the amount of times that color is found in the computers code.
        else:
            print("P")
    print(userCode)
    print(code)
    if red==5:
        Draw.clear()
        Draw.setBackground(Draw.CYAN)
        Draw.setFontBold(True)
        Draw.setFontFamily('Helvetica')
        Draw.setColor(Draw.RED)
        for i in range(0 , 20, 1):
            Draw.clear()                
            Draw.setFontSize((10*(i+1))//2)
            Draw.string("YOU WIN!", 200-7*i, 400-7*i)
            Draw.show()
        outcome()
        if Draw.mousePressed():
            mouseX=Draw.mouseX()
            mouseY=Draw.mouseY()
            if mouseX >= 215 and mouseX <= 390 and mouseY <= 500 and mouseY >= 450:
                red==0
                main()   
    
