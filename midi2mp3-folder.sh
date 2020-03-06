#!/usr/bin/env bash


SOUNDFONT=./soundbank-emg.sf2
TMPDIR=./tmp

mkdir -p "$TMPDIR"

if [[ ! -f $SOUNDFONT ]]
then
    echo "Couldn't find the soundfont: $SOUNDFONT"
    exit 1
fi

# find metronic -type f -name "*.mid"



if [ "$#" -lt 2 ]
then
    echo "usage: midi2mp3-folder input-folder output-folder"
    exit 0
else

    find $1 -type f -name "*.mid" -print0 | while IFS= read -r -d $'\0' filepath; 
        do echo "$filepath";
    #   dir=$(dirname "${filename}")
        dir=${filepath%/*}
        reldir=${dir#$1}
        outdir="$2$reldir"
        # echo "$outdir"
        mkdir -p "$outdir"

        filename=${filepath##*/}
        filename=${filename%.*}
        WAVFILE="$TMPDIR/${filename}.wav"
        outfile="$outdir/$filename.mp3"
        # echo "${outfile}"


        fluidsynth -F "${WAVFILE}" $SOUNDFONT "${filepath}" && \
            lame -m l -b 16 "${WAVFILE}" "${outfile}" && \
            rm "${WAVFILE}"

    done

    # for filename in "$@"
    # do
    #     echo "${filename}"
    #     WAVFILE="$TMPDIR/${filename##*/}"

    #     fluidsynth -F "${WAVFILE}" $SOUNDFONT "${filename}" && \
    #         lame "${WAVFILE}" && \
    #         rm "${WAVFILE}"

    #     # fluidsynth -F "${WAVFILE}" $SOUNDFONT "${filename}" && \
    #     #     lame "${WAVFILE}" && \
    #     #     rm "${WAVFILE}"
    # done
fi