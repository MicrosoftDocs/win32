---
title: IOCTL\_STORAGE\_GET\_MEDIA\_TYPES control code
description: Returns information about the geometry of floppy drives.
ms.assetid: 213711fb-26eb-443b-aff4-8f84b643adb3
keywords:
- IOCTL_STORAGE_GET_MEDIA_TYPES control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_STORAGE_GET_MEDIA_TYPES
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOCTL\_STORAGE\_GET\_MEDIA\_TYPES control code

Returns information about the geometry of floppy drives.

## Input Buffer

None.

## Input Buffer Length

None.

## Output Buffer

The driver returns an array of [**DISK\_GEOMETRY**](disk-geometry.md) records for the types of media it supports in the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Output Buffer Length

**Parameters.DeviceIoControl.OutputBufferLength** in the I/O stack location of the IRP indicates the size, in bytes, of the buffer, which must be at least (*NumberOfSupportedMediaTypes* \* **sizeof**(DISK\_GEOMETRY)).

## Status block

The **Information** field is set to the size, in bytes, of the returned data. The **Status** field can be set to STATUS\_SUCCESS, or possibly to STATUS\_INVALID\_DEVICE\_REQUEST, STATUS\_BUFFER\_TOO\_SMALL, or STATUS\_BUFFER\_OVERFLOW.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**DISK\_GEOMETRY**](disk-geometry.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_STORAGE_GET_MEDIA_TYPES%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






