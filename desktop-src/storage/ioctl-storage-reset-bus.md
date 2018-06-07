---
title: IOCTL\_STORAGE\_RESET\_BUS control code
description: Resets an I/O bus and, indirectly, each device on the bus.
ms.assetid: 26c9d499-2d53-48b8-8704-3ec7b15e15d8
keywords:
- IOCTL_STORAGE_RESET_BUS control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_STORAGE_RESET_BUS
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOCTL\_STORAGE\_RESET\_BUS control code

Resets an I/O bus and, indirectly, each device on the bus. Resetting the bus clears all device reservations and transfer speed settings, which must then be renegotiated, making it a time-consuming operation that should be used very rarely. The caller requires only read access to issue a bus reset.

The **SrbStatus** flag of pending SRBs is set to SRB\_STATUS\_BUS\_RESET.

## Input Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains a [**STORAGE\_BUS\_RESET\_REQUEST**](storage-bus-reset-request.md) structure that specifies the path ID of the bus to reset.

## Input Buffer Length

The length of a [**STORAGE\_BUS\_RESET\_REQUEST**](storage-bus-reset-request.md) structure.

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

The **Information** field is set to zero. The **Status** field is set to STATUS\_SUCCESS, or possibly to STATUS\_INSUFFICIENT\_RESOURCES, STATUS\_NOT\_IMPLEMENTED, or STATUS\_INVALID\_DEVICE\_REQUEST.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**STORAGE\_BUS\_RESET\_REQUEST**](storage-bus-reset-request.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_STORAGE_RESET_BUS%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






