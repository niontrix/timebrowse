# TimeBrowse

TimeBrowse is a Windows VSS like utility for NILFS2 and Nautilus.
It comes with a snapshot manager and nautilus extension.
The Snapshot manager manages the snapshot of NILFS.
The Nautilus extension extends the nautilus property dialog with a column to show the history of the selected item.

## Install

Please read README in each directory on how to install the files.

## Notes on this version of TimeBrowse

This version is a fork of the [original TimeBrowse](https://github.com/timebrowse/timebrowse)
that makes it work with [systemd](https://wiki.archlinux.org/index.php/systemd) in addition to [sysV](https://wiki.archlinux.org/index.php/SysVinit) as your init system.
I also upgraded the code to python 3 and Gtk+ 3.0. It currently works with Gnome 3.30.

## Showcase of TimeBrowse in Nautilus

![Showcase](showcase.gif)
