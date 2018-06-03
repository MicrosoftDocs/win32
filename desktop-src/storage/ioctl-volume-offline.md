---
title: IOCTL\_VOLUME\_OFFLINE control code
description: The IOCTL\_VOLUME\_OFFLINE IOCTL puts the volume in an OFFLINE state, which is a state where read and write operations will fail.
ms.assetid: 09a1faa7-9ce4-44ac-afb0-27ffeabc9d71
keywords:
- IOCTL_VOLUME_OFFLINE control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_VOLUME_OFFLINE
api_location:
- Ntddvol.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOCTL\_VOLUME\_OFFLINE control code

The **IOCTL\_VOLUME\_OFFLINE** IOCTL puts the volume in an OFFLINE state, which is a state where read and write operations will fail. The requests will not be passed down to the physical disk until a subsequent [**IOCTL\_VOLUME\_ONLINE**](ioctl-volume-online.md) is received.

A common use for **IOCTL\_VOLUME\_OFFLINE** is a case in which one application or driver wants to prevent a volume from being remounted by a call to open the volume from a second application or driver while the volume is in the process of being removed by the first application or driver. For example, before masking a Logical Unit Number (LUN), the volumes on the LUN should be locked (optional), dismounted, taken offline, and uninstalled. Now the LUN can be masked without causing Plug and Play (PnP) surprise removal events to be logged for the volumes and the disk itself. Without the call to take the volume offline, after the handle that is used to dismount it is closed, the volume can then be remounted by a call to open it from another application or driver, if it occurred before the call to uninstall the volume. A call to open a volume succeeds on an offline volume, but I/O directed toward an offline volume fails. Taking a volume offline has no effect on disk I/O (if the application or driver opened a handle to the disk), but stops volume I/O (if the application or driver opened a handle to the volume).

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

[**IOCTL\_VOLUME\_ONLINE**](ioctl-volume-online.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_VOLUME_OFFLINE%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






