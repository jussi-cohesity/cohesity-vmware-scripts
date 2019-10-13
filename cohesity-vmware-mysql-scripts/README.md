# Example scripts to enable application aware backups for MySQL running in VMware Linux VM

## Requirements

This script requires VMware Tools to be installed on VM and MySQLdb Python module to be installed.

## Installation

Installation is simple. You need to place pre and post scripts to correct location inside the VM:

* Place pre-free-script to /usr/sbin/pre-freeze-script
* Place post-shaw-script to /usr/sbin/post-thaw-script
* Install MySQLdb python module to Linux

Put quiesce.py and unquiesce.py to /cohesity-backup/ -folder 

Change python scripts to match your encironment

Enable Create App-Consistent backup option for protection job

Have fun!
