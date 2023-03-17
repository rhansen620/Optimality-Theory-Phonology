newdic = open("newdic.txt", "r")
cons = ['b', 'C','s', 'S', 'z', 'd', 'f', 'g', 'h', 'J', 'k', 'l', 'n', 'Z', 'w', 'm', 't', 'r', 't', 'D', 'T', 'v', 'w', 'y', 'p', 'M', 'L', 'G', ]
vowel = ['Y', 'c', 'W', 'R', 'x', '@', 'e', 'E', 'I', 'i', '^', 'U', '|', 'u', 'a', 'o', 'O', 'u', 'X']
#glides = ['y', 'w']
#sonority = ['y', 'w', 'n', 'm', 'r', 'l']
#vfricatives = ['v', 'D'] #voiced - took out 'z' because the code didn't like it?
entries = newdic.readlines()

#mono-syllable token frequency
freq_onset_count = {0:0, 1:0, 2:0, 3:0}
freq_coda_count = {0:0, 1:0, 2:0, 3:0}
total_freq = 0
for line in entries:  
    words = line.split('\t')
    total_freq += int(words[4]) +1
    if words[2] == 'S1':
        if words[0][0] in vowel:
            freq_onset_count[0] += int(words[4])+1
        #    print(words[3])
        if words[0][0] in cons:
            freq_onset_count[1] += int(words[4])+1
            if len(words[0]) > 1:
                if words[0][1] in cons:
                    freq_onset_count[2] += int(words[4])+1
                    if len(words[0])>2:
                        if words[0][2] in cons:
                            freq_onset_count[3] += int(words[4])+1
        if words[0][-1] in vowel:
            freq_coda_count[0] += int(words[4])+1
        if words[0][-1] in cons:
            freq_coda_count[1] += int(words[4])+1
            if len(words[0]) > 1:
                if words[0][-2] in cons:
                    freq_coda_count[2] += int(words[4])+1
                    if len(words[0])>2:
                        if words[0][-3] in cons:
                            freq_coda_count[3] += int(words[4])+1

print("Onset Consonant Count")
for key,value in freq_onset_count.items():
    print(str(key)+" : "+str(value))
print ("Coda Consonant Count")
for key, value in freq_coda_count.items():
    print(str(key)+" : "+str(value))


#statistical phonological model
onset_weights = {}
coda_weights = {}

for key, value in freq_onset_count.items():
    if key == 2: #less than 2
        onset_weights[key] = 4
    if key == 3:
        onset_weights[key] = 4
    if key == 3: #less than 3
        onset_weights[key] += 80
    if key == 0: #is coda
        onset_weights[key] = 2.5
print("Onset Weighted Values")    
for key,value in onset_weights.items():
    weighted = value * freq_onset_count.get(key)
    print (str(key) + " " +str(weighted))
print (onset_weights)
print ("Coda Weighted Values")
for key, value in freq_coda_count.items():
    if key == 2: #less than 2
        coda_weights[key] = 4
    if key == 3:
        coda_weights[key] = 4
    if key == 3: #less than 3
        coda_weights[key] += 80
    if key == 0: #is coda
        coda_weights[key] = 2.5
    
for key,value in coda_weights.items():
    weighted = value * freq_coda_count.get(key)
    print (str(key) + " " +str(weighted))
print (coda_weights)

newdic.close()