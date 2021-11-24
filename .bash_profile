#
# ~/.bash_profile
#
#export PATH="${PATH}:/home/_2k/"


alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'

if [ "${tty}" = /dev/tty1 ]; then
	exec startx
fi
sleep 0.5
/home/_2k/.screenlayout/layout.sh

[[ -f ~/.bashrc ]] && . ~/.bashrc
