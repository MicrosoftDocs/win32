---
title: IOCTL\_VOLUME\_ONLINE control code
description: The IOCTL\_VOLUME\_ONLINE IOCTL puts the volume in an ONLINE state, which is a state where read and write operations will be executed.
ms.assetid: 3391bda9-2eec-4c03-84ed-76b89e2c0cf0
keywords:
- IOCTL_VOLUME_ONLINE control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_VOLUME_ONLINE
api_location:
- Ntddvol.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOCTL\_VOLUME\_ONLINE control code

The **IOCTL\_VOLUME\_ONLINE** IOCTL puts the volume in an ONLINE state, which is a state where read and write operations will be executed. The requests are passed down to the physical disk until a subsequent [**IOCTL\_VOLUME\_OFFLINE**](ioctl-volume-offline.md) is received.

A common use for **IOCTL\_VOLUME\_ONLINE** is a case in which the mount manager automatically puts a new volume in the ONLINE state when the volume arrives, unless that volume is listed in a registry key that is populated by the cluster service. **IOCTL\_VOLUME\_ONLINE** is called for removable drives regardless of the NoAutoMount setting in the following registry key:

HKCU\\System\\CurrentControlSet\\Services\\Mountmgr\\NoAutoMount

But for volumes controlled by NoAutoMount, assigning a drive letter will cause **IOCTL\_VOLUME\_ONLINE** to be called.

For volumes that are controlled by the cluster service, **IOCTL\_VOLUME\_ONLINE** is sent by the cluster service when the local node owns the volume. The cluster service uses both **IOCTL\_VOLUME\_ONLINE** and **IOCTL\_VOLUME\_ONLINE** to allow I/O to a disk volume when the disk volume is owned by the local server. Until the cluster service puts the disk volume in an ONLINE state, no I/O is permitted to the disk volume. This prevents disk volume corruption that could result from multiple cluster nodes writing to the same disk volume simultaneously.

## Input Buffer

None.

## Input Buffer Length

None.

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

The **Status** member is set to STATUS\_SUCCESS.

## Requirements



|                    |                                                                                                          |
|--------------------|----------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows XP.<br/>                                                           |
| Header<br/>  | <dl> <dt>Ntddvol.h (include Ntddvol.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_VOLUME\_OFFLINE**](ioctl-volume-offline.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_VOLUME_ONLINE%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






