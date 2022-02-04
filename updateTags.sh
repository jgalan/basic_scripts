# I place this script on my git directory and point those source repositories I want to have on my tags file

# I add this script to a cronjob so that it is updated each night.
# 53 3 * * * /home/jgalan/git/updateTags.sh

# Then I add the tags file to my VIM configuration file: See [.vimrc](.vimrc) at this repository.

cd $HOME/git/
rm tags
ctags-exuberant -a --c-kinds=+p --exclude=build --exclude=install --exclude=.git --exclude=log -R $HOME/rest-framework/source/*
ctags-exuberant -a --c-kinds=+p --exclude=Build --exclude=Install --exclude=.git --exclude=log -R $HOME/apps/garfield6/*
ctags-exuberant -a  --c-kinds=+p --exclude=build --exclude=etc --exclude=install --exclude=.git --exclude=log -a -R $HOME/apps/root-6.24.02/source/*
