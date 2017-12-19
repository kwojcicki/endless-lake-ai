# endless-lake-ai

https://groups.google.com/forum/#!msg/wxpython-users/S1_PU0e5G4I/IFzY-cWoBwAJ Installation steps:

==============================================================
= ----- How to install wxPython Phoenix - The Easy Way ----- =
==============================================================

===========
= --- About --- =
===========

Last update : Monday the 21st, January 2016.

This tutorial deals with wxPython Phoenix installation on Ubuntu.

I am using Ubuntu 12.04 LTS - 64 bits.

Note :     Ubuntu 12.04 LTS comes with Python 2.7.3. You might have to make sure
    that Python is installed on your computer :

    - Type "python" in the console to run the python interpreter. You will also
    see the current version.

    Example :     damien@Ubuntu1204VB:~$ python
            Python 2.7.3 (default, Jun 22 2015, 19:33:41)
            [GCC 4.6.3] on linux2


=============
= --- Let's go --- =
=============

1. Install some modules :

    - dpkg-dev
    - build-essential
    - python2.7-dev # use appropriate Python version
    - libwebkitgtk-dev
    - libjpeg-dev
    - libtiff-dev
    - libgtk2.0-dev
    - libsdl1.2-dev
    - libgstreamer-plugins-base0.10-dev
    - libnotify-dev
    - freeglut3
    - freeglut3-dev


Note :     You can install all of them at once using the following command :

    sudo apt-get install dpkg-dev build-essential python2.7-dev libwebkitgtk-dev
    libjpeg-dev libtiff-dev libgtk2.0-dev libsdl1.2-dev libgstreamer-plugins-base0.10-dev
    libnotify-dev freeglut3 freeglut3-dev

Note : Your password will be asked.


2. Go to http://wxpython.org/Phoenix/snapshot-builds/ and download the latest .tar.gz

Example : wxPython_Phoenix-3.0.3-dev1836+f764b32.tar.gz

Note :    A .tar.gz file is called a tarball.


3. Untar the tarball : tar -xvzf wxPython_Phoenix-3.0.3-dev1836+f764b32.tar.gz


4. Go into the directory : cd wxPython_Phoenix-3.0.3-dev1836+f764b32.tar.gz

Note : You can/should use the tabulation key for auto-completing.


5. Install : sudo python setup.py install

Note :    Your password will be asked to copy files.


6. Check if the module works :

    6.1 Make sure your current folder is your home folder : type cd

    6.2 Do as follows :

Example : damien@Ubuntu1204VB:~$ python
      Python 2.7.3 (default, Jun 22 2015, 19:33:41)
           [GCC 4.6.3] on linux2
      Type "help", "copyright", "credits" or "license" for more information.
      >>> import wx
      >>> wx.version()
      '3.0.3.dev1836+f764b32 gtk2 (phoenix)'
