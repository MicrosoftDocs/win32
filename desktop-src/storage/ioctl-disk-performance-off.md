---
title: IOCTL\_DISK\_PERFORMANCE\_OFF control code
description: Disables the counters that were enabled by previous calls to IOCTL\_DISK\_PERFORMANCE. This request is available in Windows XP and later operating systems. Caller must be running at IRQL PASSIVE\_LEVEL.
ms.assetid: 9a56ac86-2d39-4367-8e64-b6f6bc0da0ea
keywords:
- IOCTL_DISK_PERFORMANCE_OFF control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_DISK_PERFORMANCE_OFF
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

# IOCTL\_DISK\_PERFORMANCE\_OFF control code

Disables the counters that were enabled by previous calls to [**IOCTL\_DISK\_PERFORMANCE**](ioctl-disk-performance.md). This request is available in Windows XP and later operating systems. Caller must be running at IRQL = PASSIVE\_LEVEL.

## Input Buffer

None.

## Input Buffer Length

None.

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

The **Information** member is set to zero. The **Status** member is set to STATUS\_SUCCESS if the operation was successful. Otherwise, the **Status** member is set to the appropriate error code.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |
| IRQL<br/>   | PASSIVE\_LEVEL<br/>                                                                                  |



## See also

<dl> <dt>

[**IOCTL\_DISK\_PERFORMANCE**](ioctl-disk-performance.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_DISK_PERFORMANCE_OFF%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






