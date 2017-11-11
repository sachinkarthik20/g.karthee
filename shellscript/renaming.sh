#!/bin/bash
IFS=$'\n'
for file in `cat html_files/aws_certification | egrep -v "Section|===|^$"`
do
	filenumber=`echo $file | awk -F":" '{print $1}'`
	filename=`echo $file | awk -F":" '{print $2}'`
	existingfilename=`ls $filename-*`
	newfilename=${filenumber}-`echo ${existingfilename} | sed 's/ /_/g'`
	echo "exist: $existingfilename"
	echo "new: $newfilename"
	mv "$existingfilename" $newfilename
done
