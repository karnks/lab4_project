import subprocess
result = subprocess.run(['python', '../src/input_handler.py', '--type', 'int'], capture_output=True, text=True)
print("STDOUT:", result.stdout)
print("Return code:", result.returncode)