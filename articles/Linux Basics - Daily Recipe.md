# Linux Basics - Daily Recipe

Among an ocean of Linux commands, some are used much more frequently than others. Here is the listing of some of the most common ones:

- `pwd`: Show your current working directory
- `cd`: Change directory
- `ls`: Show files in current working directory
- `cat`: Show content of a file
- `mkdir`: Create a directory
- `touch`: Create a file
- **`vim`**: Edit / Create a file
- `cp`: Copy a file/ directory to a specified location
- `mv`: Move a file / directory to a specified location
- `rm`: Remove files / directories

> Tip: use `man` can help show detailed usage of all commands listed above. These commands are used so frequently, so their usage should be kept in your head.

In this chapter, we are going to talk about common tasks such as navigating and manipulating directories and files, using the above listing as basics. Commands are created for tasks, knowing where they were originally brought to us helps you memorize it better.  And these tasks are quite appropriate for Linux beginners.

## Navigating directories and files

Usually, you will need to use `pwd` and `cd` to navigate to your desired working directory at the very first step when you are going to perform some shell tasks. `ls` can help you make sure you are really in that directory by showing you files in that directory. `ls` has a lot of useful options to go with, such as `ls -l` will give you a better view of files, and `ls -al` can show hidden files. Some other commands, such as `more`, `less` and `vim` can also help you view file content, and will be discussed later in other chapters.

## Manipulating directories and files

You have already known how to navigate and browse through directories. The next step is then to make changes, `mkdir` and `touch` are usually the way to go. `vim` is mode advanced for manipulating files, a separate chapter will be discussing it.

> Tip: always double check when you execute `rm`. If you want to perform `rm -rf *`, do let yourself know, there is no way to regret and go back!
