import os
import subprocess

def run_shell():
    while True:
        try:
            # Show shell prompt
            current_dir = os.getcwd()
            command = input(f"{current_dir} $ ")

            # Remove extra spaces
            command = command.strip()

            # Skip empty input
            if not command:
                continue

            # -----------------------
            # BUILT-IN COMMANDS
            # -----------------------

            # Exit shell
            if command == "exit":
                print("Exiting shell...")
                break

            # Change directory
            if command.startswith("cd"):
                try:
                    path = command.split(" ", 1)[1]
                    os.chdir(path)
                except Exception as e:
                    print(f"cd error: {e}")
                continue

            if command == "pwd":
                try:
                    print(os.getcwd())
                except Exception as e:
                    print(f"pwd error: {e}")
                continue


            # -------- LS --------
            if command.startswith("ls"):
                try:
                    parts = command.split(" ", 1)

                    # If no path → use current directory
                    if len(parts) == 1:
                        path = os.getcwd()
                    else:
                        path = parts[1]

                    files = os.listdir(path)

                    for f in files:
                        print(f)

                except Exception as e:
                    print(f"ls error: {e}")

                continue

            # -----------------------
            # EXECUTE SYSTEM COMMAND
            # -----------------------

            # Run command using subprocess
            result = subprocess.run(command, shell=True)

        except KeyboardInterrupt:
            print("\nUse 'exit' to quit.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    run_shell()