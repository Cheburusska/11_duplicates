import os

path = r'C:\your\path\here'    #insert your raw path here, between the quotes

def main(path): #takes the path to the folder and prints list of duplicates
    paths = []
    name_size = []

    for root, dirs, files in os.walk(path):
        for file in files:
            paths.append(root) #list of paths of all files in folder and subfolders
            name_size.append([file,os.path.getsize(root+'\\'+file)]) #list of filenames and filesize of all files in folder and subfolders

    duplicates = []

    for i in range(len(name_size)):
        if name_size.count(name_size[i])>1: #find all duplicates in source list of files
            duplicates.append([name_size[i][1],name_size[i][0],paths[i]])#create list of duplicates

    for duplicate in sorted(duplicates): #sort list of duplicates and print in console
        print('Имя файла: {n}   Размер:{s}    Путь к файлу: {p}'.format(n = duplicate[1],p=duplicate[2],s = duplicate[0]))

if __name__ == '__main__':
    main(path)
