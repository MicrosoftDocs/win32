---
description: Hot Sparing
ms.assetid: 2faf2f3f-f459-4e41-9c8e-042c7b72281b
title: Hot Sparing
ms.topic: article
ms.date: 05/31/2018
---

# Hot Sparing

\[Beginning with Windows 8 and Windows Server 2012, the [Virtual Disk Service](virtual-disk-service-portal.md) COM interface is superseded by the [Windows Storage Management API](/windows-hardware/drivers/storage/windows-storage-management-api-portal).\]

Hot sparing is the substitution of one disk or drive for a failing or failed disk or drive. (Hardware providers act on drives; software providers act on disks.) You can share a hot spare drive among all the LUNs in the subsystem or associate it with a specific LUN. Likewise, you can associate a hot spare disk with a single volume, pack, and software provider, or share it among all hosts on a SAN.

If the associated volume or LUN is fault tolerant, you can substitute a hot spare for a failed disk or drive and rebuild any affected parity RAID or mirrors. You can substitute a hot spare for a failing disk even if the associated volume or LUN is not fault tolerant. Assuming that you can determine the impending failure prior to catastrophic data loss, you can temporarily mirror the hot spare to the failing disk or drive and then remove the failing disk or drive.

Hot sparing can be automatic or manual. If a provider implements automatic hot sparing, it performs the substitution dynamically. Manual hot sparing requires operator or application intervention. A hot spare can contain partial data or formatting from a previous use. VDS overwrites the hot spare when the substitution occurs.

You cannot use a hot spare for ordinary binding operations. If the hot spare is larger than the failed disk or drive, any excess space remains unused until it is explicitly declared available for binding. Once the hot spare has been used for recovery, the disk or drive is no longer a hot spare. In other words, one 16-gigabyte spindle cannot act as two 8-gigabyte hot spares.

 

 
