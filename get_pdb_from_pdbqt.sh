#!/bin/tcsh

set start = $1
set end = $2

foreach q (`seq $start 1 $end`)
	
  echo "Converting file ${q} pdbqt -> pdb"	
  set file_name2="${q}.LSP"
  
  grep '^HETATM\|^ATOM\|^MODEL\|^REMARK\|^USER\|^TER\|^ENDMDL' ./ligand_pdbqt/$file_name2.pdbqt | cut -c-66 > ./ligand_pdb/$file_name2.pdb

end
