---
title: IOCTL\_MOUNTMGR\_QUERY\_POINTS control code
description: This IOCTL returns triples that consist of a persistent symbolic link name for the volume (that is, a mount point), a unique ID for the volume, and a nonpersistent device name (such as \ 0034;\\Device\\HarddiskVolume1 \ 0034;) for the volume.
ms.assetid: '2b7f947c-2fb1-4b59-bf73-a6f0e1478be2'
keywords: ["IOCTL_MOUNTMGR_QUERY_POINTS control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_MOUNTMGR_QUERY_POINTS
api_location:
- Mountmgr.h
api_type:
- HeaderDef
---

# IOCTL\_MOUNTMGR\_QUERY\_POINTS control code

This IOCTL returns triples that consist of a persistent symbolic link name for the volume (that is, a mount point), a unique ID for the volume, and a nonpersistent device name (such as "\\Device\\HarddiskVolume1") for the volume. The input to this IOCTL is a [**MOUNTMGR\_MOUNT\_POINT**](mountmgr-mount-point.md) structure that contains a single triple.

If the input triple contains a unique ID or a non-persistent device name, the request retrieves all associated mount points (symbolic links), including the volume GUID pathname and the drive letters. However, if the input triple has a symbolic link, but does not specify either the unique ID or the device name, the request only returns a single triple that contains the symbolic link that was provided in the input, together with the unique ID and the device name. The caller must submit another IOCTL with either the unique ID or the device name to retrieve the remaining mount points.

If the input triple is empty, the mount manager returns the entire mounted device list.

The mount manager returns triples that match as much info as is provided by the caller. If the caller submits the unique ID, the mount manager returns all triples with that unique ID. If the caller inputs the volume pathname or a drive letter as the symbolic link name, the mount manager returns only the triple for the symbolic link. There is one entry per symbolic link. If the caller inputs a device pathname, the mount manager returns only the triples for that device pathname. If the caller inputs a unique ID and a symbolic link, again, the mount manager returns only one entry for that symbolic link. A caller would do this to get the device pathname. If the caller inputs no device pathname, unique ID or symbolic link, the mount manager returns all entries/triples.

## Input Buffer

The mount manager client initializes the [**MOUNTMGR\_MOUNT\_POINT**](mountmgr-mount-point.md) structure, defined in *Mountmgr.h*, at the beginning of the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**. Immediately following this structure, the MM client loads the symbolic link name, the unique ID and the device name, in that order.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** in the I/O stack location of the IRP indicates the size, in bytes, of the input buffer, which must be greater than or equal to **sizeof**(MOUNTMGR\_MOUNT\_POINT).

## Output Buffer

The mount manager initializes a variable-length structure of type [**MOUNTMGR\_MOUNT\_POINTS**](mountmgr-mount-points.md), defined in *Mountmgr.h*, at the beginning of the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**. The mount manager inserts the mount points, associated with the indicated volume, at the address pointed to by the *MountPoints\[\]* member of this structure. Each mount point is represented by a MOUNTMGR\_MOUNT\_POINT structure as defined in the **Input** section for this IOCTL.

## Status block

If the operation is successful, the **Status** field is set to STATUS\_SUCCESS.

If neither the unique ID nor the nonpersistent device name are found in the volumes mounted device list, the **Status** field is set to STATUS\_INVALID\_PARAMETER.

If **InputBufferLength** is less than **sizeof**(MOUNTMGR\_MOUNT\_POINT), the **Status** field is set to STATUS\_INVALID\_PARAMETER.

If **InputBufferLength** is less than the total length of the three input ID strings, the **Status** field is set to STATUS\_INVALID\_PARAMETER.

If **OutputBufferLength** is less than **sizeof**(MOUNTMGR\_MOUNT\_POINT), the **Status** field is set to STATUS\_INVALID\_PARAMETER.

If **OutputBufferLength** is less than **sizeof**(MOUNTMGR\_MOUNT\_POINTS) plus the sum of the sizes of the mount point triples, the **Status** field is set to STATUS\_BUFFER\_OVERFLOW.

If any of the three strings contained within any of the triples is aligned on an odd address (for example, address & 01 != 0), the **Status** field is set to STATUS\_INVALID\_PARAMETER.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mountmgr.h (include Mountmgr.h)</dt> </dl> |



## See also

<dl> <dt>

[**MOUNTMGR\_MOUNT\_POINTS**](mountmgr-mount-points.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_MOUNTMGR_QUERY_POINTS%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






