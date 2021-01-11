---
description: Caching control in Transactional NTFS.
ms.assetid: 0fd272ee-cf5f-4ba9-b8aa-ff0016f51d4b
title: Deploying Transactional NTFS
ms.topic: article
ms.date: 05/31/2018
---

# Deploying Transactional NTFS

Transactional NTFS (TxF), like most transaction mechanisms, depends upon correct ordering of data writes. Ensuring proper write ordering requires explicit control of data caching. To meet this requirement, TxF requires that disk drives implement the caching control mechanisms that are part of standardized drive interfaces such as SCSI, SATA, and ATA.

The caching control mechanism used by TxF is a flag known as the Force Unit Access (FUA) function. This flag specifies that the drive should write the data to stable media storage before signaling complete. At certain critical points within a transaction, TxF needs to issue an FUA to ensure that some control data necessary to successfully rollback a transaction is not lost if a power failure occurs.

Server-class disk drives (SCSI and Fiber Channel) generally support the FUA flag. Starting in Vista, Windows supports the FUA flag only for SCSI and Fiber Channel disks.

On commodity drives (ATA/SATA/USB), TxF has periods of vulnerability during which a drive power failure can result in TxF being unable to correctly rollback the transaction, thus leaving data in an inconsistent state unless the drive's write cache is disabled.

Some Host Bus Adapters (HBAs) and storage controllers (for example, RAID systems) have built-in battery-backed caches. Because these devices preserve cached data if a power fault occurs, any disks connected to them are not required to honor the FUA flag. Further, a disk whose power supply is protected by an uninterruptable power supply (UPS) does not need to honor the FUA flag. This is because the UPS will maintain power long enough for the disk to flush its cache to the media.

Disabling a drive's write cache eliminates the requirement for the drive to honor the FUA flag. You can disable a disk's write caching by issuing the [**IOCTL\_DISK\_SET\_CACHE\_INFORMATION**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_disk_set_cache_information) control code to the disk. The state of the write cache (on/off) will be preserved across system reboots. Issuing this control code will have very significant performance consequences for all I/O issued to that disk, which will most likely be a noticeable performance degradation. Use of this control code should be carefully considered prior to deployment.

> [!Note]  
> For TxF to be capable of consistently protecting your data's integrity through power faults, the system must satisfy at least one of the following criteria:
>
> -   Use server-class disks (SCSI, Fiber Channel).
> -   Make sure the disks are connected to a battery-backed caching HBA.
> -   Use a storage controller (for example, RAID system) as the storage device.
> -   Ensure power to the disk is protected by a UPS.
> -   Ensure that the disk's write caching feature is disabled.

 

 

 



