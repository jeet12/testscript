import subprocess

def main():
    # Define source and destination paths
    source_path = "/usr/bin/python3"
    destination_path = "/home/cyberuser/python3"

    # Step 1: Copy python3 to /home/demo/
    subprocess.run(["cp", source_path, destination_path], check=True)

     # Step 2: Set capabilities cap_setuid+ep for /home/demo/python3
    subprocess.run(["setcap", "cap_setuid+ep", destination_path], check=True)

if __name__ == "__main__":
    main()
