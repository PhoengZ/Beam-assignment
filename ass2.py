import sys
from pathlib import Path

# let L is length of path in command and n is number of file in folder
# time complexity is O(nlog(n)) 
# space complexity is O(L + n)

def main():
    print("Type 'exit' to quite")
    cur = Path.cwd().resolve()
    while(True):
        i = input(f'{cur}> ').strip()
        if not i:
            continue
        split_i = i.split()
        c = split_i[0]
        arg = split_i[1:]
        if c == "exit":
            print("Goodbye kub")
            break
        elif c == "cwd":
            print(cur)
        elif c == "ls":
            items = []
            for i in cur.iterdir():
                items.append(i.name)
            items.sort()
            print(" ".join(items))
        elif c == "mkdir":
            if not arg:
                print("mkdir have to have 'folder_name' argument")
                continue
            folder_name = cur / arg[0]
            if folder_name.exists():
                print(f"{folder_name} is already exists")
                continue
            folder_name.mkdir()
        elif c == "touch":
            if not arg:
                print("touch have to have 'file_name' argument")
                continue
            file_name = cur / arg[0]
            if file_name.exists():
                print(f"{file_name} is already exists")
                continue
            file_name.touch()
        elif c == "cd":
            if not arg:
                print("cd have to have 'directory folder' argument")
                continue
            if arg[0] == ".." and cur.parent == cur:
                print("The directory is now at root")
                continue
            if arg[0].startswith("/"):
                new_path = Path(arg[0])
            else:
                new_path = cur / arg[0]
            try:
                correct_path = new_path.resolve(strict=True) # check ว่าไฟล์มีอยู่จริงมั้ย
                if not correct_path.is_dir():
                    print(f"{correct_path} is not a directory.")
                    continue
            except FileNotFoundError:
                print(f"{new_path} is not found")
                continue
            cur = correct_path
        else:
            print(f"Command :{c} isn't defined")

if __name__ == "__main__":
    main()