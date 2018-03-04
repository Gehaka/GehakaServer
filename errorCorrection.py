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
            temp = lines[i].replace(" ","")
            #def function
            if(temp[0:3] == "def"):
                lines[i] = lines[i][0:3]+" "+temp[3:]
                if(!lines[i][-3:-1] == "()"):
                    lines[i] = lines[i] + "()"
                if(!lines[i][-1:] == ":"):
                    lines[i] = lines[i] + ":"

            #Print Statement
            if("\"" not in lines[i]):
                continue
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
