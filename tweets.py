import snscrape.modules.twitter as sntwitter
import shutil
import os

location = "C:/Users/jacob/Desktop/twitterAPI/"
dir = "audios"
path = os.path.join(location,dir)
isdir = os.path.isdir(path)
if isdir == True:
    shutil.rmtree(path)

location = "C:/Users/jacob/Desktop/twitterAPI/"
dir = "audios"
path = os.path.join(location,dir)
os.mkdir(path)

location = "C:/Users/jacob/Desktop/twitterAPI/"
dir = "images"
path = os.path.join(location,dir)
isdir = os.path.isdir(path)
if isdir == True:
    shutil.rmtree(path)

location = "C:/Users/jacob/Desktop/twitterAPI/"
dir = "images"
path = os.path.join(location,dir)
os.mkdir(path)

theauthor = 'elonmusk'
query = "(from:"+theauthor+")"
tweets = []
limit = 300
contenttext = []

tweetlikes = []
tweetrts = []
tweetcmts = []
tweetdate = []

rhymeList = []
rhymesLetters = []

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    if len(tweets) == limit:
        break
    else:
        tweets.append(tweet.content)
        tweetdate.append(tweet.date)
        twtlist = list(tweet.content)
        
        temptext = ""
        templist = []
        dnAllow = False
        for i in range(len(twtlist)):
            if i <= len(twtlist) - 4:
                if twtlist[i] + twtlist[i+1] + twtlist[i+2] + twtlist[i+3] == "http":
                    dnAllow = True
                if twtlist[i] + twtlist[i+1] + twtlist[i+2] + twtlist[i+3] == 'amp;':
                    dnAllow = True
            if twtlist[i] == ' ':
                dnAllow = False
            if dnAllow == False:
                temptext+=twtlist[i]
                if twtlist[i] == "." or twtlist[i] == "?" or twtlist[i] == ";" or twtlist[i] == "!":
                    templist.append(temptext)
                    temptext = ""
        if temptext != "":
            templist.append(temptext)
            
        rhymeList.append(templist)

textList = []
totalTextList = []

for i in range(len(rhymeList)):
    for j in range(len(rhymeList[i])):
        textToList = list(rhymeList[i][j])
        newTextStr = ""
        allowChar = True
        for p in range(len(textToList)):
            if textToList[p] == '@':
                allowChar = False
            if textToList[p] == ' ':
                allowChar = True
            if allowChar == True:
                newTextStr += textToList[p]
        textList.append(newTextStr)
    totalTextList.append(textList)
    textList = []

#print(totalTextList)

rhymeText = []
rhymeType = []
rhymeIds = []

for j in range(len(totalTextList)):
    for i in range(len(totalTextList[j])):
        tempAdd = ''
        listoftext = list(totalTextList[j][i])
        for k in range(len(listoftext)):
            curC = listoftext[len(listoftext)-k-1]
            curOrd = ord(curC)
            if (curOrd >= 65 and curOrd <= 90) or (curOrd >= 97 and curOrd <= 122) or curOrd == 32:
                tempAdd = curC + tempAdd
            if len(list(tempAdd)) >= 3:
                noRhymes = True
                for e in range(len(rhymeType)):
                    if rhymeType[e] == tempAdd:
                        noRhymes = False
                        rhymeText[e].append(totalTextList[j][i])
                        rhymeIds[e].append([j,i])
                        break

                if noRhymes == True:
                    rhymeType.append(tempAdd)
                    rhymeText.append([totalTextList[j][i]])
                    rhymeIds.append([[j,i]])
                break



# for j in range(len(totalTextList)):
#     for i in range(len(totalTextList[j])):
#         tempAdd = ''
#         listoftext = list(totalTextList[j][i])
#         for k in range(len(listoftext)):
#             curC = listoftext[len(listoftext)-k-1]
#             curOrd = ord(curC)
#             if (curOrd >= 65 and curOrd <= 90) or (curOrd >= 97 and curOrd <= 122) or curOrd == 32:
#                 tempAdd = curC + tempAdd
#                 if curC.upper() == 'A' or curC.upper() == 'E' or curC.upper() == 'O' or curC.upper() == 'U' or curC.upper() == 'Y' or curC.upper() == 'I':
#                     noRhymes = True
#                     for e in range(len(rhymeType)):
#                         if rhymeType[e] == tempAdd:
#                             noRhymes = False
#                             rhymeText[e].append(totalTextList[j][i])
#                             rhymeIds[e].append([j,i])
#                             break

#                     if noRhymes == True:
#                         rhymeType.append(tempAdd)
#                         rhymeText.append([totalTextList[j][i]])
#                         rhymeIds.append([[j,i]])
#                     break
            
