import sys
from pathlib import Path

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
            print(" ".join(items))
        elif c == "mkdir":
            if not arg:
                print("mkdir have to have 'folder_name' argument")
                break;
            folder_name = cur / arg[0]
            if folder_name.exists():
                print("Folder is already exists")
                break
            folder_name.mkdir()
        elif c == "touch":
            if not arg:
                print("touch have to have 'file_name' argument")
                break;
            file_name = cur / arg[0]
            if file_name.exists():
                print("file is already exists")
                break
            file_name.touch()
        elif c == "cd":
            if not arg:
                print("cd have to have 'directory folder' argument")
                break;
            if 

        else:
            print(f"Command :{c} isn't defined")

if __name__ == "__main__":
    main()