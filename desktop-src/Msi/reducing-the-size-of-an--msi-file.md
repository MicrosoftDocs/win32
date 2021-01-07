---
description: Developers of Windows Installer packages may notice their .msi files getting larger than expected after repeated edits and saves.
ms.assetid: d5229ef5-0cb5-4daf-8468-0cb653029c1c
title: Reducing the Size of an .msi File
ms.topic: article
ms.date: 05/31/2018
---

# Reducing the Size of an .msi File

Developers of Windows Installer packages may notice their .msi files getting larger than expected after repeated edits and saves. Windows Installer .msi files are compound files that contain storages and streams, and have some of the same storage limitations as OLE document files. If you edit and save the same .msi file over and over, it creates wasted storage space in the file. This only affects authors of .msi files and has no effect on Windows Installer users. Developers may want to remove this wasted storage space before shipping their final .msi file.

To remove wasted storage space and reduce the final size of .msi files, you have the following options.

-   Export all of the tables in the database to .idt files, and then import those into a new database. This produces the most compact storage possible.
-   Use a software utility for compacting the storage space of OLE document files.

 

 



