#!/bin/bash

for i in {0..99}
do
	#let j="$i-10"
	echo "Currenty performing docking dock.${i}.conf"
	/Scr/ssen/software/autodock_vina_1_1_2_linux_x86/bin/vina --config conf_files/dock.${i}.conf --cpu 8
done
