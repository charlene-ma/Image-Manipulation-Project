"""
--------------------------
--------------------------
image manipulation program
--------------------------
--------------------------
"""

from PIL import Image, ImageFilter, ImageEnhance
import os

#views selected image
def openImg(input):
    globals()[input].show()

#saves selected as png
def makePng(name, input):
    #makes folder if does not exist
    if os.path.isdir("%s\\pngs" % (os.getcwd())) == False:
        os.mkdir("pngs")
    input.save('pngs/{}.png'.format(name))
    print("%s.png has been saved to the 'pngs' folder" % (name))
    print(" ")

#allows user to view images
def viewImg():
    print("Would you like to open an image from a folder or the current directory?")
    #asks whether user would like to view image in a folder
    choice = input("Enter 'folder' or 'current directory': ").lower()
    while choice != "folder" and choice != "current directory":
        choice = input("Invalid input. Please enter 'folder' or 'current directory': ").lower()
    print(" ")
    
    #runs if user wants to view image in a folder
    if choice == "folder":
        #prints all folders in current directory
        folderList = []
        for folder in os.listdir("."):
            if folder.endswith(".jpg") == False and folder.endswith(".py") == False:
                name, extension = os.path.splitext(folder)
                folderList.append(name)
        print("\u001b[33m")
        print("The folders you can open are:")
        print(folderList)
        print("\u001b[37m")
        print(" ")
        
        #asks which folder user would like to open
        openedFolder = input("Which folder would you like to open? (pick one from the list above): ").lower()
        #gives error message if input is invalid
        while True:
            valid = None
            for folder in folderList:
                if openedFolder == folder:
                    valid = True
            if valid != True:
                print(folderList)
                openedFolder = input("Invalid input. (pick a folder from the list above): ").lower()
                print(" ")
            else:
                break
        
        if not os.listdir(openedFolder):
            #runs if chosen folder is empty
            print("\u001b[33m")
            print("This folder is empty")
            print("\u001b[37m")
            print(" ")
        else:
            #runs if chosen folder is "pngs"
            if openedFolder == "pngs":
                #prints list of images user can view
                imgList = []
                for img in os.listdir(openedFolder):
                    if img.endswith(".png"):
                        name, extension = os.path.splitext(img)
                        imgList.append(name)
                print("\u001b[33m")
                print("The images you can view are:")
                print("\u001b[37m")
                print(imgList)
                print(" ")
                
                #gets name of image user would like to view
                imgName = input("Which image would you like to view: ").lower()
                #gives error message if input is invalid
                while True:
                    valid = None
                    for img in imgList:
                        if imgName == img:
                            valid = True
                    if valid != True:
                        print(imgList)
                        imgName = input("Invalid input. (pick an image from the list above): ").lower()
                        print(" ")
                    else:
                        break
                image = Image.open("%s/%s/%s.png" % (os.getcwd(), openedFolder, imgName)) 
                    
            else:
                #runs if folder isn't "pngs"
                #prints list of images user can view
                imgList = []
                for img in os.listdir(openedFolder):
                    if img.endswith(".jpg"):
                        name, extension = os.path.splitext(img)
                        imgList.append(name)
                print("\u001b[33m")
                print("The images you can view are:")
                print(imgList)
                print("\u001b[37m")
                print(" ")
                
                #gets name of image user would like to view
                imgName = input("Which image would you like to view: ").lower()
                #gives error message if input is invalid
                while True:
                    valid = None
                    for img in imgList:
                        if imgName == img:
                            valid = True
                    if valid != True:
                        print(imgList)
                        imgName = input("Invalid input. (pick an image from the list above): ").lower()
                    else:
                        break
                    #opens image
                    image = Image.open("%s/%s/%s.jpg" % (os.getcwd(), openedFolder, imgName))  
                    
            #shows image        
            print("Opening image...")
            print(" ")
            image.show()
        
    else:
        #runs if image user would like to view is not in a folder in directory
        #prints list of images user can view
        imgList = []
        for img in os.listdir("."):
            if img.endswith(".jpg"):
                name, extension = os.path.splitext(img)
                imgList.append(name)  
        print("\u001b[33m")
        print("The images you can view are:")
        print(imgList)
        print("\u001b[37m")
        print(" ")
        
        #asks which image user would like to view
        imageOpen = input("what image would you like to view: ").lower()
        #gives error message if input is invalid
        while True:
            valid = None
            for img in imgList:
                if imageOpen == img:
                    valid = True
            if valid != True:
                print(imgList)
                imageOpen = input("Invalid input. (pick an image from the list above): ").lower()
                print(" ")
            else:
                break
        
        #shows image
        image = Image.open(imageOpen + ".jpg")
        print("Opening image...")
        print(" ")
        image.show()

