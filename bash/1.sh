#!/bin/bash

read count
A=0
for i in count; do
    read C
    A=$(( $A + $C ))
    echo $A
done