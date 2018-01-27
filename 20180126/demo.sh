#!/bin/bash
input_file="$5"
var1=`egrep -n "$1|</$2>" $input_file | grep -A 1 "$1" | head -1 | awk -F : '{print $1}'`
var2=`egrep -n "$1|</$2>" $input_file | grep -A 1 "$1" | tail -1 | awk -F : '{print $1}'`
echo "$var1,$var2";
sed "$var1,$var2 s/$3/$4/g" $input_file

