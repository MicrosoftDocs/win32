---
title: Compound Files
description: Although you can implement your own structured storage objects and interfaces, COM provides a standard implementation called Compound Files.
ms.assetid: '23b425e6-dfe5-403b-8f43-de6843a03dcd'
ms.topic: article
ms.date: 05/31/2018
---

# Compound Files

Although you can implement your own structured storage objects and interfaces, COM provides a standard implementation called Compound Files. Using Compound Files saves you the work of coding your own implementation of structured storage and confers several additional benefits derived from adhering to a defined standard. These benefits include the following:

-   **File-system and platform independence**. Because COM's Compound Files implementation runs on top of existing flat-file systems, compound files stored in the FAT file system, NTFS file system, or Macintosh file systems can be opened by applications using any one of the other file systems.
-   **Searchable**. Because the separate objects in a compound file are saved in a standard format and can be accessed using standard COM interfaces and APIs, any browser utility using these interfaces and APIs can list the objects in the file, even though data within a given object may be in a proprietary format.
-   **Access to certain internal data**. Because the Compound Files implementation provides standard ways of writing certain types of data—summary information, for example—applications can read this data using COM interfaces and APIs.

 

 




