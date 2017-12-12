# Transcript.py
# Program created to take transcripts formatted for reading and turn them into transcripts formatted for the read. This was used in our bear in mind project to limit the amount of manual work that needs to be done
#
# Aaron Kaye, 2017

# Getting the input file and reading it
data_file = open("transcript.txt", "r")
lines = data_file.readlines()
data_file.close

# Creating the output file
data_out = open("transcript-formatted.txt", "w")

# Looping through file contents and writing formatted version to file
data_out.write('<div class="transcript-container transcript-sa">')
data_out.write('<h3>Transcript</h3>')
for line in lines:
    if line.rstrip() != "":
        data_out.write(''.join(('<p>', line.rstrip(), '</p>')))

data_out.write('</div>')

# File reading complete, close file
data_out.close()
