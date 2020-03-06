from music import *

import os


#
#mPhrase = Phrase()
#mPhrase.setTempo(105)
# 
## section 1 - chords to be repeated
#pitch1 = [[E4,G4,C5], [E4,G4,C5], [D4,G4,B4], A4, G4, [D4, FS4, A4],
#           [D4, G4, B4], [C4, E4, G4], E4, D4, C4, [G3, B4, D4]]
#dur1   = [DEN,        DEN,        HN,         SN, SN, DEN,
#           DEN,          DQN,          EN, SN, SN, DQN]
# 
## section 2 - embellishing chords
#pitch2 = [A4, B4]
#dur2   = [SN, SN] 
# 
#mPhrase.addNoteList(pitch1, dur1)  # add section 1
#mPhrase.addNoteList(pitch2, dur2)  # add section 2
#mPhrase.addNoteList(pitch1, dur1)  # again, add section 1
# 
#Play.midi(mPhrase)
#######################
#noteE4 = Note(E4, HN)        # create a middle C half note
#
#noteC4 = Note(C4, HN)        # create a middle C half note

#def tick(note):
#   Play.midi(note)            # and play it!

#
#tempo = 60
#minutes = 30
#bars = 4
#

#m = Metronome(60, [1])
#m.add(tick, parameters=[noteE4], desiredBeat=1, repeatFlag=True)
#m.add(tick, parameters=[noteC4], desiredBeat=0, repeatFlag=True)

#m.show()
#m.soundOn()
#m.start()
chord = [C4, E4, G4, C5, C5, E5]

def writeMid(folder,minutes,tempo,bars):
   filename = '{folder}/B{bars}T{tempo}M{minutes}.mid'.format(folder=folder,minutes=minutes,tempo=tempo,bars=bars)
   print filename

   ticks = minutes * tempo
   range_ticks = range(ticks)
# theme (notice how we line up corresponding pitches and rhythms)
#   pitches1   = [F4 if i%bars==0 else D4 for i in range_ticks]
   pitches1   = [chord[i%bars] for i in range_ticks]
   durations1 = [QN for i in range_ticks] 
 
# create an empty phrase, and construct theme using pitch/rhythm data
   theme = Phrase()   
   theme.addNoteList(pitches1, durations1)
 
# set the instrument and tempo for the theme
   theme.setInstrument(BANJO)
   theme.setTempo(tempo)
# play it
#   Play.midi(theme)
   Write.midi(theme, filename)
#   
##
tempo_arr = [120,90,60,40,30,20]
minutes_arr = [30,20,15,10,5,3]
bars_arr = [4,3,2,1]
#
#
#tempo_arr = [60]
#minutes_arr = [30]
#bars_arr = [4]
#
for minutes in minutes_arr:
   for bars in bars_arr:
      for tempo in tempo_arr:
         folder = './metronic/M{minutes}/B{bars}'.format(minutes=minutes, tempo=tempo, bars=bars)
         try: os.makedirs(folder)
         except OSError: pass
         writeMid(folder, minutes,tempo,bars)
         
      
   
