import PyPDF2 as pd
filename = input('Path to the file: ')
file = open(filename,'rb')
pdfReader = pd.PdfReader(file)

tried = 0

if not pdfReader.is_encrypted:
    print('The file is not password protected! You can successfully open it!')
else:
    wordListFile=open("wordList.txt", "r", errors="ignore")
    body=wordListFile.read().lower()
    words=body.split("\n")
    for i in range(len(words)):
        word=words[i]
        print(f"Trying to decode password by {word}")
        #print("Trying to decode password by {}".format(word))
        result=pdfReader.decrypt(word)
        if result==1:
            print("success, the password if {}".format(word))
            break
        elif result==0:
            tried+=1
            print(f"password tried {word}")
            continue