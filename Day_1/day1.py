ROTATION_PATH = "rotations\\rotations.txt"
RESULT_PATH = "rotations\\result.txt"
MAX_ROTATIONS = 100
dial_pnt = 50
password = 0

print(dial_pnt)
try:
    with open(ROTATION_PATH) as rotations:
        for rotation in rotations:
            nb_clicks = int(rotation[1:])
            old_pnt = dial_pnt
            
            if rotation[0] == "L":
                dial_pnt -= nb_clicks
            else:
                dial_pnt += nb_clicks

            print("Before: "+str(dial_pnt))
            

            if dial_pnt < 0:
                while dial_pnt < 0:
                    password += 1
                    dial_pnt += MAX_ROTATIONS
                    print("Add +1")
                    print("Now: " + str(password))
                if old_pnt == 0:
                    password -= 1

            if dial_pnt == 0 and old_pnt != 0:
                password += 1
                print("Add +1")
                print("Now: " + str(password))
            
            while dial_pnt >= MAX_ROTATIONS:
                dial_pnt -= MAX_ROTATIONS
                print("Add +1")
                print("Now: " + str(password))

            print("After: "+str(dial_pnt))

    print("The password is: " + str(password))

    with open(RESULT_PATH, "w") as result:
        result.write(str(password))
except:
    print("There was an error parsing the rotation file")
