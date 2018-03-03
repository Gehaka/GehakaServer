def write_file(code):
  with open('output.py', 'w') as fp:
    fp.writelines(line + '\n' for line in code)

def execute(code):
  write_file(code)
  out = subprocess.check_output(['python' 'output.py'])
  return str(out)