#!/bin/bash
# Gzowo Dataset: transcode source videos to web MP4 (hardware encoder) and cut evenly spaced keyframes into media/klatki/.
set -u
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
SCRATCH="$1"
OUT="$ROOT/media/wideo"
FR="$ROOT/media/klatki"
DUMP="/Users/jurek/Downloads/Claude/Gzowo_Dataset"
GAL="/Users/jurek/Gzowo_Gallery/Movies"
PROJ="/Users/jurek/Downloads/Claude/Projects"
mkdir -p "$OUT" "$FR"

enc() {
  local src="$1" id="$2" vb="$3"
  [ -f "$OUT/$id.mp4" ] && return
  nice -n 10 ffmpeg -v error -y -hwaccel videotoolbox -i "$src" -map 0:v:0 -map 0:a:0? \
    -vf "scale=w='if(gt(iw,ih),min(1280,iw),-2)':h='if(gt(iw,ih),-2,min(1280,ih))',fps=30,format=yuv420p" \
    -c:v h264_videotoolbox -b:v "$vb" -c:a aac -b:a 96k -ac 2 -movflags +faststart -threads 2 "$OUT/$id.tmp.mp4" \
    && mv "$OUT/$id.tmp.mp4" "$OUT/$id.mp4"
  echo "enc $id $(du -h "$OUT/$id.mp4" | cut -f1)"
}

cp_as() {
  local src="$1" id="$2"
  [ -f "$OUT/$id.mp4" ] || cp "$src" "$OUT/$id.mp4"
  echo "copy $id"
}

frames() {
  local id="$1" n="$2"
  local f="$OUT/$id.mp4"
  [ -d "$FR/$id" ] && return
  mkdir -p "$FR/$id"
  local dur
  dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f")
  for i in $(seq 1 "$n"); do
    local t
    t=$(python3 -c "print(round(($i-0.5)*$dur/$n,2))")
    local label
    label=$(python3 -c "print('%02d_%04ds' % ($i, int(float('$t'))))")
    nice -n 10 ffmpeg -v error -y -ss "$t" -i "$f" -frames:v 1 -vf "scale=w='if(gt(iw,ih),960,-2)':h='if(gt(iw,ih),-2,960)'" -q:v 4 -threads 2 "$FR/$id/$label.jpg"
  done
  echo "frames $id $n"
}

Z="$SCRATCH/rakietomania"
cp_as "$Z/VID-20251019-WA0005.mp4" "rakieta_2025-10-19_start-z-daleka-pole"
cp_as "$Z/VID-20251019-WA0006.mp4" "rakieta_2025-10-19_w-locie-niebo"
cp_as "$Z/VID-20251019-WA0008.mp4" "rakieta_2025-10-19_WA0008"
cp_as "$Z/VID-20251019-WA0009.mp4" "rakieta_2025-10-19_WA0009"
cp_as "$Z/VID-20251101-WA0007.mp4" "rakieta_2025-11-01_start-z-daleka-laka"
cp_as "$Z/VID-20251101-WA0009.mp4" "rakieta_2025-11-01_WA0009"
cp_as "$Z/VID-20251129-WA0002.mp4" "rakieta_2025-11-29_WA0002"
cp_as "$Z/VID-20251129-WA0003.mp4" "rakieta_2025-11-29_start-z-daleka-2"
for id in rakieta_2025-10-19_start-z-daleka-pole rakieta_2025-10-19_w-locie-niebo rakieta_2025-10-19_WA0008 rakieta_2025-10-19_WA0009 rakieta_2025-11-01_start-z-daleka-laka rakieta_2025-11-01_WA0009 rakieta_2025-11-29_WA0002 rakieta_2025-11-29_start-z-daleka-2; do frames "$id" 6; done

enc "$GAL/2B/DANCE.mp4" "dropsik_dance" 1500k; frames "dropsik_dance" 12
enc "$DUMP/Movie on 30-11-2020 at 19.45.mov" "kamerka_2020-11-30_jurek-i-rysio" 900k; frames "kamerka_2020-11-30_jurek-i-rysio" 6
enc "$PROJ/vfx-gzowo/footage/shot01.mp4" "dom-z-zewnatrz_2026-07-28" 2500k; frames "dom-z-zewnatrz_2026-07-28" 4
enc "$GAL/3C (coming soon)/20250525_190322.mp4" "sala-3c_2025-05-25" 1500k; frames "sala-3c_2025-05-25" 8
enc "$PROJ/vfx-narek-desk/footage/source_1125.MOV" "sciana-domu_2026-08-07" 2000k; frames "sciana-domu_2026-08-07" 5
enc "$PROJ/plaża w gzowie/photos/IMG_1137.MOV" "plaza_2026-08-08" 2000k; frames "plaza_2026-08-08" 8
enc "$PROJ/Gzowo House/capture/dom.mov" "dom-wnetrze_2026-07-28" 1800k; frames "dom-wnetrze_2026-07-28" 16
enc "$DUMP/2023-08-29 19-32-08.mkv" "kalakasan_2023-08-29_200-memes" 900k; frames "kalakasan_2023-08-29_200-memes" 6
enc "$DUMP/Jurek STRAREM___.mkv" "kalakasan_ninjago-stream" 800k; frames "kalakasan_ninjago-stream" 12
echo ALLDONE
du -sh "$OUT" "$FR"
