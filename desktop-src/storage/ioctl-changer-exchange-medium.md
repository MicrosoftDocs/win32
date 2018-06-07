---
title: IOCTL\_CHANGER\_EXCHANGE\_MEDIUM control code
description: Moves a piece of media from a source element to one destination and the piece of media originally in the first destination to a second destination. The source and second destination are often the same, which essentially swaps the two pieces of media.
ms.assetid: 76f17ee0-5b81-4325-a295-4a6982b49b73
keywords:
- IOCTL_CHANGER_EXCHANGE_MEDIUM control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_CHANGER_EXCHANGE_MEDIUM
api_location:
- Ntddchgr.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOCTL\_CHANGER\_EXCHANGE\_MEDIUM control code

Moves a piece of media from a source element to one destination and the piece of media originally in the first destination to a second destination. The source and second destination are often the same, which essentially swaps the two pieces of media.

## Input Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains the [**CHANGER\_EXCHANGE\_MEDIUM**](changer-exchange-medium.md) data, which indicates the source, both destinations, and whether either or both media should be flipped, assuming the device supports two-sided media.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** in the I/O stack location indicates the size, in bytes, of the parameter buffer, which must be &gt;= **sizeof**(CHANGER\_EXCHANGE\_MEDIUM).

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

The **Information** field is set to zero. The **Status** field is set to STATUS\_SUCCESS, or possibly to STATUS\_DESTINATION\_ELEMENT\_FULL, STATUS\_INFO\_LENGTH\_MISMATCH, STATUS\_INSUFFICIENT\_RESOURCES, STATUS\_INVALID\_DEVICE\_REQUEST, STATUS\_INVALID\_ELEMENT\_ADDRESS, STATUS\_INVALID\_PARAMETER, or STATUS\_SOURCE\_ELEMENT\_EMPTY.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddchgr.h (include Ntddchgr.h)</dt> </dl> |



## See also

<dl> <dt>

[**CHANGER\_EXCHANGE\_MEDIUM**](changer-exchange-medium.md)
</dt> <dt>

[**ChangerExchangeMedium**](changerexchangemedium.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_CHANGER_EXCHANGE_MEDIUM%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






