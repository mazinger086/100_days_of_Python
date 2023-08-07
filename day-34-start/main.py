# age: int
# name: str
# height: float
# is_human: bool


def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

"""Con el : data_type determinas el tipo de dato en el argunmento
con la -> forzas a que si o si retorne un bool, se los conoce com Type Hints 
"""

if police_check(12):
    print("You may pass")
else:
    print("Pay a fine")