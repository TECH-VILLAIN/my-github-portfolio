with open("c:\\Users\\TECH_VILLAIN\\Documents\\message.txt", 'a') as file1:
    file1.write("i am a man in an animal form\n")
    file1.write('i am hipo\n')
    file1.write('somto')
    file1.write('dera')

with open("c:\\Users\\TECH_VILLAIN\\Documents\\message.txt", 'r') as file1:
    content = file1.read()
    print(content)
for char in content:
    print(char)
contents = content.split()
count_words = len(contents)
print(count_words)