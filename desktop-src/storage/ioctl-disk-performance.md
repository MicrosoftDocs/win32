---
title: IOCTL\_DISK\_PERFORMANCE control code
description: Increments a reference counter that enables the collection of disk performance statistics, such as the numbers of bytes read and written since the driver last processed this request, for a corresponding disk monitoring application.
ms.assetid: 'd88d323d-6e74-4a4b-9246-893d92bea89b'
keywords: ["IOCTL_DISK_PERFORMANCE control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_DISK_PERFORMANCE
api_location:
- Ntdddisk.h
api_type:
- HeaderDef
---

# IOCTL\_DISK\_PERFORMANCE control code

Increments a reference counter that enables the collection of disk performance statistics, such as the numbers of bytes read and written since the driver last processed this request, for a corresponding disk monitoring application. In Microsoft Windows 2000 this IOCTL is handled by the filter driver diskperf. In Windows XP and later operating systems, the partition manager handles this request for disks and *ftdisk.sys* and *dmio.sys* handle this request for volumes.

## Input Buffer

None.

## Input Buffer Length

None.

## Output Buffer

The driver returns the [**DISK\_PERFORMANCE**](disk-performance.md) data in the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Output Buffer Length

**Parameters.DeviceIoControl.OutputBufferLength** in the I/O stack location of the IRP indicates the size, in bytes, of the buffer, which must be at least **sizeof**(DISK\_PERFORMANCE).

## Status block

The **Information** field is set to **sizeof**(DISK\_PERFORMANCE) when the **Status** field is set to STATUS\_SUCCESS. Otherwise, the **Status** field can be set to STATUS\_INVALID\_PARAMETER or STATUS\_BUFFER\_TOO\_SMALL.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |
| IRQL<br/>   | PASSIVE\_LEVEL<br/>                                                                                  |



## See also

<dl> <dt>

[**IOCTL\_DISK\_PERFORMANCE\_OFF**](ioctl-disk-performance-off.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_DISK_PERFORMANCE%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






