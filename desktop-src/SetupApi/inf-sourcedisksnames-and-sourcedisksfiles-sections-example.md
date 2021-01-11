---
description: The SourceDisksNames section of an INF file identifies the disks that contain the source files being installed.
ms.assetid: af4bc466-f0a3-4f83-adb7-6bfc276f7764
title: INF SourceDisksNames and SourceDisksFiles Sections Example
ms.topic: article
ms.date: 05/31/2018
---

# INF SourceDisksNames and SourceDisksFiles Sections Example

The **SourceDisksNames** section of an INF file identifies the disks that contain the source files being installed. The **SourceDisksFiles** section identifies the source files and the source disks that contain them. Note that MIPS, Alpha, and PPC platforms are not supported by Windows 2000 or Windows XP.

Beginning with Windows XP, a **SourceDisksNames** section may specify a tag as well as cabinet file. For example, the following **SourceDisksNames** section may be used with removable or fixed media. If using removable media, the example section verifies the presence of the media by first checking for the presence of the tag. If using fixed media, the example section verifies the presence of the media by first checking for the presence of the cabinet. After verifying the presence of a cabinet, the system attempts to copy files out of the cabinet and prompts for any files it was unable to copy.

``` syntax
[SourceDisksNames]
1="Dajava" , "Dajava.cab",,, 0x10,"Dajava.tag"
```

For more information about **SourceDisksNames** or **SourceDisksFiles**, see the "General Guidelines for INF File" and "INF File Sections and Directives" sections of the Microsoft Windows 2000 Driver Development Kit.

 

 



