#A company decided of 5% to the employee if his/her year of service is more then 5
years. Ask the user for their salary and year of service and print the net bonus amount. 

S=int(input("enter your salary:"))
YOE=int(input("enter your year:"))
if YOE>5:
    B=S*0.05+S
    print("CONGRATULATIONS,you have received bonus for service more than 5 years")
else:
    print("SORRY,you don't get bonus for service less than 5 years")
