import subprocess

def write_file(code):
  with open('output.py', 'w') as fp:
    fp.writelines(line + '\n' for line in code)

def execute(code):
  write_file(code)
  try:
    out = subprocess.check_output(['python', 'output.py'], stderr=subprocess.STDOUT)
  except subprocess.CalledProcessError as e:
    out = e.output
  return str(out)