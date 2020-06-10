cd $1
datadir=$2
for i in `ls $datadir`
do
	echo "Working on $i"
	python3 batchwrite.py $datadir/$i
done
