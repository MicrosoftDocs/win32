---
description: The crumb argument supports full Advanced Query Syntax (AQS) statements and is especially useful as a means of controlling the scope of a search.
title: CRUMB Argument (The Windows Shell)
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 8f87a2b7-7f5a-4629-b881-44bf418b2df0
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# CRUMB Argument (The Windows Shell)

The `crumb` argument supports full Advanced Query Syntax (AQS) statements and is especially useful as a means of controlling the scope of a search. In addition to AQS statments, the `crumb` argument can take a special `location` parameter on Windows Vista and `kind` and `store` parameters on Windows XP, as described later in this topic.

This topic contains the following sections:

-   [Crumb Syntax](#crumb-syntax)
    -   [General Examples](#general-examples)
-   [Using crumb with Vista (location)](#using-crumb-with-vista-location)
    -   [Vista Examples](#vista-examples)
    -   [Constants for Common Folders](#constants-for-common-folders)
    -   [Argument Information](#argument-information)

## Crumb Syntax

The crumb syntax is as follows:


```
crumb=<column>:<value>[,<label>][,<column>:<value>[,<label>]]& 
```



The <column> portion is any property in the property system, and the <value> portion is a valid value for that property. The <label> portion is an optional alias for the property that displays as a user interface hint.

### General Examples


```
crumb=System.Author:paolo&
crumb=store:mapi&
crumb=location:c%3a%5cMyVacationPix,Vacation&
```



## Using crumb with Vista (location)

In the crumb parameter, Windows Vista supports full AQS and also the `location` property, which has a special implementation available only on Windows Vista. You can use either an AQS string or the `location` property within a single crumb parameter, but not both. If the crumb parameter includes AQS, everything else in that crumb parameter is ignored.

The `location` property enables you to specify a path to search. Windows Vista can bypass the Indexer and traverse the directory directly if the location is outside the Indexer's crawl scope. Consequently, these searches may be slower than searches that use the Indexer.

When you specify a `location` property, two additional parameters are supported and optional:



| Parameter | Values                  | Description                                                                                                                                                                       |
|-----------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| inclusion | include, exclude        | Specifies whether the query should include or exclude items from that path. "Include" is the default. Windows Vista does not support exclusions without inclusions. (See example) |
| recursion | recursive, nonrecursive | Specifies whether the search should recurse all subfolders starting from the value defined in the location:<value>. "Recursive" is the default.                             |



 

To scope a search using the **search:** protocol, you have different options depending on the target of the scope.

Folder on a local machine:

-   Use AQS (crumb=folder:<URL-encoded path>)
-   Use location argument (crumb=location:<URL-encoded path>)

Folder on a remote machine/network:

-   Use location argument (crumb=location:<URL-encoded path>)

Folder accessed through a known Universal Naming Convention (UNC) protocol handler:

-   Use AQS (crumb=store:<UNC protocol handler name>)
-   Use location argument (crumb=location:<URL-encoded path>)

### Vista Examples


```
search:query=vacation&crumb=location:shell%3aPersonal,include,recursive&
    
search:crumb=location:c%3a%5cPictures&crumb=location:c%3a%5cPictures%5cDuplicates,,exclude& 
    
search:crumb=location:c%3a%5cDocuments&crumb=kind:pics&
```



The first example executes a search for "vacation" starting at the `shell://Personal` location (a special shortcut to the user's **My Documents** folder), including that folder and all subfolders. See table below.

The second example executes a search within C:\\Pictures, but not in C:\\Pictures\\Duplicates.

The third example executes a search within C:\\Documents, limited to files with the `kind` property set to pics.

### Constants for Common Folders

Windows Vista enables the use of CSIDL values that provide a unique system-independent way to identify special folders used frequently by applications, but which may not have the same name or location on any given system. For example, the system folder may be "C:\\Windows" on one system and "C:\\Winnt" on another.

Use these locations with this syntax:


```
crumb=location:shell%3a<LocationName>&
```



The following table lists the CSIDL values. Refer to [**ShellSpecialFolderConstants**](/windows/desktop/api/Shldisp/ne-shldisp-shellspecialfolderconstants) for more information.



| Name                        | search string                   | Description                                                                                                                                                                            |
|-----------------------------|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ADMINISTRATIVE TOOLS        | ADMINISTRATIVE%20TOOLS          | File system directory that serves as a repository for administrative tools.                                                                                                            |
| APPDATA                     | APPDATA                         | File system directory that serves as a common repository for application-specific data. A typical path is C:\\Documents and Settings\\username\\Application Data.                      |
| CACHE                       | CACHE                           | File system directory that serves as a common repository for temporary Internet files. A typical path is C:\\Documents and Settings\\username\\Temporary Internet Files.               |
| CD BURNING                  | CD%20BURNING                    | Folder containing data to be burned to CD.                                                                                                                                             |
| COMMON ADMINISTRATIVE TOOLS | COMMON%20ADMINISTRATIVE%20TOOLS | Administrative tools for all users.                                                                                                                                                    |
| COMMON APPDATA              | COMMON%20APPDATA                | Application data for all users. A typical path is C:\\Documents and Settings\\All Users\\Application Data.                                                                             |
| COMMON DESKTOP              | COMMON DESKTOP                  | Microsoft Windows Desktop data for all users. Virtual folder that is the root of the namespace.                                                                                        |
| COMMON DOCUMENTS            | COMMON%20DOCUMENTS              | Documents for all users. A typical path is C:\\Documents and Settings\\All Users\\My Documents.                                                                                        |
| COMMON PROGRAMS             | COMMON%20PROGRAMS               | Program groups common to all users. A typical path is C:\\Documents and Settings\\All Users\\Start Menu\\Programs.                                                                     |
| COMMON START MENU           | COMMON%20START%20MENU           | Start menu items common to all users. A typical path is C:\\Documents and Settings\\All Users\\Start Menu.                                                                             |
| COMMON STARTUP              | COMMON%20STARTUP                | Startup program group common to all users.                                                                                                                                             |
| COMMON TEMPLATES            | COMMON%20TEMPLATES              | Document templates common to all users.                                                                                                                                                |
| COMMONMUSIC                 | MY%20MUSIC                      | My Music folder templates common to all users.                                                                                                                                         |
| COMMONPICTURES              | MY%20PICTURES                   | My Pictures folder templates common to all users.                                                                                                                                      |
| COMMONVIDEO                 | MY%20VIDEO                      | My Video folder templates common to all users.                                                                                                                                         |
| CONNECTIONSFOLDER           | CONNECTIONSFOLDER               | folder containing connection data.                                                                                                                                                     |
| CONTROL PANEL FOLDER        | CONTROLPANELFOLDER              | Virtual folder containing icons for the Control Panel applications.                                                                                                                    |
| COOKIES                     | COOKIES                         | File system directory that serves as a common repository for Internet cookies. A typical path is C:\\Documents and Settings\\username\\Cookies.                                        |
| DESKTOP                     | DESKTOP                         | Microsoft Windows Desktop. Virtual folder that is the root of the namespace.                                                                                                           |
| FAVORITES                   | FAVORITES                       | File system directory that serves as a common repository for the user's favorite items. A typical path is C:\\Documents and Settings\\username\\Favorites.                             |
| FONTS                       | FONTS                           | Virtual folder containing installed fonts. A typical path is C:\\WINDOWS\\Fonts.                                                                                                       |
| HISTORY                     | HISTORY                         | File system directory that serves as a common repository for Internet history items.                                                                                                   |
| INTERNETFOLDER              | INTERNETFOLDER                  | Folder that contains Internet data.                                                                                                                                                    |
| LOCAL APPDATA               | LOCAL%20APPDATA                 | File system directory that serves as a data repository for local (non-roaming) applications. A typical path is C:\\Documents and Settings\\username\\Local Settings\\Application Data. |
| LOCALIZEDRESOURCEDIR        | LOCALIZEDRESOURCEDIR            | Localized resource directory.                                                                                                                                                          |
| MYCOMPUTERFOLDER            | MYCOMPUTERFOLDER                | My Computer. Virtual folder containing everything on the local computer: storage devices, printers, and Control Panel. This folder may also contain mapped network drives.             |
| MY MUSIC                    | MY%20MUSIC                      | My Music folder. A typical path is C:\\Documents and Settings\\username\\My Documents\\My Music.                                                                                       |
| MY PICTURES                 | MY%20PICTURES                   | My Pictures folder. A typical path is C:\\Documents and Settings\\username\\My Documents\\My Pictures.                                                                                 |
| MY VIDEO                    | MY%20VIDEO                      | My Video folder. A typical path is C:\\Documents and Settings\\username\\My Documents\\My Video.                                                                                       |
| NETHOOD                     | NETHOOD                         | Virtual folder representing the root of the network namespace hierarchy.                                                                                                               |
| NETWORK PLACES FOLDER       | NETWORKDPLACESFOLDER            | A file system folder containing the link objects that may exist in the My Network Places virtual folder. It is not the same as NETHOOD, which represents the network namespace root.   |
| OEM LINKS                   | OEM%20LINKS                     | Folder containing links to OEM sites.                                                                                                                                                  |
| PERSONAL                    | PERSONAL                        | File system directory that serves as a common repository for a user's documents. A typical path is C:\\Documents and Settings\\username\\My Documents.                                 |
| PRINTERS FOLDER             | PRINTERS FOLDER                 | Virtual folder containing installed printers.                                                                                                                                          |
| PRINTHOOD                   | PRINTHOOD                       | File system directory that contains the link objects that may exist in the Printers virtual folder. A typical path is C:\\Documents and Settings\\username\\PrintHood.                 |
| PROGRAMS                    | PROGRAMS                        | File system directory that contains the user's program groups (which are also file system directories). A typical path is C:\\Documents and Settings\\username\\Start Menu\\Programs.  |
| PROFILE                     | PROFILE                         | User's profile folder.                                                                                                                                                                 |
| PROGRAM FILES               | PROGRAM%20FILES                 | Program Files folder. A typical path is C:\\Program Files.                                                                                                                             |
| PROGRAM FILES COMMON        | PROGRAMFILESCOMMON              | Program Files folder common to all users.                                                                                                                                              |
| PROGRAM FILES COMMON x86    | PROGRAMFILESCOMMONX86           | Program Files folder common to all users on x86 machines.                                                                                                                              |
| PROGRAM FILESx86            | PROGRAMFILESx86                 | Program Files folder on x86 machines.                                                                                                                                                  |
| RECENT                      | RECENT                          | File system directory that contains the user's most recently used documents. A typical path is C:\\Documents and Settings\\username\\Recent.                                           |
| RECYCLE BIN FOLDER          | RECYCLEBINFOLDER                | Virtual folder containing the objects in the user's Recycle Bin.                                                                                                                       |
| RESOURCEDIR                 | RESOURCEDIR                     | The Resource directory.                                                                                                                                                                |
| SENDTO                      | SENDTO                          | File system directory that contains Send To menu items. A typical path is C:\\Documents and Settings\\username\\SendTo.                                                                |
| START MENU                  | START%20MENU                    | File system directory containing Start menu items. A typical path is C:\\Documents and Settings\\username\\Start Menu.                                                                 |
| STARTUP                     | STARTUP                         | File system directory that corresponds to the user's Startup program group.                                                                                                            |
| SYSTEMx86                   | SYSTEMx86                       | System folder on x86 machines.                                                                                                                                                         |
| TEMPLATES                   | TEMPLATES                       | File system directory that serves as a common repository for document templates.                                                                                                       |
| SYSTEM                      | SYSTEM                          | System folder. A typical path is C:\\Windows\\System.                                                                                                                                  |
| WINDOWS                     | WINDOWS                         | Windows directory or SYSROOT.                                                                                                                                                          |



 

### Argument Information



|                          |                                         |
|--------------------------|-----------------------------------------|
| Minimum Operating System | Windows Vista with Service Pack 1 (SP1) |



 

 

 



