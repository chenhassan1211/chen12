import subprocess

# Parameters
experiment_title = "your_experiment_title"
machine_name = "your_machine_name"
command_to_run = "echo 1"

# Constructing the cnvrg command
cnvrg_command = [
    "cnvrg", "run",
    f"-t='{experiment_title}'",
    f"--a='{machine_name}'",
    command_to_run
]

# Execute the command
result = subprocess.run(cnvrg_command, capture_output=True, text=True)

# Check if the command ran successfully
if result.returncode == 0:
    print("Command executed successfully!")
    print(result.stdout)
else:
    print("Command failed!")
    print(result.stderr)
