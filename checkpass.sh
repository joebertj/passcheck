shaone=$(echo -n "$2" | sha1sum | awk '{print toupper($1)}')
python $1/getdata.py $shaone
