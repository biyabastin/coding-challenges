# Marks of 5 subjects

sub1 = 78 
sub2 = 85 
sub3 = 92
sub4 = 74
sub5 = 88

# Total marks

total_marks = sub1 + sub2 + sub3 + sub4 + sub5

# Percentage

percentage = total_marks/5 

print("Total marks :", total_marks )
print("percentage :", percentage )

# Grade

if percentage >= 90 and percentage <=100:
    print("Grade : A+")
elif percentage >= 80 and percentage <= 90:
    print("Grade : A") 
elif percentage >= 70 and percentage <=80:
    print("Grade : B")
elif percentage >= 60 and percentage <=70:
    print("Grade : C")
elif percentage >= 50 and percentage <=60:
    print("Grade : D")
else :
    print("Grade : F")

# Result

# print("Total marks :", total_marks )
# print("percentage :", percentage )

