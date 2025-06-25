import os


def write_file(file_name, file_content):
    file_name = str(file_name)
    if not file_name.endswith('.txt'):
        file_name += '.txt'

    directory = os.path.dirname(file_name)
    if directory:  
        os.makedirs(directory, exist_ok=True)

        with open(file_name, 'w') as f:
             f.write(file_content)
          

def append_file(file_name, append_content):
    file_name = str(file_name)
    if not file_name.endswith('.txt'):
        file_name += '.txt'

    directory = os.path.dirname(file_name)
    if directory:  
        os.makedirs(directory, exist_ok=True)

        with open(file_name, 'a') as f:
             f.write(append_content)
   

def read_file(file_name):
     file_name = str(file_name)
     if not file_name.endswith('.txt'):
        file_name += '.txt'

     directory = os.path.dirname(file_name)
     if directory:  
      
      os.makedirs(directory, exist_ok=True)

     with open (file_name,'r') as f:
         return f.read()
  
  