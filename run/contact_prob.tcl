set nf [molinfo top get numframes]


set firstresidue 8
set lastresidue 40

set totalresiduecontact {}
for {set i $firstresidue} {$i <= $lastresidue} {incr i} {
        lappend totalresiduecontact 0.0
}

set count 0.0
for {set k 1250} {$k < $nf} {incr k} {
        molinfo top set frame $k
        set residues [lsort -unique [[atomselect top "protein and (within 3 of resname LSP)"] get resid]]
        set residuecontact {}
        set count [expr $count+1]
	for {set j $firstresidue} {$j <= $lastresidue} {incr j} {
                if {[lsearch -exact $residues $j] >= 0} {
                        lappend residuecontact 1.0
                } else {
                        lappend residuecontact 0.0
                }
        }
        set totalresiduecontact [vecadd $totalresiduecontact $residuecontact]
}
puts "residue contact probability $totalresiduecontact"
set avgresiduecontact [vecscale [expr 1.0/$count] $totalresiduecontact]

set fp1 [open "LSP_protcontact_prob.dat" w]
for {set s $firstresidue} {$s <= $lastresidue} {incr s} {
        set index [expr $s-$firstresidue]
        set fraction [lindex $avgresiduecontact $index]
        puts $fp1 "$s $fraction"
}
flush $fp1
close $fp1
puts "contact probability calculation done"

