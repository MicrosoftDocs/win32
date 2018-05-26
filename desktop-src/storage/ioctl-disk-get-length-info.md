---
title: IOCTL\_DISK\_GET\_LENGTH\_INFO control code
description: Returns the length, in bytes, of the disk, partition, or volume associated with the device object that is the target of the request.
ms.assetid: 62d31b13-bc4a-4b2f-82be-551a61cae218
keywords:
- IOCTL_DISK_GET_LENGTH_INFO control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_DISK_GET_LENGTH_INFO
api_location:
- Ntdddisk.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOCTL\_DISK\_GET\_LENGTH\_INFO control code

Returns the length, in bytes, of the disk, partition, or volume associated with the device object that is the target of the request.

## Input Buffer

None.

## Input Buffer Length

None.

## Output Buffer

The driver returns the [**GET\_LENGTH\_INFORMATION**](get-length-information.md) data in the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Output Buffer Length

**Parameters.DeviceIoControl.OutputBufferLength** in the I/O stack location of the IRP indicates the size, in bytes, of the buffer, which must be &gt;= **sizeof**(GET\_LENGTH\_INFORMATION).

## Status block

The **Information** field is set to the size, in bytes, of the returned data. The **Status** field can be set to STATUS\_SUCCESS, or to STATUS\_BUFFER\_TOO\_SMALL if the buffer supplied by the caller is inadequate.

## Requirements



|                    |                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------|
| Version<br/> | Supported in Windows XP and later operating systems.<br/>                                            |
| Header<br/>  | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**GET\_LENGTH\_INFORMATION**](get-length-information.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_DISK_GET_LENGTH_INFO%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






