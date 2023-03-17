newdic = open("newdic.txt", "r")
cons = ['b', 'C','s', 'S', 'z', 'd', 'f', 'g', 'h', 'J', 'k', 'l', 'n', 'Z', 'w', 'm', 't', 'r', 't', 'D', 'T', 'v', 'w', 'y', 'p']
glides = ['y', 'w']
sonority = ['y', 'w', 'n', 'm', 'r', 'l']
vfricatives = ['v', 'D'] #voiced - took out 'z' because the code didn't like it?
entries = newdic.readlines()

#type counts and probabilities
type_dict= {}
freq_count = {}
total_freq = 0
for line in entries:  
    words = line.split('\t')
    total_freq += int(words[4]) +1
    if line.startswith(tuple(cons)) == True:
        if line[1] in cons:
            if line[2] in cons:
                if type_dict.get(line[0:3]) == None:
                    type_dict[line[0:3]] = 1
                    freq_count[line[0:3]] = int(words[4]) +1
                else:
                    type_dict[line[0:3]] += 1
                    freq_count[line[0:3]] += int(words[4])+1
            else:
                if type_dict.get(line[0:2]) == None:
                    type_dict[line[0:2]] = 1
                    freq_count[line[0:2]] = int(words[4])+1
                else:
                    type_dict[line[0:2]] += 1
                    freq_count[line[0:2]] += int(words[4])+1
        else:
            continue
print(type_dict)
print(freq_count)
print(total_freq)
weights = {}
total = sum(type_dict.values())

for key, value in freq_count.items():
    print (key+' frequency probability against the whole dictionary: '+str(value/total_freq))

for key, value in type_dict.items():
    print(key+' probability: '+str(value/total))
    if len(key) == 3:
        weights[key] = 10
    if key[1] in glides:
        weights[key] = 1.5
    if key[0] in sonority:
        if weights[key] ==None:
            weights[key] = 2
        else:
            weights[key] += 2
    if key[0] in vfricatives:
        if weights[key] == None:
            weights[key] = 1.5
        else:
            weights[key] += 1.5
    if key in weights:
        weighted = value * weights[key]
        print (key + " " +str(weighted))
print (weights)


#syllable length N/V
noun_syllables = {}
verb_syllables = {}
for line in entries:
    words = line.split('\t')
    if 'N' in words[5]:
        if noun_syllables.get(words[2]) ==None:
            noun_syllables[words[2]] = 1
        else:
            noun_syllables[words[2]] += 1
    if 'V' in words[5]:
        if verb_syllables.get(words[2]) ==None:
            verb_syllables[words[2]] = 1
        else:
            verb_syllables[words[2]] += 1
print("Noun Syllable Count")
for key,value in noun_syllables.items():
    print(key+" : "+str(value))
print ("Verb Syllable Count")
for key, value in verb_syllables.items():
    print(key+" : "+str(value))

newdic.close()