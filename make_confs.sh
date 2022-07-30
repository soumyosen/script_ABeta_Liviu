#!/bin/bash

#ZRN=$1
start=$1
end=$2
#NCPUS=$1

#pwd=`eval pwd`

for i in `seq $start 1 $end`;
do
	file=conf_files/dock.${i}.conf

	echo "receptor = ./receptor_pdbqt/${i}.frame.pdbqt" >> $file 
	echo "ligand = ./ligand_pdbqt/LSP.pdbqt" >> $file

	echo "center_x = 0.0" >> $file
	echo "center_y = 0.0" >> $file
	echo "center_z = 0.0" >> $file

	echo "size_x = 100" >> $file
	echo "size_y = 80" >> $file
	echo "size_z = 140" >> $file

#randomize_only

	echo "exhaustiveness = 50" >> $file

#cpu = 8

echo "num_modes  = 10" >> $file
echo "energy_range = 10" >> $file

echo "out = ./ligand_pdbqt/${i}.LSP.pdbqt" >> $file
echo "log = ./log_files/${i}.frame.log" >> $file

	#echo $i

	#/home/baylonc2/bin/vina --receptor pdbqts/8300.${i}.frame.pdbqt --ligand ligand.pdbqt --center_x 4 --center_y 6 --center_z 53 --size_x 20 --size_y 20 --size_z 15 --cpu $NCPUS --num_modes 10 --energy_range 5 --out pdbqts.ligand/${i}.ligand.pdbqt --log ligand.log/${i}.log 


done
