#!/bin/bash
dir=$1

for filename in $dir/*.pdf; do
  [ -e "$filename" ] || continue
  echo $filename
  pdftotext "$filename" - >> ./output.xt
done
