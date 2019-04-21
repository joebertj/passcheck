for i in `ls /var/local`
do
	echo "Working on $i"
	cp /var/local/$i test.data
	python batchwrite.py
done
