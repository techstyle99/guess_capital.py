




file = open("/users/georgeaugust/desktop/webdev/visual_studio_code/test_project/project1/textfile.txt", "r")
data = file.read().replace(" ", "")
characters = len(data)
print("There are " + str(characters) + " in this text file")