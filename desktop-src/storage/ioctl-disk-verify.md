---
title: IOCTL\_DISK\_VERIFY control code
description: Performs verification for a specified extent on a disk.
ms.assetid: 923a7fac-c1d5-4634-b209-087e3d5d217a
keywords:
- IOCTL_DISK_VERIFY control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_DISK_VERIFY
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

# IOCTL\_DISK\_VERIFY control code

Performs verification for a specified extent on a disk.

## Input Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains the [**VERIFY\_INFORMATION**](verify-information.md) data specifying the starting offset and length to be verified.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** indicates the size, in bytes, of the buffer, which must be &gt;= **sizeof**(VERIFY\_INFORMATION).

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

The **Information** field is set to zero to prevent the I/O manager from copying data from **SystemBuffer** back into the user area.

If the request is successful, then the **Status** field is set to STATUS\_SUCCESS. Otherwise, the **Status** field can be set to STATUS\_BUFFER\_TOO\_SMALL, STATUS\_INFO\_LENGTH\_MISMATCH, STATUS\_INVALID\_PARAMETER, STATUS\_INSUFFICIENT\_RESOURCES, STATUS\_NONEXISTENT\_SECTOR, STATUS\_DEVICE\_DATA\_ERROR, STATUS\_INVALID\_DEVICE\_REQUEST, STATUS\_IO\_TIMEOUT, or STATUS\_DEVICE\_NOT\_CONNECTED.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**VERIFY\_INFORMATION**](verify-information.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_DISK_VERIFY%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






