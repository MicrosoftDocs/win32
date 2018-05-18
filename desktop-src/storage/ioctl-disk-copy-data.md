---
title: IOCTL\_DISK\_COPY\_DATA control code
description: This IOCTL\_DISK\_COPY\_DATA IOCTL is used to copy data from one area of the disk to another.
ms.assetid: '1434ee49-4c3d-4104-bca4-c0ea4299c9aa'
keywords: ["IOCTL_DISK_COPY_DATA control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_DISK_COPY_DATA
api_location:
- Ntdddisk.h
api_type:
- HeaderDef
---

# IOCTL\_DISK\_COPY\_DATA control code

This IOCTL\_DISK\_COPY\_DATA IOCTL is used to copy data from one area of the disk to another.

## Input Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains the [**DISK\_COPY\_DATA\_PARAMETERS**](disk-copy-data-parameters.md) data. **Parameters.DeviceIoControl.InputBufferLength** in the I/O stack location of the IRP indicates the size, in bytes, of the buffer.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** in the I/O stack location of the IRP indicates the size, in bytes, of the buffer.

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

The **Status** field is set to STATUS\_SUCCESS if the operation is successful.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**DISK\_COPY\_DATA\_PARAMETERS**](disk-copy-data-parameters.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_DISK_COPY_DATA%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






