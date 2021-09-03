import json
import difflib

data = json.load(open('/Users/loganolbrich/Desktop/Coding projects/10 Python Projects/3-FirstAPP/data.json'))

def translate(w):
    if w in data:
        return data[w]
    else:
        closestmatch = difflib.get_close_matches(w, data.keys(),n=2, cutoff=0.75)
        if bool(closestmatch) == False:
            print("Word not found, please try again")
            return
        userinput = input('Did you mean %s? Y or N:' % closestmatch[0])
        if userinput.lower() == 'y':
            print(translate(closestmatch[0]))
        else:
            userinput2 = input('Did you mean %s? Y or N:' % closestmatch[1])
            if userinput2.lower() == 'y':
                print(translate(closestmatch[1]))
            else:
                print('Word doesnt exist, please try again')  
                return

word = input("Enter word:")

Output = translate(word.lower())

if type(Output) == list:
    for item in Output:
        print(item)
else: 
    print(Output)
    
