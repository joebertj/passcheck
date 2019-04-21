for i in `ls /var/local`
do
	cp /var/local/$i test.data
	exit
done
