---
title: IOCTL\_DVD\_READ\_STRUCTURE control code
description: Returns information about a DVD disc, such as a layer descriptor, copyright information, or manufacturer-specific information.
ms.assetid: 64cf4d53-5d03-43bc-b295-37ecf67b4d2a
keywords:
- IOCTL_DVD_READ_STRUCTURE control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_DVD_READ_STRUCTURE
api_location:
- Ntddcdvd.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOCTL\_DVD\_READ\_STRUCTURE control code

Returns information about a DVD disc, such as a layer descriptor, copyright information, or manufacturer-specific information.

## Input Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains a [**DVD\_READ\_STRUCTURE**](dvd-read-structure.md) structure that indicates the session ID and type of information to return.

## Input Buffer Length

Length of a [**DVD\_READ\_STRUCTURE**](dvd-read-structure.md).

## Output Buffer

The driver returns the disc information in the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Output Buffer Length

**Parameters.DeviceIoControl.OutputBufferLength** in the I/O stack location indicates the size, in bytes, of the buffer, which must be &gt;= **sizeof(***Descriptor***)** where *Descriptor* is [**DVD\_LAYER\_DESCRIPTOR**](dvd-layer-descriptor.md), [**DVD\_COPYRIGHT\_DESCRIPTOR**](dvd-copyright-descriptor.md), [**DVD\_DISK\_KEY\_DESCRIPTOR**](dvd-disk-key-descriptor.md), [**DVD\_BCA\_DESCRIPTOR**](dvd-bca-descriptor.md), or [**DVD\_MANUFACTURER\_DESCRIPTOR**](dvd-manufacturer-descriptor.md).

## Status block

The **Information** field is set to the number of bytes transferred. The **Status** field is set to STATUS\_SUCCESS, or possibly to STATUS\_INSUFFICIENT\_RESOURCES.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdvd.h (include Ntddcdvd.h)</dt> </dl> |



## See also

<dl> <dt>

[**DVD\_READ\_STRUCTURE**](dvd-read-structure.md)
</dt> <dt>

[**DVD\_LAYER\_DESCRIPTOR**](dvd-layer-descriptor.md)
</dt> <dt>

[**DVD\_COPYRIGHT\_DESCRIPTOR**](dvd-copyright-descriptor.md)
</dt> <dt>

[**DVD\_DISK\_KEY\_DESCRIPTOR**](dvd-disk-key-descriptor.md)
</dt> <dt>

[**DVD\_BCA\_DESCRIPTOR**](dvd-bca-descriptor.md)
</dt> <dt>

[**DVD\_MANUFACTURER\_DESCRIPTOR**](dvd-manufacturer-descriptor.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_DVD_READ_STRUCTURE%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






