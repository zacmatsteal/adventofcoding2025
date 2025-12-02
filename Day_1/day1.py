import math

ROTATION_PATH = "rotations\\rotations.txt"
RESULT_PATH = "rotations\\result.txt"
MAX_ROTATIONS = 100
dial_pnt = 50
password = 0

try:
    with open(ROTATION_PATH) as rotations:
        for rotation in rotations:
            nb_clicks = int(rotation[1:])
            old_pnt = dial_pnt
            
            if rotation[0] == "L":
                dial_pnt -= nb_clicks
            else:
                dial_pnt += nb_clicks

            if (dial_pnt > MAX_ROTATIONS and old_pnt < MAX_ROTATIONS):
                password += 1
                password += dial_pnt // MAX_ROTATIONS - 1
            if (dial_pnt < 0):
                if old_pnt > 0:
                    password += 1
                password += (abs(dial_pnt)) // MAX_ROTATIONS
            
            dial_pnt %= MAX_ROTATIONS
            
            if dial_pnt == 0:
                password += 1

    print("The password is: " + str(password))

    with open(RESULT_PATH, "w") as result:
        result.write(str(password))
except:
    print("There was an error parsing the rotation file")
