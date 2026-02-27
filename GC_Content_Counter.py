# python GC_Content_Counter.py

# sequence="ATGCATGCATGCATGC"
while True:
    sequence=input("Enter DNA Sequence: ")
    valid=True
    for base in sequence:
        if base.upper() not in "ATGC":
            print(f"Invalid {base} detected. Try again")
            valid=False
            break
    if(valid and sequence):
        break

countG=0
countC=0
for base in sequence:
        if base.upper() == 'G':
            countG=countG+1
        elif base.upper() == "C":
            countC=countC+1
    
gc_content= countC+countG
length=len(sequence) 
content= (gc_content/length)*100

print("C : ",countC)
print("G : ",countG)
print("gc sum : ", gc_content)
print("Length: ", length)
print(f"Final GC Content: {content: .2f}%")


