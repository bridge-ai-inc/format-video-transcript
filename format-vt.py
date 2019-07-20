mystring = ''

# Open input and output files
file_in = open('input_transcript.txt', 'r') 
file_out = open('output_transcript.txt', 'w+')

# Loop through all lines in the transcript and append to 'mystring'
for line in file_in:
  print(line)
  mystring += line.replace('\n', ' ') 

print(mystring)
file_out.write(mystring)

# Remember to close the files
file_in.close()
file_out.close()
