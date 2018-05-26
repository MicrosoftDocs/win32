---
title: IOCTL\_VOLUME\_PHYSICAL\_TO\_LOGICAL control code
description: Returns the logical offset corresponding to a physical disk number and a physical offset.
ms.assetid: 3e127456-6387-4340-84c1-d613d8094f33
keywords:
- IOCTL_VOLUME_PHYSICAL_TO_LOGICAL control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_VOLUME_PHYSICAL_TO_LOGICAL
api_location:
- Ntddvol.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOCTL\_VOLUME\_PHYSICAL\_TO\_LOGICAL control code

Returns the logical offset corresponding to a physical disk number and a physical offset.

The volume manager supports this IOCTL as described for all types of basic and dynamic volumes.

## Input Buffer

Caller inserts the [**VOLUME\_PHYSICAL\_OFFSET**](volume-physical-offset.md) structure, containing the physical offset and physical disk number, at the beginning of the buffer, at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** in the I/O stack location of the IRP indicates the size, in bytes, of the input buffer, which must be greater than or equal to the value of **sizeof**(VOLUME\_PHYSICAL\_OFFSET).

## Output Buffer

The volume manager returns the logical offset in the [**VOLUME\_LOGICAL\_OFFSET**](volume-logical-offset.md) structure at the beginning of the buffer, at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Output Buffer Length

**Parameters.DeviceIoControl.OutputBufferLength** in the I/O stack location of the IRP indicates the size, in bytes, of the output buffer, which must be greater than or equal to the value of **sizeof**(VOLUME\_LOGICAL\_OFFSET).

## Status block

If the operation is successful, the **Status** member is set to STATUS\_SUCCESS.

If either the input or output buffer is too small, the volume manager sets the **Status** member to STATUS\_BUFFER\_TOO\_SMALL. If data is returned in the output buffer but the buffer is too small to receive all of it, the volume manager sets the **Status** member to STATUS\_BUFFER\_OVERFLOW. The **Information** member is set to the size of the output buffer provided by the caller.

If the given physical disk number and physical offset do not belong to the volume or if they are taken from RAID parity data, this call will fail with STATUS\_INVALID\_PARAMETER.

## Requirements



|                    |                                                                                                          |
|--------------------|----------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows XP.<br/>                                                           |
| Header<br/>  | <dl> <dt>Ntddvol.h (include Ntddvol.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_VOLUME\_LOGICAL\_TO\_PHYSICAL**](ioctl-volume-logical-to-physical.md)
</dt> <dt>

[**VOLUME\_LOGICAL\_OFFSET**](volume-logical-offset.md)
</dt> <dt>

[**VOLUME\_PHYSICAL\_OFFSETS**](volume-physical-offsets.md)
</dt> <dt>

[**VOLUME\_PHYSICAL\_OFFSET**](volume-physical-offset.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_VOLUME_PHYSICAL_TO_LOGICAL%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






