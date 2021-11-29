# Linux Basics - First Step

Whenever you open a terminal and want to perform some kind of tasks, you start to type Linux commands. But there could be thousands of commands and even a much larger amount of options to go with these commands. How could you remember all of them? The answer is impossible. You have to put up with this fact. What you can do is to get familiar with commonly used commands, and know where to get help when needed.

There are a lot of online materials you can refer to when you come accross questions, but what if you cannot access internet, or you want a more quicker way to get help? Here you could find one command that is very useful: `man`. You can use `man` to get a detailed documentation about your queried command within your terminal. For example, when you dont' remember the usage of `ls`, you could type `man ls`, and the output you see will show you what you want:

```shell
LS(1)

NAME
       ls - list directory contents

SYNOPSIS
       ls [OPTION]... [FILE]...

DESCRIPTION
       List information about the FILEs (the current directory by default).  Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.

       Mandatory arguments to long options are mandatory for short options too.

       -a, --all
              do not ignore entries starting with .
...
```
Type `q` can exit current pop-up view.

In addition, there is an alternative way to find usage of a command, usally append ` -h` or `--help` to the command can get you there. For example, `ls --help` shows you the usage of Linux command `ls`. You can choose whatever approach to get help as you like.
