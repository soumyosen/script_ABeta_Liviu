#!/bin/tcsh

set start = $1
set end = $2

#num of reps
foreach q (`seq $start 1 $end`)

	/Scr/ssen/software/mgltools_x86_64Linux2_1.5.6/bin/pythonsh /Scr/ssen/software/mgltools_x86_64Linux2_1.5.6/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_receptor4.py -r ./receptor_pdb/frame_$q.pdb -o ./receptor_pdbqt/$q.frame.pdbqt -v -U nphs_lps_waters	

end
