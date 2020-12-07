""""

Name:		problem2.py
Purpose: Compute the number of popeyes chicken pieces each student and the teacher will get and output it to the user.

Author:	Wang.J

Created:	date in 07/12/2020

"""

print(" *** Welcome to the popeyes chicken piece distributer *** ")

# get the number of students and popeyes chicken pieces from the UserWarning
students = int(input("Enter the number of students: "))
chicken_pieces = int(input("Enter the number of popeyes chicken pieces: "))

# compute the number of popeyes chicken pieces each student and the teacher will get
chicken_students = int(round(chicken_pieces / students))
Mr_Fabroa = int(round(students % chicken_pieces))

# output the number of popeyes chicken pieces each student will get and the number of popeyes chicken pieces the teacher will get
print ("The number of popeyes chicken pieces each student will get is " + str(chicken_students))
print ("The number of popeyes chicken pieces Mr. Fabroa will get is " + str(Mr_Fabroa))