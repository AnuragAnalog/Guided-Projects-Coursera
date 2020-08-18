#!/bin/bash

sudo adduser $1

array=(Documents Downloads Project)

for i in "${array[@]}"
do
    sudo cp -r /home/template/$i /home/$1/.
    sudo chown -R $1 /home/$1
    sudo chgrp -R $1 /home/$1
done