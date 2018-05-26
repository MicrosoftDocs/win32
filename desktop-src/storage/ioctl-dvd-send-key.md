---
title: IOCTL\_DVD\_SEND\_KEY control code
description: Sends the specified key to a DVD device to complete the related step in an authentication sequence.This IOCTL has only read access to the device and cannot send keys that make alterations to the hardware configuration.
ms.assetid: 8db0e6fe-1dfc-4f26-8fd7-7d170c33da0a
keywords:
- IOCTL_DVD_SEND_KEY control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_DVD_SEND_KEY
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

# IOCTL\_DVD\_SEND\_KEY control code

Sends the specified key to a DVD device to complete the related step in an authentication sequence.

This IOCTL has only read access to the device and cannot send keys that make alterations to the hardware configuration. Therefore, this request is limited to sending key types **DvdChallengeKey**, **DvdBusKey2**, and **DvdInvalidateAGID**.

The [**IOCTL\_DVD\_SEND\_KEY2**](ioctl-dvd-send-key2.md) request has write access to the device and is not limited to these three key types.

For more information, see [**DVD\_KEY\_TYPE**](dvd-key-type.md).

## Input Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains a [**DVD\_COPY\_PROTECT\_KEY**](dvd-copy-protect-key.md) structure that indicates the session ID, key type, and key to be sent to the device.

## Input Buffer Length

Length of a [**DVD\_COPY\_PROTECT\_KEY**](dvd-copy-protect-key.md).

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

The **Information** field is set to zero. The **Status** field is set to STATUS\_SUCCESS, or possibly to STATUS\_INSUFFICIENT\_RESOURCES.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdvd.h (include Ntddcdvd.h)</dt> </dl> |



## See also

<dl> <dt>

[**DVD\_COPY\_PROTECT\_KEY**](dvd-copy-protect-key.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_DVD_SEND_KEY%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






