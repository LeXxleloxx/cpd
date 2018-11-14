with open('2018_data.csv', 'rb') as file:
    with open('new2018_data.bin', 'wb') as new_file:
        w=file.read()
        new_file.write(w)
        print(w)