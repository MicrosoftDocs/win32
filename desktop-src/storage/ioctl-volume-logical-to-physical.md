---
title: IOCTL\_VOLUME\_LOGICAL\_TO\_PHYSICAL control code
description: Returns physical offsets and physical disk numbers for a given volume logical offset.
ms.assetid: 'deadee81-4a6d-4c8b-80fd-46c29becc2cf'
keywords: ["IOCTL_VOLUME_LOGICAL_TO_PHYSICAL control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_VOLUME_LOGICAL_TO_PHYSICAL
api_location:
- Ntddvol.h
api_type:
- HeaderDef
---

# IOCTL\_VOLUME\_LOGICAL\_TO\_PHYSICAL control code

Returns physical offsets and physical disk numbers for a given volume logical offset.

For example, a logical volume offset inside a mirrored volume with two [*plex*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-plex) corresponds to two physical offsets, one in each of the two disks participating in the mirror. In response to this IOCTL, the volume manager returns two physical offsets and two physical disk numbers for the logical volume offset.

The volume manager supports this IOCTL for all types of basic and dynamic volumes.

## Input Buffer

Caller inserts the [**VOLUME\_LOGICAL\_OFFSET**](volume-logical-offset.md) structure containing the logical offset at the beginning of the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** in the I/O stack location of the IRP indicates the size, in bytes, of the input buffer, which must be greater than or equal to the value of **sizeof**(VOLUME\_LOGICAL\_OFFSET).

## Output Buffer

The output buffer size must be large enough to hold the structure [**VOLUME\_PHYSICAL\_OFFSETS**](volume-physical-offsets.md), which contains a variable-length array of structures of type [**VOLUME\_PHYSICAL\_OFFSET**](volume-physical-offset.md).

The volume manager returns one or more physical offsets and disk numbers in the VOLUME\_PHYSICAL\_OFFSETS structure at the beginning of the buffer, at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Output Buffer Length

**Parameters.DeviceIoControl.OutputBufferLength** in the I/O stack location of the IRP indicates the size, in bytes, of the output buffer.

## Status block

If the operation is successful, the **Status** member is set to STATUS\_SUCCESS. Otherwise, the **Status** member is set to the appropriate error code. Possible error codes include the following:

<dl> <dt>

<span id="STATUS_INVALID_PARAMETER"></span><span id="status_invalid_parameter"></span>STATUS\_INVALID\_PARAMETER
</dt> <dd>

The input buffer is too small.

</dd> </dl>

<dl> <dt>

<span id="STATUS_BUFFER_TOO_SMALL_"></span><span id="status_buffer_too_small_"></span>STATUS\_BUFFER\_TOO\_SMALL 
</dt> <dd>

The output buffer is too small. The volume manager sets the **Irp-&gt;IoStatus.Information** member to the size of the output buffer the caller should have provided.

</dd> </dl>

## Requirements



|                    |                                                                                                          |
|--------------------|----------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows XP.<br/>                                                           |
| Header<br/>  | <dl> <dt>Ntddvol.h (include Ntddvol.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_VOLUME\_PHYSICAL\_TO\_LOGICAL**](ioctl-volume-physical-to-logical.md)
</dt> <dt>

[**VOLUME\_LOGICAL\_OFFSET**](volume-logical-offset.md)
</dt> <dt>

[**VOLUME\_PHYSICAL\_OFFSETS**](volume-physical-offsets.md)
</dt> <dt>

[**VOLUME\_PHYSICAL\_OFFSET**](volume-physical-offset.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_VOLUME_LOGICAL_TO_PHYSICAL%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






