
 ## File Handling 
 
 
## Open a file named "youtube.txt" in write mode ('w')
# If the file does not exist, Python will create it automatically
file = open("youtube.txt", 'w')

try:
    # Write some text inside the file
    file.write('chai aur code')

# "finally" block always runs, even if an error happens above
finally:
    # Close the file to save changes and free memory
    file.close()



# Another and better way to work with files is using "with"
# "with" automatically closes the file for us, so we don’t need file.close()
with open('youtube.txt', 'w') as file:
    # This will overwrite the previous content because mode is 'w'
    file.write('manish is cute')

    

    