---
title: IOCTL\_VOLUME\_IS\_CLUSTERED control code
description: Allows a driver or application to determine if a volume is clustered.
ms.assetid: aa8accf8-79c9-4868-b621-d468a121cb60
keywords:
- IOCTL_VOLUME_IS_CLUSTERED control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_VOLUME_IS_CLUSTERED
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

# IOCTL\_VOLUME\_IS\_CLUSTERED control code

Allows a driver or application to determine if a volume is clustered.

## Input Buffer

None.

## Input Buffer Length

None.

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

If the volume is clustered, the IOCTL returns **STATUS\_SUCCESS**. If the volume is not clustered, the IOCTL returns **STATUS\_UNSUCCESSFUL**.

## Remarks

For an invalid disk type, such as dynamic disk, the disk management component will return **STATUS\_INVALID\_DEVICE\_REQUEST**.

## Requirements



|                    |                                                                                                          |
|--------------------|----------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows XP.<br/>                                                           |
| Header<br/>  | <dl> <dt>Ntddvol.h (include Ntddvol.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_VOLUME_IS_CLUSTERED%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





