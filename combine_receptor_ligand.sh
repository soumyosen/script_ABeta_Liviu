#!/bin/tcsh

set start = $1
set end = $2

foreach i (`seq $start 1 $end`)
	
  echo "Combining for frame file ${i}"	
  grep -v '^END' ./receptor_pdb/frame_${i}.pdb > ./receptor_pdb/receptor_try.pdb  
  foreach j (`seq 0 1 9`)  
    grep -v '^CRYST1' ./ligand_pdb/${i}.${j}.LSP.pdb > ./ligand_pdb/ligand_try.pdb
    cat ./receptor_pdb/receptor_try.pdb ./ligand_pdb/ligand_try.pdb > ./complex_pdb/${i}.${j}.complex_LSP.pdb
    rm -f ./ligand_pdb/ligand_try.pdb
  end	
  rm -f ./receptor_pdb/receptor_try.pdb	
end


