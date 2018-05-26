---
title: IOCTL\_STORAGE\_SET\_READ\_AHEAD control code
description: Causes the device to skip to the given target address when the device reaches a certain trigger address during read-ahead caching.
ms.assetid: a7ed65f3-40a9-4b08-b59d-7c65c250d5cb
keywords:
- IOCTL_STORAGE_SET_READ_AHEAD control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_STORAGE_SET_READ_AHEAD
api_location:
- Ntddcdvd.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOCTL\_STORAGE\_SET\_READ\_AHEAD control code

Causes the device to skip to the given target address when the device reaches a certain trigger address during read-ahead caching.

## Input Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains a [**STORAGE\_SET\_READ\_AHEAD**](storage-set-read-ahead.md) structure that indicates the trigger and target addresses.

## Input Buffer Length

The length of a [**STORAGE\_SET\_READ\_AHEAD**](storage-set-read-ahead.md) structure.

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

The **Information** field is set to zero. The **Status** field is set to STATUS\_SUCCESS.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdvd.h (include Ntddcdvd.h)</dt> </dl> |



## See also

<dl> <dt>

[**STORAGE\_SET\_READ\_AHEAD**](storage-set-read-ahead.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_STORAGE_SET_READ_AHEAD%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






