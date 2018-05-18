---
title: IOCTL\_VOLUME\_READ\_PLEX control code
description: Performs a read on a specific plex of a volume.
ms.assetid: '187e15d2-b527-4dab-81ea-498663363f8b'
keywords: ["IOCTL_VOLUME_READ_PLEX control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_VOLUME_READ_PLEX
api_location:
- Ntddvol.h
api_type:
- HeaderDef
---

# IOCTL\_VOLUME\_READ\_PLEX control code

Performs a read on a specific [*plex*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-plex) of a volume. Because all plexes are identical, the volume manager can retrieve data from any of a volume's plexes during a normal read operation. The volume manager spreads reads among a volume's plexes, to balance the I/O load on the physical media and to maximize read performance.

If, however, an application or kernel-mode component must read data from a particular plex instead of letting the volume manager pick one, it can use this IOCTL to do so.

## Input Buffer

Caller inserts the [**VOLUME\_READ\_PLEX\_INPUT**](volume-read-plex-input.md) structure, containing the logical offset, at the beginning of the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** in the I/O stack location of the IRP indicates the size, in bytes, of the input buffer, which must be greater than or equal to the value of **sizeof**(VOLUME\_READ\_PLEX\_INPUT).

## Output Buffer

Like [**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff550794), this IOCTL stores the read data in the memory buffer passed as a memory descriptor list (MDL) in the **Irp-&gt;MdlAddress** field.

## Output Buffer Length

The length of the buffer.

## Status block

If the operation is successful, the volume manager sets the **Status** field to STATUS\_SUCCESS.

The VOLUME\_READ\_PLEX\_INPUT structure at **Irp-&gt;AssociatedIrp.SystemBuffer** has a **Length** member that must be aligned on a 512-byte boundary. If **Length** does not have the proper alignment, the operation fails and the volume manager sets the **Status** field to VKE\_EINVAL.

## Requirements



|                    |                                                                                                          |
|--------------------|----------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows XP.<br/>                                                           |
| Header<br/>  | <dl> <dt>Ntddvol.h (include Ntddvol.h)</dt> </dl> |



## See also

<dl> <dt>

[**VOLUME\_READ\_PLEX\_INPUT**](volume-read-plex-input.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_VOLUME_READ_PLEX%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






