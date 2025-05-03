
import os

# Run a shell command
os.system("echo Hello from the OS")

# Get current working directory
cwd = os.getcwd()
print("Current Working Directory:", cwd)

# Join paths
joined_path = os.path.join("folder", "file.txt")
print("Joined Path:", joined_path)

# Absolute path
abs_path = os.path.abspath("file.txt")
print("Absolute Path:", abs_path)

# List files in directory
print("Files:", os.listdir("."))  
print("Files:", os.listdir(".."))  # List files in parent directory

# Get directory name
dir_name = os.path.dirname("/home/user/file.txt")
print("Directory Name:", dir_name)

# Get base name
base_name = os.path.basename("/home/user/file.txt")
print("Base Name:", base_name)

# Split path
head, tail = os.path.split("/home/user/file.txt")
print("Head:", head)
print("Tail:", tail)

# Split extension
name, ext = os.path.splitext("hello.py")
print("Name:", name)
print("Extension:", ext)

# Safely create a folder
folder = "example_folder"
if not os.path.exists(folder):
    os.mkdir(folder)
    print(f"Folder '{folder}' created.")
else:
    print(f"Folder '{folder}' already exists.")

# Rename a file if it exists
old_name = "old_file.txt"
new_name = "renamed_file.txt"
# Create dummy file to demonstrate rename
with open(old_name, "w") as f:
    f.write("Temporary file content")

if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print(f"Renamed '{old_name}' to '{new_name}'.")

# Delete the renamed file and folder
if os.path.exists(new_name):
    os.remove(new_name)
    print(f"Deleted file '{new_name}'.")

if os.path.exists(folder):
    os.rmdir(folder)
    print(f"Deleted folder '{folder}'.")

print("\n=== Get Environment Variables ===")
# Access environment variable
home = os.environ.get("HOME", "Not Found")
print("HOME Environment Variable:", home)

print("\n=== File Existence and Permissions ===")
file_check = "check.txt"
with open(file_check, "w") as f:
    f.write("test")

print("Does 'check.txt' exist?", os.path.exists(file_check))
print("Is 'check.txt' a file?", os.path.isfile(file_check))
print("Is 'check.txt' readable?", os.access(file_check, os.R_OK))

os.remove(file_check) ## remove a file

print("Current Process ID:", os.getpid())
print("Parent Process ID:", os.getppid())
