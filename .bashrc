#
# ~/.bashrc
#

alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

# set vim mode in bash
set -o vi

# remap escape to kj
bind '"kj":"\e"'


source /usr/share/doc/pkgfile/command-not-found.bash

# replace with a better ascii generator
neofetch


