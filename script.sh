counter=1
for elem in $(ls scheme*)
do
	echo $elem
	echo "res$counter.csv"
	echo $counter
	python3 main.py $elem "res$counter.csv"
	let "counter += 1"
done