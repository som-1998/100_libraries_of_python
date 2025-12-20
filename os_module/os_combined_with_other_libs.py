
import os
import shutil
import schedule
import time
import logging
import subprocess
import pandas as pd



## 1. os + shutil: Automate file backups and cleanup
# Create dummy file and backup directory
## file name
file_to_backup = "data.txt"
backup_dir = "backup"

with open(file_to_backup, "w") as f:
    f.write("Important data")

if not os.path.exists(backup_dir):
    os.mkdir(backup_dir)

shutil.copy(file_to_backup, os.path.join(backup_dir, file_to_backup))
print(f"Backed up {file_to_backup} to {backup_dir}/")

# Clean up
os.remove(file_to_backup)
shutil.rmtree(backup_dir)

### 2. os + schedule: Run tasks at specific times
def job():
    ## can be any function
    print("Job executed at:", time.strftime("%Y-%m-%d %H:%M:%S"))
    print("Scheduled job running:", os.getcwd())

schedule.every(1).seconds.do(job)
# Uncomment below lines to test the schedule in real-time
for _ in range(3):
    schedule.run_pending()
    time.sleep(1)

print("Scheduling demo complete (disabled real-time execution for safety).")

# 3. os + logging: Maintain logs for file operations
logging.basicConfig(filename='app.log', level=logging.INFO)
file_name = "somnath.txt"

with open(file_name, "w") as f:
    f.write("Log this action")

if os.path.exists(file_name):
    logging.info(f"{file_name} created at {os.path.abspath(file_name)}")
    os.remove(file_name)
    logging.info(f"{file_name} deleted")


### 4. os + subprocess: Advanced shell commands
try:
    result = subprocess.run(["echo", "Hello from subprocess"], capture_output=True, text=True)
    print("Subprocess Output:", result.stdout.strip())
except Exception as e:
    print("Subprocess error:", e)

### 5. os + pandas: Batch process CSVs in directories
sample_dir = "csv_dir"
os.mkdir(sample_dir)

# Create dummy CSV files
for i in range(3):
    df = pd.DataFrame({"col1": [i, i+1], "col2": [i+2, i+3]})
    df.to_csv(os.path.join(sample_dir, f"sample_{i}.csv"), index=False)

# Batch read and concat
df_list = []
for file in os.listdir(sample_dir):
    if file.endswith(".csv"):
        df = pd.read_csv(os.path.join(sample_dir, file))
        df_list.append(df)

df = pd.concat(df_list, ignore_index=True)
print(df)

# Cleanup
shutil.rmtree(sample_dir)
