set nf [molinfo top get numframes]

set refsel [atomselect top "protein and name CA" frame 0]

for {set i 0} {$i < $nf} {incr i} {
	molinfo top set frame $i
	set sel [atomselect top "protein and name CA"]
	set all [atomselect top all]
	set tm [measure fit $sel $refsel]
	$all move $tm
	set c [measure center [atomselect top "protein and backbone and noh"]]
	set movevec [vecscale $c -1.0]
	$all moveby $movevec
	$all writepdb frame_$i.pdb
	$sel delete
	$all delete
}

$refsel delete
