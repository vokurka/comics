
for file in Export*
do
 # do something on $file
 tail -n +9 "$file" > "1st_step/$file"
done

