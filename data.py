#!/usr/bin/python3

def main():
    text = input('>> ')
    for keyword in ['eval', 'exec', 'import', 'open', 'os', 'read', 'system', 'write']:
        if keyword in text:
            print("No!!!")
            return
    else:
        exec(text)

if __name__ == "__main__":
    main()