#change file size
def resize(size, imgName, img):
    #makes folder if folder does not exist
    if os.path.isdir("%s\\%d%s" % (os.getcwd(), size, " px")) == False:
        os.mkdir("%d px" % (size))
    img.thumbnail((size, size))
    img.save('%d px/%s %d.jpg' % (size, imgName, size))
    print("\u001b[33m")
    print("Your %d pixel image has been saved in the '%d px' folder." % (size, size))
    print("\u001b[37m")
    print(" ")

#rotates opened img to length inputted by user
def rotate(img, angle, imgName):
    #makes folder if folder does not exist
    if os.path.isdir("%s\\%s" % (os.getcwd(), str(angle) + " degree rotations")) == False:
        os.mkdir("%d degree rotations" % (angle))
    img.rotate(angle).save("%d degree rotations/%s rotated_%d" % (angle, imgName, angle) + ".jpg")
    print("\u001b[33m")
    print("Your modified file has been saved to the '%d degree rotations' folder" % (angle))
    print("\u001b[37m")
    print(" ")

#makes selected img black and white
def blackAndWhite(img, imgName):
    #makes folder if folder does not exist
    if os.path.isdir("%s\\black and white" % (os.getcwd())) == False:
        os.mkdir("black and white")
    img.convert(mode='L').save('black and white/%s (b and w).jpg' % (imgName))
    print("\u001b[33m")
    print("Your black and white image has been saved to the 'black and white' folder")
    print("\u001b[37m")
    print(" ")

#makes img blurred based on blur radius inputted by user
def blur(img, imgName, radius):
    #makes folder if folder does not exist
    if os.path.isdir("%s\\blurred images" % (os.getcwd())) == False:
        os.mkdir("blurred images")
    img.filter(ImageFilter.GaussianBlur(radius)).save("blurred images/%s %d blurred.jpg" % (imgName, radius))
    print("\u001b[33m")
    print("Your blurred image has been saved in the 'blurred images' folder")
    print("\u001b[37m")
    print(" ")
    
#increases contrast of image
def contrastChange(img, percentage, imgName):
    #makes folder if folder does not exist
    if os.path.isdir("%s\\contrast change" % (os.getcwd())) == False:
        os.mkdir("contrast change")
    decimal = (percentage/100) + 1
    ImageEnhance.Contrast(img).enhance(decimal).save("contrast change/%s (%d contrast increase).jpg" % (imgName, percentage))
    print("\u001b[33m")
    print("Your image has been saved in the 'contrast change' folder")
    print("\u001b[37m")
    print(" ")

#makes a list of img names
imgList = []
for img in os.listdir("."):
    if img.endswith(".jpg"):
        name, extension = os.path.splitext(img)
        imgList.append(name)

program = "start"
decision = None

