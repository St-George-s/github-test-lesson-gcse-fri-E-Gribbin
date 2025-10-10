theTeam = ["Ali", "Eve", "Ling", "Nina", "Sarah", "Tom"]

def linearSearch(student_name):
    for counter in range(len(theTeam)):
        if theTeam[counter] == student_name:
            return True
    return False

print(linearSearch("Ali"))
print(linearSearch("Emmie"))
print(linearSearch("Tom"))