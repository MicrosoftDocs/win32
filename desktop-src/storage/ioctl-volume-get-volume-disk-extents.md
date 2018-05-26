---
title: IOCTL\_VOLUME\_GET\_VOLUME\_DISK\_EXTENTS control code
description: Returns the physical location(s) of a volume on one or more disks.
ms.assetid: d831ea36-16ee-4723-95b1-f9903106b7c0
keywords:
- IOCTL_VOLUME_GET_VOLUME_DISK_EXTENTS control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_VOLUME_GET_VOLUME_DISK_EXTENTS
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

# IOCTL\_VOLUME\_GET\_VOLUME\_DISK\_EXTENTS control code

Returns the physical location(s) of a volume on one or more disks. Extents are initially stored in the order in which they are created, but remirroring, splitting, or breaking a mirror, or actions taken during disaster recovery, can affect the order of disk extents.

## Input Buffer

None.

## Input Buffer Length

None.

## Output Buffer

The driver returns a VOLUME\_DISK\_EXTENTS structure in the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**, which must be at least **sizeof**(VOLUME\_DISK\_EXTENTS).

## Output Buffer Length

The length of a VOLUME\_DISK\_EXTENTS structure.

## Status block

The driver sets **Irp-&gt;IoStatus.Information** and the **Status** field as follows:

-   If the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** is &lt; **sizeof**(VOLUME\_DISK\_EXTENTS), the driver sets **Irp-&gt;IoStatus.Information** to zero and returns STATUS\_INVALID\_PARAMETER.

-   If the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** is at least **sizeof**(VOLUME\_DISK\_EXTENTS) but too small for all data to be returned, the driver sets **Irp-&gt;IoStatus.Information** to **sizeof**(VOLUME\_DISK\_EXTENTS) and sets **Status** to STATUS\_BUFFER\_OVERFLOW.

-   If the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** is large enough for all data to be returned, the driver sets **Irp-&gt;IoStatus.Information** to **sizeof**(VOLUME\_DISK\_EXTENTS) + ((NumberOfDiskExtents - 1) \* **sizeof**(DISK\_EXTENT)) and sets **Status** to STATUS\_SUCCESS.

## Requirements



|                    |                                                                                                                                                                                                             |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available in Microsoft Windows 2000 for volumes on fixed disks, but not for volumes on removable media. Available for use with removable media in Microsoft Windows 2000 SP4 and Windows XP SP1.<br/> |
| Header<br/>  | <dl> <dt>Ntddvol.h (include Ntddvol.h)</dt> </dl>                                                                                                    |



## See also

<dl> <dt>

[**VOLUME\_DISK\_EXTENTS**](volume-disk-extents.md)
</dt> <dt>

[**DISK\_EXTENT**](disk-extent.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_VOLUME_GET_VOLUME_DISK_EXTENTS%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