while True:
    #asks what user would like to do at start
    if program == "start":
        print(" ")
        print("Welcome to the image manipulation program! Enter 'open' to open an image and modify it, 'view' to view an image, 'view all' to view all images in directory, or 'q' to quit.")
        decision = input("Enter 'open', 'view', or 'q': ").lower()
        while decision != "open" and decision != "view" and decision != "q":
            decision = input("Invalid input. Please enter 'open', 'view', 'view all', or 'q': ").lower()
        program = "ongoing"
        print(" ")
    
    #opens image
    if decision == "open":
        #prints list of all imgs in directory
        print("\u001b[33m")
        print("The images you can open are:")
        print(imgList)
        print("\u001b[37m")
        print(" ")
        
        #opens img base on input
        image = input("Which image would you like to open? (enter one of the above options): ").lower()
        print(" ")
        while imgList.count(image) == 0:
            print("Invalid input. Please pick enter something from the list below: ")
            print("The images you can open are:")
            print(imgList)
            image = input("Enter an image from the list above: ").lower()
            print(" ")
        openedImg = Image.open('%s.jpg' % (image))
        
        #asks how user would like to modify img (if yes)
        while True:
            print("How would you like to modify the image file? (you can save as png, resize, rotate, make black and white, blur, or increase contrast)")
            modType = input("(enter 'png', 'resize', 'rotate', 'black and white', 'blur', or 'contrast'): ").lower()
            print(" ")
            while modType != "png" and modType != "resize" and modType != "rotate" and modType != "black and white" and modType != "blur" and modType != "contrast":
                modType = input("Invalid input. Please enter 'png', 'resize', 'rotate', 'black and white', 'blur', or 'contrast': ").lower()
                print(" ")
            
            #saves img as png
            if modType == "png":
                #prints message if png file already exists
                if os.path.isfile("%s\\pngs\\%s" % (os.getcwd(), image + ".png")) == True:
                    print("\u001b[33m")
                    print("You already have a vesion of this image with a png file type")
                    print("\u001b[37m")
                    print(" ")
                else:
                    makePng(image, openedImg)
                    
            #resizes img
            elif modType == "resize":
                while True:
                    try:
                        resizeVal = int(input("What size in pixels would you like your image to be?: "))
                        print(" ")
                        break
                    except:
                        print("Invalid input. Please enter an integer")
                        
                if os.path.isfile("%s\\%d px\\%s %d.jpg" % (os.getcwd(), resizeVal, image, resizeVal)) == True:
                    #prints if file already exists
                    print("\u001b[33m")
                    print("You already have a version of this file with this file size")
                    print("\u001b[37m")
                    print(" ")
                else:
                    resize(resizeVal, image, openedImg)
            
            #rotates img      
            elif modType == "rotate":
                while True:
                    try:
                        rotAngle = int(input("How much would you like to rotate your image? (enter an angle): "))
                        print(" ")
                        break
                    except:
                        print("Invalid input. Please enter an integer")
                        
                if os.path.isfile("%s\\%d degree rotations\\%s" % (os.getcwd(), rotAngle, image + " rotated_" + str(rotAngle) + ".jpg")) == True:
                    #prints if file already exists
                    print("\u001b[33m")
                    print("You have already rotated this image to %d degrees" % (rotAngle))
                    print("\u001b[37m")
                    print(" ")
                else:
                    rotate(openedImg, rotAngle, image)

            #makes img black and white
            elif modType == "black and white":
                if os.path.isfile("%s\\black and white\\%s (b and w).jpg" % (os.getcwd(), image)) == True:
                    #prints if file already exists
                    print("\u001b[33m")
                    print("You already have a black and white version of this file")
                    print("\u001b[37m")
                    print(" ")
                else:
                    blackAndWhite(openedImg, image)
            
            #blurs images
            elif modType == "blur":
                while True:
                    try:
                        blurRadius = int(input("Enter your desired blur radius (enter an integer): "))
                        print(" ")
                        break
                    except:
                        print("Invalid input. Please enter an integer")
                        
                if os.path.isfile("%s\\blurred images\\%s %d blurred.jpg" % (os.getcwd(), image, blurRadius)) == True:
                    #prints if file already exists
                    print("\u001b[33m")
                    print("You already have a blurred version of this file")
                    print("\u001b[37m")
                    print(" ")
                else:
                    blur(openedImg, image, blurRadius)
            
            #changes contrast
            elif modType == "contrast":
                while True:
                    try:
                        contrastPercentage = int(input("Enter a number value to increase the contrast by (enter an integer): "))
                        print(" ")
                        break
                    except:
                        print("Invalid input. Please enter an integer")
                        
                if os.path.isfile("%s\\contrast change\\%s (%d contrast increase).jpg" % (os.getcwd(), image, contrastPercentage)) == True:
                    #prints if file already exists
                    print("\u001b[33m")
                    print("You already have a version of this file with a contrast increase of %d" % (contrastPercentage))
                    print("\u001b[37m")
                    print(" ")
                else:
                    contrastChange(openedImg, contrastPercentage, image)
            
            #asks if user would like to make another edit
            done = input("Would you like to make another edit? (Enter 'yes' or 'no'): ").lower()
            print(" ")
            while done != "yes" and done != "no":
                done = input("Would you like to make another edit? (Enter 'yes' or 'no'): ").lower()
            if done == "no":
                program = "start"
                break
    
    #allows user to view images in directory 
    elif decision == "view":
        viewImg()
        #asks if user would like to view another image
        while True:
            ask = input("Would you like to view another image (enter 'yes' or 'no'): ").lower()
            print(" ")
            while ask != "yes" and ask != "no":
                ask = input("Invalid input. Please enter 'yes' or 'no'): ")
                print(" ")
            if ask == "yes":
                viewImg()
            else:
                program = "start"
                break
    
    #runs if user quits program
    elif decision == "q":
        print("Exiting program...")
        print(" ")
        break
        
