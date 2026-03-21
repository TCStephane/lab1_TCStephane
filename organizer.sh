#!/usr/bin/bash
if [ ! -d "archive" ]; then 
	mkdir archive
fi

timestamp=$(date +"%Y%m%d-%H%M%S")

if [ -f "grades.csv" ]; then
	archived_name="archive/grades_${timestamp}.csv"
	mv grades.csv "$archived_name"

	touch grades.csv

	echo "${timestamp}: Moved grades.csv to ${archived_name}" >> organizer.log
else
	echo "${timestamp}: grades.csv not found, skipping archive." >> organizer.log
fi
