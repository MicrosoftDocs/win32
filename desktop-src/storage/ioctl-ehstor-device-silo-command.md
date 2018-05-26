---
title: IOCTL\_EHSTOR\_DEVICE\_SILO\_COMMAND control code
description: This IOCTL issues a silo command to the targeted silo on the device. Both input and output data are structured according to the definition of silo commands, as found in the IEEE 1667 specification document.
ms.assetid: 3258FA16-E1FE-4CBF-8C87-0C7A8B2A7EBF
keywords:
- IOCTL_EHSTOR_DEVICE_SILO_COMMAND control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_EHSTOR_DEVICE_SILO_COMMAND
api_location:
- EhStorIoctl.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOCTL\_EHSTOR\_DEVICE\_SILO\_COMMAND control code

This IOCTL issues a silo command to the targeted silo on the device. Both input and output data are structured according to the definition of silo commands, as found in the IEEE 1667 specification document.

## Input Buffer

The input buffer at Irp-&gt;AssociatedIrp.SystemBuffer must contain a structure of type [**SILO\_COMMAND**](silo-command.md).

## Input Buffer Length

The length of a [**SILO\_COMMAND**](silo-command.md) structure.

## Output Buffer

The output buffer contains the output data returned directly from the device response to this silo command. The structure of this output data is assumed to be shared knowledge between the client issuing this IOCTL and the device.

## Output Buffer Length

The length of the buffer.

## Status block

One of the following values may be returned in the Status field:

<dl> STATUS\_SUCCESS - The silo command was successfully issued to the device.  
</dl>

<dl> STATUS\_INVALID\_BUFFER\_SIZE - The input buffer length supplied is of incorrect size.  
</dl>

<dl> STATUS\_BUFFER\_TOO\_SMALL - The output buffer length supplied is of insufficient size to hold the device response for this silo command.  
</dl>

## Requirements



|                   |                                                                                                                  |
|-------------------|------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>EhStorIoctl.h (include EhStorIoctl.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_EHSTOR_DEVICE_SILO_COMMAND%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





