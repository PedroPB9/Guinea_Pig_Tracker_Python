c = 0
guinea_type = ''
f = 'chart.csv'


while c < 20:
    print('=*-' * 12)
    print("Welcome To The Guinea Pig Tracker!")
    print('=*-' * 12)
    print("\t\tANIMALS ACCEPTED:")
    print("[1] = Rabbit \n[2] = Mouse")
    print('=*-' * 12)
    try:
        guinea_pig = int(input("Please, inform the code of the guinea pig: "))
    except Exception as ex:
        msg = f"An exception of type {type(ex).__name__} occured. \nArguments: {ex.args}."
        print(msg)
    else:
        try:
            if guinea_pig == 1:
                guinea_type = "Rabbit"
            elif guinea_pig == 2:
                guinea_type = "Mouse"
            else:
                print("Type not accepted!")
                continue
            amount = int(input(f"How much {guinea_type} were used in this stage? "))
        except Exception as ex:
            msg = f"An exception of type {type(ex).__name__} occured. \nArguments: {ex.args}."
            print(msg)
        else:
            try:
                a = open(f, 'rt')
            except (FileNotFoundError, FileNotFoundError):
                a = open(f, 'x')
                a.close()
            finally:
                c+=1
                a = open(f, 'a')
                a.write(f"{guinea_type};{amount}\n")
                a.close()

r = 0.0
m = 0.0
cob = 0
r_pctg = 0.0
m_pctg = 0.0
a = open(f, 'rt')
while True:
    b = a.readline()
    if not b:
        break
    n, am = b.split(';')
    if n == "Rabbit":
        r+= int(am)
    else:
        m+= int(am)
a.close()
cob = r + m
r_pctg = (r*100) // cob
m_pctg = (m*100) // cob
print(f"Guinea Pigs Used: {cob}\n"
      f"Total Rabbits: {r}\n"
      f"Total Mouses: {m}\n"
      f"Rabbit's percentage: {r_pctg}\n"
      f"Mouse's percentage: {m_pctg}")



