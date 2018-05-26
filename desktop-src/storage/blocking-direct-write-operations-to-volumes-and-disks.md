---
title: Blocking Direct Write Operations to Volumes and Disks
description: Blocking Direct Write Operations to Volumes and Disks
ms.assetid: 155d6bd5-9082-4f0c-bfb0-c17e45d4faf6
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Blocking Direct Write Operations to Volumes and Disks

Some of the most compelling new features in Windows Vista are its guarantees regarding code and data integrity. To better protect Windows Vista from potentially malicious techniques, changes to the storage driver stack have been introduced to block direct write operations to volume and disk handles. If your application or driver writes directly to a volume that has a file system mounted on it, without first obtaining exclusive access to it, you could cause corruption or system instability, or both. This is because those writes might collide with other changes coming from the file system and leave the contents of the volume or file system, or both in an inconsistent state. To prevent this, we have made the following changes.

Write operations on a DASD volume handle will succeed if the file system is not mounted, or if:

-   The sectors being written to are the boot sectors.

-   The sectors being written to reside outside file system space.

-   The file system has been locked implicitly by requesting exclusive write access.

-   The file system has been locked explicitly by sending down a lock/dismount request.

-   The write request has been flagged by a kernel-mode driver that indicates that this check should be bypassed. The flag is called SL\_FORCE\_DIRECT\_WRITE and it is in the IrpSp-&gt;flags field. This flag is checked by both the file system and storage drivers.

The changes that are mentioned previously will not apply if the file system on the volume is not mounted or the volume has no file system.

Write operations on a disk handle will succeed if:

-   The sectors being written to do not fall within a file system.

-   The sectors being written to fall within a mounted file system that is locked explicitly.

-   The sectors being written to fall within a file system that is not mounted or the volume has no file system.

In addition to the various Win32 File I/O API routines (such as WriteFile), there are device I/O control requests that can be used to issue write operations to a volume or disk. The changes mentioned previously will apply to the device I/O control requests as well. They include the following:

-   IOCTL\_DISK\_COPY\_DATA

-   IOCTL\_SCSI\_PASS\_THROUGH

-   IOCTL\_SCSI\_PASS\_THROUGH\_DIRECT

-   SCSIOP\_WRITE6

-   SCSIOP\_WRITE

-   SCSIOP\_WRITE\_VERIFY

-   SCSIOP\_WRITE\_SAME

-   SCSIOP\_WRITE\_LONG

-   SCSIOP\_XDWRITE

-   SCSIOP\_XPWRITE

-   SCSIOP\_XDWRITE\_READ

-   SCSIOP\_WRITE12SCSIOP\_WRITE\_VERIFY12

-   SCSIOP\_WRITE16

-   SCSIOP\_WRITE\_VERIFY16

-   SCSIOP\_WRITE\_SAME16

-   SCSIOP\_WRITE\_LONG16

-   SCSIOP\_WRITE\_XDWRITE\_EXTENDED16

-   SCSIOP\_WRITE\_COPY

-   SCSIOP\_WRITE\_COPY\_COMPARE

-   IOCTL\_ATA\_PASS\_THROUGH\_DIRECT

-   IOCTL\_ATA\_PASS\_THROUGH

-   IDE\_COMMAND\_WRITE

-   IDE\_COMMAND\_WRITE\_DMA

-   IDE\_COMMAND\_WRITE\_DMA\_QUEUED

-   IDE\_COMMAND\_WRITE\_MULTIPLE

-   IDE\_COMMAND\_WRITE\_EXT

-   IDE\_COMMAND\_WRITE\_DMA\_EXT

-   IDE\_COMMAND\_WRITE\_DMA\_FUA\_EXT

-   IDE\_COMMAND\_WRITE\_DMA\_QUEUED\_EXT

-   IDE\_COMMAND\_WRITE\_DMA\_QUEUED\_FUA\_EXT

-   IDE\_COMMAND\_WRITE\_MULTIPLE\_EXT

-   IDE\_COMMAND\_WRITE\_MULTIPLE\_FUA\_EXT

The application needs to lock the volume, dismount the volume, or both, before it can issue DASD I/O. This is new to Windows Vista and was done to address potentially malicious techniques.

1.  The file system will block all write operations to reserved sections of the disk. In this case, those reserved sections include the MBR and the two FAT areas. To block these areas, you need to lock the volume by sending FSCTL\_LOCK\_VOLUME. You must issue this structure on the same volume handle that performs the actual write operations. This request can fail if there are open file handles. In this case, the application can force a dismount of the file system by issuing FSCTL\_DISMOUNT\_VOLUME. However, the volume is not actually dismounted until the file handle is closed. Until then, the application can continue to issue DASD I/O by using the same file handle that is currently open.

2.  There is an extended region beyond the volume space that is known to the file system where write operations will be blocked. To allow write operations to this region, you must issue FSCTL\_ALLOW\_EXTENDED\_DASD\_IO on the volume handle.

You can use the Win32 API routine DeviceIoControl to issue all the previous FSCTSs.

For more information, see [INFO: Direct Drive Access Under Win32](http://go.microsoft.com/fwlink/p/?linkid=123001) and [Changes to the file system and to the storage stack to restrict direct disk access and direct volume access in Windows Vista and in Windows Server 2008](http://go.microsoft.com/fwlink/p/?linkid=123002).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20Blocking%20Direct%20Write%20Operations%20to%20Volumes%20and%20Disks%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




