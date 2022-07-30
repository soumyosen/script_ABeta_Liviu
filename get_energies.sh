#!/bin/bash

# This script is to get average delta G (affinity) per pose
#mkdir -p energy.files

for j in {0..99}
do
	
	grep "REMARK VINA RESULT:" ./ligand_pdbqt/$j.LSP.pdbqt >> ./energy_files/all_energ.affi.log
        
	
done


awk '{ print $4 }' ./energy_files/all_energ.affi.log > ./energy_files/only_energy.log
