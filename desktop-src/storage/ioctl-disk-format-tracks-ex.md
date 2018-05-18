---
title: IOCTL\_DISK\_FORMAT\_TRACKS\_EX control code
description: Is similar to IOCTL\_DISK\_FORMAT\_TRACKS, except that it allows the caller to specify several more parameters.
ms.assetid: '6bd7e722-6603-4d3b-9f18-1b7eb531f5fb'
keywords: ["IOCTL_DISK_FORMAT_TRACKS_EX control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_DISK_FORMAT_TRACKS_EX
api_location:
- Ntdddisk.h
api_type:
- HeaderDef
---

# IOCTL\_DISK\_FORMAT\_TRACKS\_EX control code

Is similar to [**IOCTL\_DISK\_FORMAT\_TRACKS**](ioctl-disk-format-tracks.md), except that it allows the caller to specify several more parameters. The additional extended parameters are the format gap length, the number of sectors per track, and an array whose element size is equal to the number of sectors per track. This array represents the track layout.

## Input Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains the [**FORMAT\_EX\_PARAMETERS**](format-ex-parameters.md) data.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** in the I/O stack location of the IRP indicates the size, in bytes, of the buffer.

## Output Buffer

The device driver returns an array of BAD\_TRACK\_NUMBER values to the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**. BAD\_TRACK\_NUMBER is currently defined as a WORD on 32-bit systems.

## Output Buffer Length

Length of the buffer.

## Status block

The driver sets the **Status** field to STATUS\_SUCCESS. Otherwise, the driver sets the **Status** field to STATUS\_INVALID\_PARAMETER if the input buffer length is &lt; **sizeof**(FORMAT\_EX\_PARAMETERS) or if the format parameters supplied by the caller will not work on the drive to be formatted.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_DISK\_FORMAT\_TRACKS**](ioctl-disk-format-tracks.md)
</dt> <dt>

[**FORMAT\_EX\_PARAMETERS**](format-ex-parameters.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_DISK_FORMAT_TRACKS_EX%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






