---
title: IOCTL\_STORAGE\_PROTOCOL\_COMMAND control code
description: A driver can use IOCTL\_STORAGE\_PROTOCOL\_COMMAND to pass vendor-specific commands to a storage device.
ms.assetid: 1AA59350-2475-4BF7-B447-42FDDB311882
keywords:
- IOCTL_STORAGE_PROTOCOL_COMMAND control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_STORAGE_PROTOCOL_COMMAND
api_location:
- ntddstor.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOCTL\_STORAGE\_PROTOCOL\_COMMAND control code

A driver can use **IOCTL\_STORAGE\_PROTOCOL\_COMMAND** to pass vendor-specific commands to a storage device.

## Input Buffer

None.

## Input Buffer Length

None.

## Output Buffer

The driver returns the results of the vendor-specific command to the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**. Cast the structure returned to a [**STORAGE\_PROTOCOL\_COMMAND**](storage-protocol-command.md) and check its **ReturnStatus** field to determine the status of the command request.

## Output Buffer Length

**Parameters.DeviceIoControl.OutputBufferLength** in the I/O stack location indicates the size, in bytes, of the parameter buffer, which must be &gt;= **sizeof**([**STORAGE\_PROTOCOL\_COMMAND**](storage-protocol-command.md)).

## Status block

The **Information** field is set to the number of bytes returned. The **Status** field is set to **STATUS\_SUCCESS**, or possibly to **STATUS\_INSUFFICIENT\_RESOURCES**.

## Requirements



|                                     |                                                                                                            |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10<br/>                                                                                      |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                             |
| Header<br/>                   | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**STORAGE\_PROTOCOL\_COMMAND**](storage-protocol-command.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_STORAGE_PROTOCOL_COMMAND%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






