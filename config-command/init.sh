#!/bin/bash

mv ~/.bashrc ~/.bashrc.bak
cp ./.bashrc ~/.bashrc
cp ./.git-completion.bash ~/.git-completion.bash
cat ./.bash_aliases > ~/.bash_aliases