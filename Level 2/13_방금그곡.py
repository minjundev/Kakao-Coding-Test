def solution(m, musicinfos):
    answer = dict()
    m = encoding(m)
    for musicinfo in musicinfos :
        category = musicinfo.split(',')
        sheet = encoding(category[3])
        time = computeMinute(category[0],category[1])
        music = makeMusic(time,sheet)
        if m in music :
            answer[category[2]] = time
    
    if len(answer) :
        return max(answer,key=answer.get) # max(answer) does not guarantee the first one
    else :
        return "(None)"

def encoding(string) :
    index = 0
    dict = {'C':'a', 'C#':'b', 'D':'c', 'D#':'d', 'E':'e', 'F':'f', 'F#':'g', 'G':'h', 'G#':'i', 'A':'j', 'A#':'k', 'B':'l', 'E#':'m'}  
    new_string = ''
    while index < len(string)-1 : # ensure index over
        token = string[index]
        if string[index+1] == '#' :
            token += '#'
            index += 1
        new_string += dict[token]
        index += 1
    if index < len(string) :
        new_string += dict[string[index]]
    return new_string
            
def computeMinute(start,end) :
    tmp_start = start.split(':')
    tmp_end = end.split(':')
    return (int(tmp_end[0])-int(tmp_start[0]))*60 + (int(tmp_end[1])-int(tmp_start[1]))

def makeMusic(minute, sheet) :
    music = ''
    for i in range(0,int(minute/len(sheet))) :
        music += sheet
    music += sheet[:minute%len(sheet)]
    return music
