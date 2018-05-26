---
title: IOCTL\_DISK\_FORMAT\_TRACKS control code
description: Formats the specified set of contiguous tracks on the disk.
ms.assetid: f27f962f-badc-4e6f-ad3b-ce2a0c8ce825
keywords:
- IOCTL_DISK_FORMAT_TRACKS control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_DISK_FORMAT_TRACKS
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

# IOCTL\_DISK\_FORMAT\_TRACKS control code

Formats the specified set of contiguous tracks on the disk.

## Input Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains the [**FORMAT\_PARAMETERS**](format-parameters.md) data. **Parameters.DeviceIoControl.InputBufferLength** in the I/O stack location of the IRP indicates the size, in bytes, of the buffer.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** in the I/O stack location of the IRP indicates the size, in bytes, of the buffer.

## Output Buffer

The device driver returns an array of BAD\_TRACK\_NUMBER values to the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Output Buffer Length

Length of the buffer.

## Status block

The **Information** field is set to the size of the returned bad-track array when the **Status** field is set to STATUS\_SUCCESS. Otherwise, the **Information** field is zero and the **Status** field possibly can be set to STATUS\_INVALID\_PARAMETER or STATUS\_MEDIA\_WRITE\_PROTECTED if the media is removable.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**FORMAT\_PARAMETERS**](format-parameters.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_DISK_FORMAT_TRACKS%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






