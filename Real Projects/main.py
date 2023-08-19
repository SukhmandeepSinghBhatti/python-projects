# This program is in under development




import os

def cratesIfNotExists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

# def move(foldername,files):
#     for file in files:
#         os.replace(file,f"{foldername}{files}")

files = os.listdir()
files.remove("main.py")
print(files)
cratesIfNotExists('Images')
cratesIfNotExists('Media')
cratesIfNotExists('Docs')
cratesIfNotExists('Others')

# imgExts = ".png", ".jpg",".jpeg" 
# Images = [files for files in files if os.path.splitext(files)[1].lower() in imgExts]
# print(Images)

# docExts = ".txt",".docx",".pdf",".doc" 
# Docs = [files for files in files if os.path.splitext(files)[1].lower() in docExts]
# print(Docs)

# mediaExts = ".mp3",".mp4",".flv"
# medias = [files for files in files if os.path.splitext(files)[1].lower() in mediaExts]

# others = ""
# for files in files:
#     ext = os.path.splitext(files)[1].lower()
#     if (ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and os.path.isabs(files):
#         others.append(files)
# print(others)

# move("Images",Images)
# move("Docs",Docs)
# move("Medias",medias)
# move("Others",others)
