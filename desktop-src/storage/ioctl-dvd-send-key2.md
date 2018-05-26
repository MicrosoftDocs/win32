---
title: IOCTL\_DVD\_SEND\_KEY2 control code
description: Sends the specified key to a DVD device -to complete the related step in an authentication sequence. The IOCTL\_DVD\_SEND\_KEY2 request has write access to the device and can send a broader range of key types than IOCTL\_DVD\_SEND\_KEY.
ms.assetid: 58b9c2a5-cd29-4c62-b5ae-39911821e3b7
keywords:
- IOCTL_DVD_SEND_KEY2 control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_DVD_SEND_KEY2
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

# IOCTL\_DVD\_SEND\_KEY2 control code

Sends the specified key to a DVD device -to complete the related step in an authentication sequence. The IOCTL\_DVD\_SEND\_KEY2 request has write access to the device and can send a broader range of key types than [**IOCTL\_DVD\_SEND\_KEY**](ioctl-dvd-send-key.md).

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_DVD_SEND_KEY2%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






