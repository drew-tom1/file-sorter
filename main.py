import os
import shutil
import time

source = 'C:/Users/drew/Downloads/'

totalFiles = os.listdir(source)

for file in totalFiles:
    start_time = time.time()
    fullList = os.path.splitext(file)
    extension = fullList[-1] 

    match extension:
        case ".pdf":
            shutil.move(source + '/' + file, 'C:/Users/drew/Documents/.pdfs/' + file)
        case ".docx":
            shutil.move(source + '/' + file, 'C:/Users/drew/Documents/.docxs/' + file)
        case ".jpeg":
            shutil.move(source + '/' + file, 'C:/Users/drew/Documents/photos/' + file)
        case ".jpg":
            shutil.move(source + '/' + file, 'C:/Users/drew/Documents/photos/' + file)
        case ".png":
            shutil.move(source + '/' + file, 'C:/Users/drew/Documents/photos/' + file)
        case ".mp3":
            shutil.move(source + '/' + file, 'C:/Users/drew/Videos/' + file)
        case ".mp4":
            shutil.move(source + '/' + file, 'C:/Users/drew/Videos/' + file)
        case ".zip":
            shutil.move(source + '/' + file, 'C:/Users/drew/Documents/.zips/' + file)
        case ".pka":
            shutil.move(source + '/' + file, 'C:/Users/drew/Documents/packet tracers/' + file)
        case _:
            shutil.move(source + '/' + file, 'C:/Users/drew/Documents/misc/' + file)

    end_time = time.time()
    runtime = end_time - start_time
print(f"Program Runtime: {runtime} seconds")