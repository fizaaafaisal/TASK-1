score=int(input("enter your mark : "))
if(score>80):
    print("A GRADE ")
    print("ELIGIBLE FOR HIGHER STUDIES")
else:
    if(score>60):
        print("B GRADE ")
        print("ELIGIBLE FOR HIGHER STUDIES")
    else:
        if(score>50):
            print("C GRADE")
            print("ELIGIBLE FOR HIGHER STUDIES")
        else:
            if(score>45):
                print("D GRAEDE")
                print("ELIGIBLE FOR HIGHER STUDIES")
            else:
              if(score>25):
                 print("E GRAEDE")
                 print("NOT ELIGIBLE")
              else:
                 print("F GRAEDE")
                 print("NOT ELIGIBLE")
print("BORD OF HIGHER EXAMINATIONS")
