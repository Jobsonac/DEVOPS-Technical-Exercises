#!/bin/sh

BASE_DIR="/home/jobson"
DEST_BASE_DIR="deployPackage/"
ADDED_DIR="${DEST_BASE_DIR}/added"
REMOVED_DIR="${DEST_BASE_DIR}/removed"

>${BASE_DIR}/added.txt
>${BASE_DIR}/removed.txt

cat file_diff.txt |
( 
while read status file; do  
  filepath=$file
  filename=${filepath##*/}
  if [ "$status" = "A" -o "$status" = "M" ]; then
     # Capturing filename into added.txt
     echo "$filename" >> ${BASE_DIR}/added.txt
     echo "Capturing $filename into ${BASE_DIR}/added.txt"
     # Moving file to deployPackage/added
     echo "Moving $filename to ${ADDED_DIR}"
     mv $file ${ADDED_DIR}
  elif [ "$status" = "R" -o "$status" = "D" ]; then
     # Capturing filename into removed.txt
     echo "$filename" >> ${BASE_DIR}/removed.txt
     echo "Capturing $filename into ${BASE_DIR}/removed.txt"
     # Moving file to deployPackage/removed
     echo "Moving $filename to ${REMOVED_DIR}"
     mv $file ${REMOVED_DIR}
  fi
done 
)
