---
description: The Install section of an INF File defines the steps of the installation procedure.
ms.assetid: 24d40dc6-ac09-4cf8-9229-f81da2925576
title: INF Install Section Example
ms.topic: article
ms.date: 05/31/2018
---

# INF Install Section Example

The **Install** section of an INF File defines the steps of the installation procedure. Each line of an **Install** section has two parts. On the left of the equals sign (=) is the key. On the right hand side, is a list of one or more section titles. The key specifies the type of the sections that are listed on the right. For a description of this section's format see the "INF File Sections and Directives" of the Microsoft Windows 2000 Driver Development Kit.

The following is an example of an **Install** section.

``` syntax
[MyInstallSection]
Copyfiles=DataFiles, ProgramFiles
Delfiles=OldFiles
UpdateInis=NewIniInfo
AddReg=NewRegistryInfo, MoreNewRegistryInfo
DelReg=OldRegistryInfo, MoreOldRegistryInfo
```

In this example the **CopyFiles** key is set to the values "DataFiles" and "ProgramFiles". This specifies two **Copy Files** sections in the INF file that contain the names of the source files used by copying operations. The destination for the copied files would be specified in a **DestinationDirs** section in the INF file.

The **Delfiles** key is given the value "OldFiles". This specifies a **Delete Files** section that contains information relevant to file deletion operations.

The **UpdateInis** key specifies **Update INI File** sections that contain information about updating entries in the INI file.

The **AddReg** and **DelReg** keys specify **Add Registry** and **Delete Registry** sections that contain information about adding or deleting registry information.

 

 



