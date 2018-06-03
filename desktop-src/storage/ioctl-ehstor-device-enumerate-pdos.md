---
title: IOCTL\_EHSTOR\_DEVICE\_ENUMERATE\_PDOS control code
description: This IOCTL returns a result set containing the enumeration of all active storage Physical Device Objects (PDOs) associated with the given Addressable Command Target (ACT).
ms.assetid: 900A8CAB-287D-4D92-B4CB-2959E87C8E67
keywords:
- IOCTL_EHSTOR_DEVICE_ENUMERATE_PDOS control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_EHSTOR_DEVICE_ENUMERATE_PDOS
api_location:
- EhStorIoctl.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOCTL\_EHSTOR\_DEVICE\_ENUMERATE\_PDOS control code

This IOCTL returns a result set containing the enumeration of all active storage Physical Device Objects (PDOs) associated with the given Addressable Command Target (ACT). The client may first probe for the required buffer size by issuing this IOCTL in the following manner:


```
DeviceIoControl(
    hDevice,
    IOCTL_EHSTOR_DEVICE_ENUMERATE_PDOS,
    &amp;pdoType,
    sizeof(PDO_TYPE),
    NULL,
    0,
    &amp;dwBytesRequired,
    NULL );
```



With the output buffer parameter set to **NULL**, the I/O manager clears the IRP\_INPUT\_OPERATION bit in the IRP flags. Upon detecting this, the storage silo driver can safely set IoStatus.Information to the required buffer size, thus indicating it to the client.

This only works because STATUS\_BUFFER\_OVERFLOW (0x80000005) is an NT\_WARNING() value for which I/O manager copies IoStatus.Information into the lpBytesReturned parameter, returning that value to the client.

Caution is required here because IOCTL\_EHSTOR\_DEVICE\_ENUMERATE\_PDOS is defined with METHOD\_BUFFERED, therefore I/O manager will attempt to copy this number of bytes into the output buffer.

## Input Buffer

The input buffer at Irp-&gt;AssociatedIrp.SystemBuffer must contain a ULONG value as defined in [**PDO\_TYPE**](pdo-type.md),

where either all of the PDOs, just the disk PDO, just the control PDO or all silo PDOs are enumerated respectively according to the provided PDO\_TYPE input value.

## Input Buffer Length

The length of a ULONG.

## Output Buffer

Irp-&gt;AssociatedIrp.SystemBuffer points to the buffer that will receive the PDO enumeration results. If the client supplied a non-**NULL** buffer with the issued IOCTL, then the driver fills it with the result set only if the Parameters.DeviceIoControl.The return value is STATUS\_SUCCESS if the buffer size is sufficient and the results have been copied to the buffer. Otherwise STATUS\_INVALID\_BUFFER\_SIZE is returned and the output buffer is unmodified.

The returned enumeration buffer contains a result set structured according to the following rules. The leading structure in the buffer, [**ENUM\_PDO\_RESULTS**](enum-pdo-results.md), consists of a structure count and an array of [**ENUM\_PDO\_ENTRY**](enum-pdo-entry.md) structures.

## Output Buffer Length

OutputBufferLength indicates a buffer size of sufficient length to include the entire result set.

## Status block

One of the following values may be returned in the Status field:

<dl> STATUS\_SUCCESS - The output buffer contains the enumeration of the requested PDOs.  
</dl>

<dl> STATUS\_BUFFER\_OVERFLOW - The Information field is set to the required buffer size to contain the entire enumeration result set output.  
</dl>

<dl> STATUS\_INVALID\_BUFFER\_SIZE - The output buffer length supplied is insufficient to contain the entire enumeration result set output.  
</dl>

## Requirements



|                   |                                                                                                                  |
|-------------------|------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>EhStorIoctl.h (include EhStorIoctl.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_EHSTOR_DEVICE_ENUMERATE_PDOS%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





