def fileIO():
    myfile = open("Ch5_sample.py", "r") # open the file to read
    title = myfile.readline() # get the first line of the file, the title
    paragraph = myfile.readlines() # read the rest of the lines and store in a list (one line at a time)
    # but only reads what's left after the file (so doesn't include the first line of hte file_

    myfile.close() # close the input file, done reading the file

    print(title) # print the first line of the file, the title
    # we get two end lines because the readline() had read the \n at the end of the line, but print also does
    #   a new line by default, so there are two new lines printed
    #   BECAUSE we didn't chop off the \n
    
    for line in paragraph: # for each string (each line) in the read file
        print(line[:-1]) # print each line without the endline! \n is represented as only one character
        
    print("(The for loop ran", len(paragraph), "times)") # How many times it ran (length of the list)
    
    saveFile = open("Ch5_output.py", "w") # opens the output file to write to
    # write will overwrite anything that already existed. If the file didn't exist before, it just creates a new file
    #   with the given name. Otherwise, it will access that value and COMPLETELY overwrite it.
    print("WOAH!", file=saveFile) # writes "WOAH!" to the output file
    saveFile.close() # closes the output file

    # if we look in the same folder where this file and the input file are saved, the new file that was written to
    #   should be there now! Or if it already existed, it should be updated



fileIO()


