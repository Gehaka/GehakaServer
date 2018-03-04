import keyword
import re

def errorCorrection(lines):
    keyWordList = keyword.kwlist
    operators = ['=','==','+','-','*','/','%','**','//','!=','<>','>','<','>=','<=']
    for i in range(len(lines)):
        lines[i] = re.sub(' +',' ',lines[i])
        #Assignment Operator
        if("=" in lines[i]):
            lines[i] = lines[i]
        else:
            #Print Statement
            if("\"" not in lines[i]):
                continue
            temp = lines[i].replace(" ","")
            if(temp[0:5] != "print"):
                temp = temp[0:5].replace(temp[0:5],"print")
            if(temp[len(temp)-1] == "\"" and temp[5] != "\""):
                temp = temp[:5]+"\""+temp[5:]
            if(temp[len(temp)-1] != "\"" and temp[5] == "\""):
                temp = temp+"\""
            lines[i] = temp
    return lines

def main():
    res = errorCorrection(lines)

if __name__=="main":
    main()
