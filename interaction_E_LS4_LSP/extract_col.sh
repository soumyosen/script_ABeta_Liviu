#!/bin/bash

files=("energy_LSP" "energy_LS4_PI" "energy_LS4_FI")

for file in "${files[@]}"
do
	cp $file.dat temp.traj
	awk '{print $3}' temp.traj > temp_elec.traj
	awk '{print $4}' temp.traj > temp_vdW.traj
	paste -d, temp_elec.traj temp_vdW.traj > $file.traj
	rm -f temp*
done


