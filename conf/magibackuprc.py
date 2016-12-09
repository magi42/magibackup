#!/usr/bin/python

################################################################################
# Hosts

# Have the local host and one remote host
# - mountroot is base mount point for drives.
#   For user-mounted volumes, it is usually under user directory.
hosts = [LocalHost(mountroot="/media"),
         RemoteHost("otherhostname", mountroot="/media/myuserid")]

################################################################################
# Excludes

                 # Backed up separately
home_excludes = ["myuserid/photos",
                 "myuserid/video",

                 # Not backed up at all
                 ".encfs/plain",             # Only back up encryped
                 ".local/share/Trash/*",

                 # Miscellaneous application caches, logs, and such
                 ".cache",
                 ".thumbnails", 
                 ".local/share/Steam",
                 ".m2",
                 ".ivy2",
                 ".xsession-errors",
                 ".mozilla/firefox/*/Cache/*",
                 ".mozilla/firefox/*/storage/*",
                 ".config/google-chrome/Default/Extensions"]

# Get rid off versioning, etc.
pruned_excludes = home_excludes + ["*~", ".svn"] 

################################################################################
# Drive backups

drives = [Drive("SG2TB2016",
                volumes = [PlainVolume("/"),
                           # Not supported currently
                           CryptVolume("/.encfs", "/mirror", "password123")],
                hosts = ["localhost", "otherhostname"],
                backups = [
                    Backup(["/home/myuserid/video"],
                           target = "/",
                           excludes = ["*~", "*/4k/*"])
                    ]),
          Drive("WDMB4T2016",
                volumes = [PlainVolume("/")],
                hosts = ["localhost"],
                backups = [
                    Backup(["/old/home/myuserid"],
                           target = "/mirror/old",
                           excludes = home_excludes),
                    Backup(["/etc"],
                           target = "/mirror",
                           excludes = None,
                           sudo = True),
                    Backup(["/home/myuserid",
                            "/media/new/home/myuserid/data"],
                           target = "/mirror",
                           excludes = home_excludes),
                    Backup(["/home/myuserid/photos",
                            "/media/new/home/myuserid/video"],
                           target = "/mirror",
                           excludes = ["*~", "thumbnails-digikam.db"])]),
          Drive("WD3TB2012",
                volumes = [PlainVolume("/")],
                hosts = ["localhost", "otherhostname"],
                backups = [
                    Backup(["/home/myuserid",
                            "/media/new/home/myuserid/data",
                            "/media/new/home/myuserid/video"],
                           target = "/mirror",
                           excludes = home_excludes),
                    Backup(["/etc"],
                           target = "/mirror",
                           sudo = True),
                    Backup(["/home/myuserid/photos"],
                           target = "/mirror",
                           excludes = ["*~", "thumbnails-digikam.db"])]),
          Drive("KtonmDuo32G",
                volumes = [PlainVolume("/"),
                           #CryptVolume("/.encfs", "/mirror", "password123")
                           ],
                hosts = ["localhost", "otherhostname"],
                backups = [
                    Backup(["/home/myuserid/Dropbox/shared",
                            "/home/myuserid/data/articles",
                            "/home/myuserid/data/manuals",
                            "/home/myuserid/data/datasheets",
                            "/media/new/home/myuserid/data/mp3"
                            ],
                           target = "/mirror",
                           excludes = pruned_excludes)
                ])
          ]
