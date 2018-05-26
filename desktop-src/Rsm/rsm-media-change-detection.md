---
Description: Many removable media devices, including all those connected to the system by means of SCSI and IDE, cannot themselves report when media are entered or removed.
ms.assetid: 9fe2625b-b082-4f8e-a40e-562f1a2d2683
title: RSM Media Change Detection
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RSM Media Change Detection

\[[Removable Storage Manager](removable-storage-manager.md) is no longer available as of Windows 7 and Windows Server 2008 R2.\]

Many removable media devices, including all those connected to the system by means of SCSI and IDE, cannot themselves report when media are entered or removed. Instead the host system must notice such changes either by querying the device specifically for this information or when performing some other operation on the drive.

Since Removable Storage Manager controls changers and knows when media enter and leave drives, this is not a problem for drives in changers. It is an issue, however, for stand-alone drives. The information that Removable Storage Manager has about the contents of a stand-alone drive might be incorrect if the state of the drive has changed. For example, the snap-in might show that a drive is empty for a period of time after a tape is inserted into a tape drive. An inventory operation on the stand-alone drive library brings the state up-to-date.

Some applications need to have current information. For these applications Removable Storage Manager provides a media change detection mechanism that can be turned on and controlled through Removable Storage Manager API calls. With media detection turned on for a stand-alone drive library, the state of the drive that Removable Storage Manager presents to applications is updated almost immediately after the physical state of the drive changes.

 

 



