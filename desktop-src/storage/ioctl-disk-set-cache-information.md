---
title: IOCTL\_DISK\_SET\_CACHE\_INFORMATION control code
description: Sets disk cache configuration data.
ms.assetid: ae1ca621-4862-4345-bb51-4a1c31e00542
keywords:
- IOCTL_DISK_SET_CACHE_INFORMATION control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_DISK_SET_CACHE_INFORMATION
api_location:
- Ntdddisk.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOCTL\_DISK\_SET\_CACHE\_INFORMATION control code

Sets disk cache configuration data.

## Input Buffer

The input buffer.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** in the I/O stack location of the IRP indicates the size, in bytes, of the buffer made available to the driver, which must be &gt;= **sizeof**(DISK\_CACHE\_INFORMATION). Otherwise, the driver returns with an error status of STATUS\_INFO\_LENGTH\_MISMATCH.

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

The **Information** field is set to zero. The **Status** field can be set to STATUS\_SUCCESS or STATUS\_INFO\_LENGTH\_MISMATCH if the input buffer is not large enough.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**DISK\_CACHE\_INFORMATION**](disk-cache-information.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_DISK_SET_CACHE_INFORMATION%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