#print(rhymeText)
#print(rhymeType)


morethanone = []
morethnrhm = []
for i in range(len(rhymeText)):
    if len(rhymeText[i]) >= 4:
        morethanone.append(rhymeText[i])
        morethnrhm.append(rhymeIds[i])

avcnts = []
for i in range(len(morethanone)):
    tcnt = 0
    for j in range(len(morethanone[i])):
        tcnt+= len(list(morethanone))
    avtcnt = tcnt/len(morethanone[i])
    avcnts.append(avtcnt)

newmore = []
newmrhm = []

while len(avcnts) > 0:
    for i in range(len(avcnts)):
        if min(avcnts) == avcnts[i]:
            newmore.append(morethanone[i])
            newmrhm.append(morethnrhm[i])
            morethanone.pop(i)
            morethnrhm.pop(i)
            avcnts.pop(i)
            break

goodrhymes = []
genids = []

for i in range(len(newmore)):
    wordslist = []
    goodrhymest = []
    idest = []
    if len(newmore[i]) >= 4:
        for j in range(len(newmore[i])):
            moreList = list(newmore[i][j])
            lastword = ''
            for k in range(len(moreList)):
                if moreList[len(moreList)-k-1] == ' ':
                    break
                lastcw = moreList[len(moreList)-k-1]
                olastc = ord(lastcw)
                if (olastc >= 65 and olastc <= 90) or (olastc >= 97 and olastc <= 122):
                    lastword = lastcw + lastword
            addtheword = True
            for e in range(len(wordslist)):
                if str(wordslist[e]) == str(lastword):
                    addtheword = False
                    break
            if addtheword == True:
                wordslist.append(lastword)
                goodrhymest.append(newmore[i][j])
                idest.append(newmrhm[i][j])
            if len(goodrhymest) >= 4:
                break
    if len(goodrhymest) >= 4:
        goodrhymes.append(goodrhymest)
        genids.append(idest)

for i in range(len(goodrhymes)):
    print(goodrhymes[i])

import random

lyrics = []
lyricids = []

while len(goodrhymes) > 0 and len(lyrics) < 20:
    randomC = random.randint(0,len(goodrhymes)-1)
    randomList = goodrhymes[randomC]
    randomIds = genids[randomC]
    lyrics.append(randomList)
    lyricids.append(randomIds)
    goodrhymes.pop(randomC)
    genids.pop(randomC)

print(lyrics)
print(lyricids)

for i in range(len(lyricids)):
    for j in range(len(lyricids[i])):
        print(str(i) +' - '+ str(j))
        print(totalTextList[lyricids[i][j][0]][lyricids[i][j][1]])


bpm = 149

bps = bpm/60

aps = 1/bps

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='C:/Users/jacob/Downloads/pythonyoutube-340102-7696de956b15.json'


from google.cloud import texttospeech

# Instantiates a client
client = texttospeech.TextToSpeechClient()
for i in range(len(lyrics)):

    location = "C:/Users/jacob/Desktop/twitterAPI/audios/"
    dir = str(format(i,'05d'))
    path = os.path.join(location,dir)
    os.mkdir(path)

    for j in range(len(lyrics[i])):
        # Set the text input to be synthesized
        synthesis_input = texttospeech.SynthesisInput(text=lyrics[i][j])

        # Build the voice request, select the language code ("en-US") and the ssml
        # voice gender ("neutral")
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
        )

        # Select the type of audio file you want returned
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

        # Perform the text-to-speech request on the text input with the selected
        # voice parameters and audio file type
        response = client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        outputfile = "output"+str(format(j,'05d'))+".mp3"

        # The response's audio_content is binary.
        with open(outputfile, "wb") as out:
            # Write the response to the output file.
            out.write(response.audio_content)
            print('Audio content written to file '+outputfile)
        os.rename(outputfile,'audios/'+format(i,'05d')+'/'+outputfile)

# import pygame module in this program
import pygame

# draw some text into an area of a surface
# automatically wraps words
# returns any text that didn't get blitted


def renderTextCenteredAt(text, font, colour, x, y, screen, allowed_width):
        
        words = text.split()

        
        lines = []
        while len(words) > 0:
            
            line_words = []
            while len(words) > 0:
                line_words.append(words.pop(0))
                fw, fh = font.size(' '.join(line_words + words[:1]))
                if fw > allowed_width:
                    break

            
            line = ' '.join(line_words)
            lines.append(line)

        
        y_offset = 0
        for line in lines:
            fw, fh = font.size(line)

            
            tx = x
            ty = y + y_offset

            font_surface = font.render(line, True, colour)
            screen.blit(font_surface, (tx, ty))

            y_offset += fh
        
        return y_offset,fw

