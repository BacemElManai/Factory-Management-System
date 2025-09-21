# 🏭 Factory Management System
# Original structure, only menu system added

from numpy import array
from pickle import dump, load

# --- Data model ---
factory = dict(
    name=str,
    employees=int,
    revenue=float,
    address=str,
    id=str,
    director=str
)

records = array([factory] * 5)

# --- Validation functions ---
def is_alpha(s: str) -> bool:
    i = 0
    ok = True
    while i < len(s) and ok:
        ok = "A" <= s[i].upper() <= "Z"
        i += 1
    return ok

def is_upper(s: str) -> bool:
    i = 0
    ok = True
    while i < len(s) and ok:
        ok = "A" <= s[i] <= "Z"
        i += 1
    return ok

# --- Core functions ---
def fill(f):
    answer = "Y"
    while answer.upper() == "Y":
        entry = dict(factory)

        entry["name"] = input("Factory name: ")
        while not (len(entry["name"]) <= 10 and is_upper(entry["name"])):
            entry["name"] = input("Factory name (≤ 10 chars, uppercase only): ")

        entry["employees"] = int(input("Number of employees: "))
        while entry["employees"] <= 10:
            entry["employees"] = int(input("Number of employees (> 10): "))

        entry["revenue"] = int(input("Revenue: "))
        while entry["revenue"] < 0:
            entry["revenue"] = int(input("Revenue (≥ 0): "))

        entry["address"] = input("Address: ")

        entry["id"] = input("Factory ID (8 digits): ")
        while not (len(entry["id"]) == 8 and entry["id"].isdecimal()):
            entry["id"] = input("Factory ID (8 digits): ")

        entry["director"] = input("Director name: ")
        while not (len(entry["director"]) <= 20 and is_alpha(entry["director"])):
            entry["director"] = input("Director name (≤ 20 chars, alphabetic only): ")

        answer = input("Do you want to continue? (Y/N): ")
        while answer.upper() not in ["Y", "N"]:
            answer = input("Do you want to continue? (Y/N): ")

        dump(entry, f)

    f.close()

def sort_factories(f):
    f = open("factories.dat", "rb")
    n = 0
    end = False
    while end == False:
        try:
            records[n] = load(f)
            n += 1
        except:
            end = True
    f.close()

    for i in range(1, n):
        x = records[i]
        j = i
        while j > 0 and records[j - 1]["employees"] < x["employees"]:
            records[j] = records[j - 1]
            j -= 1
        records[j] = x

    f = open("factories.dat", "wb")
    for i in range(n):
        dump(records[i], f)
    f.close()

def transfer(f, f1):
    f = open("factories.dat", "rb")
    end = False
    while end == False:
        try:
            e = load(f)
            if e["address"].lower() == "tunis":
                ch = e["name"] + ":" + e["director"]
                f1.write(ch + "\n")
        except:
            end = True
    f.close()
    f1.close()

# --- Menu system ---
def menu():
    while True:
        print("\n=== 🏭 Factory Management Menu ===")
        print("1 - Add Factory")
        print("2 - Show All Factories")
        print("3 - Show Factories in Tunis")
        choice = input("Enter your choice: ")

        if choice == "1":
            f = open("factories.dat", "ab")
            fill(f)
            sort_factories(f)
        elif choice == "2":
            f = open("factories.dat", "rb")
            n = 0
            end = False
            while not end:
                try:
                    e = load(f)
                    print(e)
                    n += 1
                except:
                    end = True
            f.close()
        elif choice == "3":
            f1 = open("factories_tunis.txt", "w")
            transfer(None, f1)
            print("✅ Tunis factories exported to factories_tunis.txt")
            # Now display the file content
            print("\n📄 Contents of factories_tunis.txt:")
            with open("factories_tunis.txt", "r") as f_read:
                content = f_read.read()
                if content.strip() == "":
                    print("⚠️ No Tunis factories found.")
                else:
                    print(content)
        else:
            print("❌ Invalid choice, please try again.")

# --- Run program ---
if __name__ == "__main__":
    menu()
