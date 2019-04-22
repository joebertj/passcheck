cd $1
datadir=~/rawdata
for i in `ls $datadir`
do
	echo "Working on $i"
	cp $datadir/$i ../test.data
	python batchwrite.py
done
