---
Description: The RSM API is the interface that applications use to access the services and media in an RSM system.
ms.assetid: ed36df18-8db8-4e0a-af4f-3f37dbfdf384
title: RSM API
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RSM API

\[[Removable Storage Manager](removable-storage-manager.md) is no longer available as of Windows 7 and Windows Server 2008 R2.\]

The RSM API is the interface that applications use to access the services and media in an RSM system. It is a dynamic-link library (DLL) that contains a group of functions you can use to build your data management application. These functions perform the following operations:

-   Mount and dismount media
-   Clean drives
-   Insert and eject media
-   Inventory libraries
-   Enable and disable libraries, drives, and media
-   Access information in the RSM database

When you develop your media management application using the RSM API, you gain the following benefits:

-   Multiple applications can share the same library, drive, and media resources
-   Code written to the RSM API for a specific library can execute on a wide range of libraries, both those that exist now and those that are introduced in the future
-   A single computer can track multiple types of media
-   A single computer can track media that are inside or outside a media library unit

 

 



