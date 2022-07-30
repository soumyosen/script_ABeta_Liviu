
set first 0
set last 99

for {set i $first} {$i <= $last} {incr i} {	
	mol new $i.LSP.pdb waitfor all
	set nf [molinfo top get numframes]
	for {set j 0} {$j < $nf} {incr j} {
		molinfo top set frame $j
		set all [atomselect top all]
		$all writepdb $i.$j.LSP.pdb
		$all delete
		puts "Frame $i pose $j"
	}
	mol delete all
}

 
