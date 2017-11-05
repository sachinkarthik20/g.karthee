#!/bin/bash
IFS=$'\n'
matchstring=$1
linenumber=`grep -n $matchstring udemy.html | awk -F":" '{print $1}'`
sec=1
for line in `sed -n "${linenumber}p" udemy.html | awk -F"<span translate=\"\"><span>Section:" '{out=""; for(i=2;i<=NF;i++){out=out"\n"$i}; print out}'`; 
do
	echo "Section $sec:"
	echo "==========="
	echo -e $line | grep -oP '(?<=Lecture\</span\> \<span\>).+?(?=\</span\> \</span\> \<span class=\"lecture__item__link__time mr20\")' | sed 's/<\/span> <\/span> <\/span><!----> <!----> <span class="lecture__item__link__name">//g'; 
	echo ""
	sec=$((sec+1))
done