twituser = "@elonmusk"
twitbody = "something something one two three hello this is a random text sample something something one two three hello this is a random text sample"

# activate the pygame library
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
 
# define the RGB value for white,
#  green, blue colour .
grey = [200,200,200]
lblue = [205,205,255]
dblue = [50,50,100]
white = [255,255,255]
black = [0,0,0]
 
# assigning values to X and Y variable
X = 1280
Y = 720
 
# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y))
 
# set the pygame window name
pygame.display.set_caption('Show Text')
 
# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('Roboto-Light.ttf', 16)
 
# create a text surface object,
# on which text is drawn on it.
text = font.render(twituser, True, lblue, dblue)
 

chosenw = 800
choseny = 400
chosenx1 = 0
choseny1 = Y-choseny

tweetcount = 0
for i in range(len(lyrics)):
    for j in range(len(lyrics[i])):
        twituser = theauthor
        print(len(lyricids[i]))
        print(len(lyricids[i][j]))
        print(lyricids[i][j][0])
        twitbody = tweets[lyricids[i][j][0]]
        yoffset = 0
        fwy=0
        bodyfontsize = 0
        while yoffset <= choseny and fwy <= chosenw:
            bodyfontsize+=1
            bodyfont = pygame.font.Font('Roboto-Light.ttf', bodyfontsize)
            yoffset,fwy = renderTextCenteredAt(twitbody, bodyfont, black, chosenx1, choseny1, display_surface, chosenw)
        bodyfontsize-=2
        bodyfont = pygame.font.Font('Roboto-Light.ttf', bodyfontsize)
        display_surface.fill(white)
        renderTextCenteredAt(twitbody, bodyfont, black, chosenx1, choseny1, display_surface, chosenw)
        alooking = list(twitbody)
        allGoodf = True
        newgood = ""
        if alooking[0] == "@":
            for t in range(len(alooking) - 1):
                if alooking[t] == " ":
                    if alooking[t+1] == "@":
                        allGoodf = True
                    else:
                        break
                if allGoodf == True:
                    newgood += alooking[t]
            renderTextCenteredAt(newgood, bodyfont, [131,238,255], chosenx1, choseny1, display_surface, chosenw)
                

        font_surface = bodyfont.render(twituser, True, black)
        authorx = chosenx1
        authory = choseny1 - bodyfontsize*1.5
        #display_surface.blit(font_surface, (authorx, authory))
        imagefile = "tweetimg"+str(tweetcount)+".png"
        pygame.image.save(display_surface,imagefile)
        os.rename(imagefile,'images/'+imagefile)
        tweetcount+=1

from moviepy.editor import *
import math

clip = ColorClip(size = (1280,720), color = [255,255,255])

senClips = []
totalrhymetime = 0

bgrMusic = AudioFileClip('backgroundsong.mp4')

twtlkcount = 0
for i in range(len(lyrics)):

    for j in range(len(lyrics[i])):
        location = "C:/Users/jacob/Desktop/twitterAPI/audios/"
        dir = str(format(i,'05d'))
        path = os.path.join(location,dir)
        os.chdir(path)

        utFile = AudioFileClip("output"+str(format(j,'05d'))+".mp3")

        location = "C:/Users/jacob/Desktop/twitterAPI/images/"
        os.chdir(location)

        tweetfile = "tweetimg"+str(twtlkcount)+".png"
        twtlkcount+=1
        tweetclip = ImageClip(tweetfile)
        workClip = tweetclip
        workClip = workClip.set_audio(utFile)
        workClip = workClip.set_duration(utFile.duration)

        rbeats = math.ceil(workClip.duration/aps)
        rtimes = rbeats*aps
        restofaudio = rtimes - workClip.duration
        blankClip = clip
        blankClip = blankClip.set_duration(restofaudio)

        totalrhymetime += blankClip.duration + workClip.duration
        if totalrhymetime < bgrMusic.duration:
            senClips.append(blankClip)
            senClips.append(workClip)
        else:
            break

senTog = concatenate_videoclips(senClips,method="compose")

location = "C:/Users/jacob/Desktop/twitterAPI/"
os.chdir(location)

bgrMusic = bgrMusic.set_duration(senTog.duration)
bgrMusic = bgrMusic.volumex(0.1)

musicAndSpeech = CompositeAudioClip([senTog.audio,bgrMusic])

senTog.audio = musicAndSpeech

senTog.write_videofile("somevideo.mp4",fps=30)




print(tweetdate)

