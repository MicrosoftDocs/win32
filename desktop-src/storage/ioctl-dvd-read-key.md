---
title: IOCTL\_DVD\_READ\_KEY control code
description: Returns a copy-protection key of the specified type challenge key, bus key, title key, read RPC key, set RPC key, or disk key.
ms.assetid: 42745dae-f472-4f64-8f16-9f4dec1e986a
keywords:
- IOCTL_DVD_READ_KEY control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_DVD_READ_KEY
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

# IOCTL\_DVD\_READ\_KEY control code

Returns a copy-protection key of the specified type: challenge key, bus key, title key, read RPC key, set RPC key, or disk key. A challenge key or bus key is sent back to the device to complete the related step in a DVD authentication sequence. After the authentication sequence is completed, a title key is used to encrypt and decrypt user data transferred from a DVD disc and a disk key is used to encrypt and decrypt title key data. If the drive region has not been set previously (if it is still at factory default) and if the inserted media has a region, the device region will be set to the current media region.

## Input Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains a [**DVD\_COPY\_PROTECT\_KEY**](dvd-copy-protect-key.md) structure that indicates the session ID of the DVD session and the type of key to return.

## Input Buffer Length

**Parameters.DeviceIoControl.OutputBufferLength** indicates the size, in bytes, of the buffer, which must be &gt;= the size of one of the following: DVD\_CHALLENGE\_KEY\_LENGTH, DVD\_BUS\_KEY\_LENGTH, DVD\_TITLE\_KEY\_LENGTH, DVD\_RPC\_KEY\_LENGTH, DVD\_SET\_RPC\_KEY\_LENGTH, or DVD\_DISK\_KEY\_LENGTH.

## Output Buffer

The driver returns the DVD\_COPY\_PROTECT\_KEY data in the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Output Buffer Length

Length of a [**DVD\_COPY\_PROTECT\_KEY**](dvd-copy-protect-key.md).

## Status block

The **Information** field is set to the number of bytes transferred. The **Status** field is set to STATUS\_SUCCESS, or possibly to STATUS\_INSUFFICIENT\_RESOURCES.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdvd.h (include Ntddcdvd.h)</dt> </dl> |



## See also

<dl> <dt>

[**DVD\_COPY\_PROTECT\_KEY**](dvd-copy-protect-key.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_DVD_READ_KEY%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






