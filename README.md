# Web Basic
This is a project I made to cover the very basics of building a super simple web application using the [Python programming language](https://www.python.org/) and the [Flask web framework](http://flask.pocoo.org/).

I wrote this for anyone who might know a bit of Python from a basic programming class, but who needs a good place to start for web development.

*****
<!--
## See the App Running, Live!
I currently host a copy of this app on Heroku, so you can check it out for yourself and see it in action. It's pretty unimpressive for an end-user, but the point is that it's something you could easily build yourself with no experience in almost no time.

* [Homepage]()
* [A Static Page that Uses Templates]()
* [A Dynamic Page that Responds to Query Arguments]()
-->
## Getting the App Running On You Computer
In order to work on the code and test it on your computer, we'll need to quickly setup your computer to be able to run Flask applications. This might seem like a lot of work but **don't worry because you'll really on have to do this once.** It might take a few confusing minutes before you even get started, but unfortunately the tedium is necessary to make sure your computer is ready to work on the app.

First, you'll want to pull up your system's terminal window. I'm going to assume you're working on a Mac OSX computer. Open the "Terminal" app by searching for it in spotlight search, or opening it from the Applications folder. We're going to run two commands to make sure our system is all setup.

### Ensuring Python is Installed
First, type `python` and hit enter. You should see something like this

    Python 2.7.5 (default, Aug 25 2013, 00:04:04) 
    [GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

This ensures that you have Python installed on your system, which we'll need to run our app. Note that your version number might look a little different, but as long as your version of Python is 2.6 or greater, you should be fine.

If you want, you can start typing and hit enter, you'll be writing Python code! If you're ready to move on, just hit `Ctrl+D` to exit out of the Python interactive interpreter.

### Ensuring Git is Installed
The next command we're goint to try running is called "git" and it's a program that's used to keep track of changes to files over time. This is known as "version control" and is super important if you'll be working on real apps.

Git allows you to see all of the different changes that were made to the app over time, and what was added and removed every time a change was made. This lets you "step through" the changes and see the stages the app went through as it was being built.

We'll also use git to download a copy of the app on your computer. Try running the `git` in your terminal window and see what happens. If you see a big output about usage and commonly used commands, then you already have it installed on your system and you're ready to go.

Unfortunately, most new Macs don't have git installed by default, so you'll probably need to install it [from here](http://sourceforge.net/projects/git-osx-installer/). Once you download the installer and run through all the steps, you should be able to close and re-open the terminal application, type `git` and press enter, and see some output that looks like this:

	usage: git [--version] [--help] [-C <path>] [-c name=value]
	           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
	           [-p|--paginate|--no-pager] [--no-replace-objects] [--bare]
	           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
	           <command> [<args>]

	The most commonly used git commands are:
	   add        Add file contents to the index
	   bisect     Find by binary search the change that introduced a bug
	   branch     List, create, or delete branches
	   checkout   Checkout a branch or paths to the working tree
	   clone      Clone a repository into a new directory
	   commit     Record changes to the repository
	   diff       Show changes between commits, commit and working tree, etc
	   fetch      Download objects and refs from another repository
	   grep       Print lines matching a pattern
	   init       Create an empty Git repository or reinitialize an existing one
	   log        Show commit logs
	   merge      Join two or more development histories together
	   mv         Move or rename a file, a directory, or a symlink
	   pull       Fetch from and integrate with another repository or a local branch
	   push       Update remote refs along with associated objects
	   rebase     Forward-port local commits to the updated upstream head
	   reset      Reset current HEAD to the specified state
	   rm         Remove files from the working tree and from the index
	   show       Show various types of objects
	   status     Show the working tree status
	   tag        Create, list, delete or verify a tag object signed with GPG

	'git help -a' and 'git help -g' lists available subcommands and some
	concept guides. See 'git help <command>' or 'git help <concept>'
	to read about a specific subcommand or concept.


### Downloading the Project Locally Using Git
Alright, now that we have ensured your system has both Python and Git installed, we're ready to start getting the application setup. Note that we'll be running a bunch of commands in the same Terminal window, so it's important to leave that up the whole time.

First, you'll want to move to your desktop by running

`cd ~/Desktop`

And then run the following command to download a copy of the app onto your desktop:

`git clone git@github.com:hartleybrody/web_starter.git`

You should see the folder for the app appear on your desktop with some folders and files inside it!

You're almost ready to being working on the app, but first we're going to get a "development environment" running on your local computer so that you can  make changes and test what they look like quickly.

### Setting up the Python Environment
Still in your terminal window, we're going to install "pip" which is a tool for managing Python libraries. Run the following:

`sudo easy_install pip`

Note that you might need to enter your user account's password to approve the install. Don't worry if you start typing and nothing shows up, that's how the terminal handles password fields (the same way that browsers show dots or stars when you type a password into a web form). Hit "enter" when you're done typing your password to continue the installation.

Once pip is installed, the only thing that's left is to install the Python packages that our app requires. You'll want to make sure you're in the same folder as the project, so you'll probably need to run

`cd ~/Desktop/web_starter`

Then, to install the packages, you run

`pip install -r requirements.txt`

This tells pip to install all of the packages listed inside the `requirements.txt` file. That might take a few seconds to download and install everything, and then everything is ready to go!

### Starting Your Local Server
If you're still hanging in there, nice work! You will almost never have to run those steps again when you're first starting out, so you should be able to let them slide right out of your brain. Go take a break if need be to let your mind rest (but leave the Terminal window open).

Now that we're ready to start working on the app, simply type

`python app.py`

and you should see the following output

	* Running on http://127.0.0.1:5000/
	* Restarting with reloader

Now, open up your browser and navigate to `http://localhost:5000/` and you should see the homepage of your app! Wooho!

## Working On the App
Using your favorite text editor (not Microsoft Word, try TextEdit), open the `app.py` file that's inside the app folder and start reading what's inside. There are tons of comments -- pieces of text that are meant for humans and are ignored by the program -- with every line of code, so it should be easy to read along and see what's happening.

Once you've read through the basics, you'll be itching to start tinkering. Feel free to edit the code and play with your app. The local development server should reload every time you change a file, so edit something and then go see your changes by refreshing the app in your browser.

If you want to learn more about other functions and tools that the Flask framework provides (like user sessions and showing messages and redirecting requests), check out the [Flask Quickstart Guide](http://flask.pocoo.org/docs/quickstart/) for more.

## Contribute!
If there are things you'd like to see added to this app, feel free to send me a pull request. Please keep in mind that the audience is people who are making their first foyer into web development, so anything that's too complex will be rejected.

Things I'd love to add examples of:

* Using SQL Alchemay to create an ORM
* Using Users and Sessions
* Template Inheretence
* Writing some basic tests

