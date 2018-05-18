---
title: IOCTL\_MOUNTMGR\_VOLUME\_ARRIVAL\_NOTIFICATION control code
description: This IOCTL allows a client to simulate a Plug and Play device interface arrival notification with the given volume name.
ms.assetid: '0c27c49e-a06c-4781-9d7f-50f15f9715ac'
keywords: ["IOCTL_MOUNTMGR_VOLUME_ARRIVAL_NOTIFICATION control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_MOUNTMGR_VOLUME_ARRIVAL_NOTIFICATION
api_location:
- Mountmgr.h
api_type:
- HeaderDef
---

# IOCTL\_MOUNTMGR\_VOLUME\_ARRIVAL\_NOTIFICATION control code

This IOCTL allows a client to simulate a Plug and Play device interface arrival notification with the given volume name. If a client does not register a device interface of type MOUNTDEV\_MOUNTED\_DEVICE\_GUID, the mount manager is not alerted of its arrival. However, the client can alert the mount manager of its volume's arrival directly by means of this IOCTL.

This IOCTL allows clients to obtain drive letters for newly created volumes during text mode setup when the Plug and Play device installer is not running.

Clients that have registered a device interface of type MOUNTDEV\_MOUNTED\_DEVICE\_GUID in the normal way should not use this IOCTL.

## Input Buffer

The mount manager client loads the following structure with the nonpersistent target device name. The initialized structure, [**MOUNTMGR\_TARGET\_NAME**](mountmgr-target-name.md), defined in *Mountmgr.h*, is inserted at the beginning of the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_MOUNTMGR_VOLUME_ARRIVAL_NOTIFICATION%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






