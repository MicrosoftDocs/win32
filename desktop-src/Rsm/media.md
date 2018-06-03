---
Description: Units of media store information. Each unit of media, or medium, also referred to as a cartridge, is of a certain type, such as 8mm tape, magnetic disk, optical disk, or CD-ROM.
ms.assetid: a0afe0ca-61ad-4ac8-8e3e-4a7e9ddd6600
title: Media
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Media

\[[Removable Storage Manager](removable-storage-manager.md) is no longer available as of Windows 7 and Windows Server 2008 R2.\]

Units of media store information. Each unit of media, or medium, also referred to as a cartridge, is of a certain type, such as 8mm tape, magnetic disk, optical disk, or CD-ROM.

Most types of media have a single side. For example, a tape must always be oriented in a certain way. When the tape is placed in a drive, all of its data is accessible. Some types of media, such as magneto-optic (MO) disks, have two sides. An MO disk has an "A" side and a "B" side. When an MO disk is placed in a drive with the "A" side up, then the "A" side is accessible and the "B" side is not. To access the "B" side, the disk must be inserted with the "B" side up.

Removable Storage Manager represents media physically and logically. *Physical media* are the tangible media that are inserted and removed from libraries and mounted in drives.

When an application needs to access data on a cartridge, Removable Storage Manager generates a logical media identifier (LMID) that allows the application to request the data on that cartridge. Because access to the data occurs only through that ID, Removable Storage Manager can manage the physical location of the data. For example, if the original cartridge begins to fail, Removable Storage Manager can move the data to a new cartridge without having to notify the application.

Physical media and the sides they contain are tracked in Removable Storage Manager and can take on various states as they are entered into a library and used. For more information about media and side states, see [Media Life Cycle](media-life-cycle.md) and [Media Pools](media-pools.md).

Removable Storage Manager provides the infrastructure necessary to share media among various applications. Removable Storage Manager ensures that all media are used in such a way as to preserve the data they contain. Removable Storage Manager accomplishes this by identifying and verifying the identity of each cartridge. For more information about how Removable Storage Manager verifies the identity of media, see [RSM Media Identification and Naming](rsm-media-identification-and-naming.md).

 

 



