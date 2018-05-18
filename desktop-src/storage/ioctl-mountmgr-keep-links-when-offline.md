---
title: IOCTL\_MOUNTMGR\_KEEP\_LINKS\_WHEN\_OFFLINE control code
description: This IOCTL directs the mount manager to keep a symbolic link active after the Plug and Play manager has given notification that its corresponding volume has gone offline.
ms.assetid: '56af77f9-7c29-4bde-a8ae-9af23af4d296'
keywords: ["IOCTL_MOUNTMGR_KEEP_LINKS_WHEN_OFFLINE control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_MOUNTMGR_KEEP_LINKS_WHEN_OFFLINE
api_location:
- Mountmgr.h
api_type:
- HeaderDef
---

# IOCTL\_MOUNTMGR\_KEEP\_LINKS\_WHEN\_OFFLINE control code

This IOCTL directs the mount manager to keep a symbolic link active after the Plug and Play manager has given notification that its corresponding volume has gone offline. When the volume goes back online, the mount manager reassigns the symbolic link to the volume. No other volume is allowed to claim the symbolic link while its original owner is offline.

Clusters use this IOCTL to ensure that a node can continue to access a volume with the same drive letter, even if the volume is not continually present in the system.

## Input Buffer

The mount manager client loads the following structure with the symbolic link that will persist even after its volume is removed from the system. The initialized structure [**MOUNTMGR\_TARGET\_NAME**](mountmgr-target-name.md), defined in *Mountmgr.h*, is inserted at the beginning of the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** in the I/O stack location of the IRP indicates the size, in bytes, of the input buffer, which must be greater than or equal to **sizeof**(MOUNTMGR\_TARGET\_NAME).

## Output Buffer

None

## Output Buffer Length

None

## Status block

If the operation is successful, the **Status** field is set to STATUS\_SUCCESS.

The input buffer size, indicated by **InputBufferLength**, must be large enough to hold the structure MOUNTMGR\_TARGET\_NAME and the symbolic link name that follows it. If it is not large enough, the **Status** field is set to STATUS\_INVALID\_PARAMETER.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mountmgr.h (include Mountmgr.h)</dt> </dl> |



## See also

<dl> <dt>

[**MOUNTMGR\_TARGET\_NAME**](mountmgr-target-name.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_MOUNTMGR_KEEP_LINKS_WHEN_OFFLINE%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






