# File I/O
# w - write only mode
# r - read only mode
# r+ - read and write mode
# a- append mode


my_list = [1,2,3,]
my_file = open("C:\\Users\\aparida\\Desktop\\testfile.txt", "w")

for item in my_list:
    my_file.write(str(item) + "\n")

my_file.close()

