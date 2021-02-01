# 파일 모드 write : w, read: r, append :a

try:
    opendfile = open("python_file.txt", "w")
    opendfile.write("Hello World")
except Exception as e:
    print(e)
finally:
    opendfile.close()

#### with 를 사용하면 close를 안해도 된다(위랑 같은 내용)
#with open("text.txt", "w") as opendfile:
#    opendfile.write("Hello ")

opendfile = open("python_file.txt", "a")
opendfile.write("\nHello Again")
opendfile.close()

opendfile = open("python_file.txt", "r")
for i in opendfile:
    print("{}  {} {}".format(i, type(i), type(opendfile)))
opendfile.close()


