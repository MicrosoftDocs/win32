---
title: IOCTL\_DISK\_DELETE\_DRIVE\_LAYOUT control code
description: Removes partition information from the disk.
ms.assetid: 787fa1ce-5305-4159-8710-3c6971133c4c
keywords:
- IOCTL_DISK_DELETE_DRIVE_LAYOUT control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_DISK_DELETE_DRIVE_LAYOUT
api_location:
- Ntdddisk.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOCTL\_DISK\_DELETE\_DRIVE\_LAYOUT control code

Removes partition information from the disk. If the partition style of the disk is Master Boot Record (MBR), sector 0 of the disk is wiped clean except for the bootstrap code. All signatures, such as the AA55 boot signature and the NTFT disk signature, will be removed. If the partition style of the disk is GUID Partition Table (GPT), the primary partition table header in sector 1 and the backup partition table in the last sector of the disk are wiped clean. This operation can be used to generate so-called "superfloppies" that contain a file system starting at the first sector of the disk rather than in a partition on the disk.

## Input Buffer

None.

## Input Buffer Length

None.

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

The **Status** field is set to STATUS\_SUCCESS, or possibly to STATUS\_INSUFFICIENT\_RESOURCES.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_DISK_DELETE_DRIVE_LAYOUT%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





