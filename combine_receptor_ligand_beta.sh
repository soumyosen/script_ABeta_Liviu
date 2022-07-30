#!/bin/tcsh

set start = $1
set end = $2

foreach i (`seq $start 1 $end`)
	
  echo "Combining for frame file ${i}"	
  grep -v '^END' ./receptor_pdb/frame_${i}.pdb > ./receptor_pdb/receptor_try.pdb  
  foreach j (`seq 0 1 9`)  
    grep -v '^CRYST1' ./energy_files/${i}.${j}.ligand_nonrigid_beta.pdb > ./energy_files/ligand_try.pdb
    cat ./receptor_pdb/receptor_try.pdb ./energy_files/ligand_try.pdb > ./complex_pdb_beta/${i}.${j}.complex_NRL_beta.pdb
    rm -f ./energy_files/ligand_try.pdb
  end	
  rm -f ./receptor_pdb/receptor_try.pdb	
end


