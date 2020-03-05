from music import *

import os

#noteE4 = Note(E4, HN)        # create a middle C half note
#
#noteC4 = Note(C4, HN)        # create a middle C half note

#def tick(note):
#   Play.midi(note)            # and play it!

#
#tempo = 60
#minutes = 30
#bars = 4

def writeMid(folder,minutes,tempo,bars):
   filename = '{folder}/B{bars}T{tempo}M{minutes}.mid'.format(folder=folder,minutes=minutes,tempo=tempo,bars=bars)
   print filename
#m = Metronome(60, [1])
#m.add(tick, parameters=[noteE4], desiredBeat=1, repeatFlag=True)
#m.add(tick, parameters=[noteC4], desiredBeat=0, repeatFlag=True)

#m.show()
#m.soundOn()
#m.start()

   ticks = minutes * tempo
   range_ticks = range(ticks)
# theme (notice how we line up corresponding pitches and rhythms)
   pitches1   = [F4 if i%bars==0 else D4 for i in range_ticks]
   durations1 = [QN for i in range_ticks] 
 
# create an empty phrase, and construct theme using pitch/rhythm data
   theme = Phrase()   
   theme.addNoteList(pitches1, durations1)
 
# set the instrument and tempo for the theme
   theme.setInstrument(SYNTH_BASS_2)
   theme.setTempo(tempo)
 
# play it
#Play.midi(theme)
   Write.midi(theme, filename)
   

tempo_arr = [120,90,60,40,30,20]
minutes_arr = [30,20,15,10,5,3]
bars_arr = [4,3,2,1]

for minutes in minutes_arr:
   for bars in bars_arr:
      for tempo in tempo_arr:
         folder = './metronic/M{minutes}/T{tempo}'.format(minutes=minutes,tempo=tempo)
         try: os.makedirs(folder)
         except OSError: pass
         writeMid(folder, minutes,tempo,bars)