#!/bin/bash

./hello 1 > output_1.txt &
./hello 2 > output_2.txt &
./hello 3 > output_3.txt &
./hello 4 > output_4.txt &
./hello 5 > output_5.txt &
./hello 6 > output_6.txt &
./hello 7 > output_7.txt &
./hello 8 > output_8.txt &
./hello 9 > output_9.txt &
./hello 10 > output_10.txt &

wait
echo "Jobs finalizados!"
