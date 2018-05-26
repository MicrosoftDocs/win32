---
title: IOCTL\_MOUNTMGR\_CHANGE\_NOTIFY control code
description: Clients send this IOCTL to the mount manager to be informed whenever there is a change in the mount managers persistent symbolic link name database.
ms.assetid: ad6ab15b-6789-4ee8-ba99-9eaa6eec070a
keywords:
- IOCTL_MOUNTMGR_CHANGE_NOTIFY control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_MOUNTMGR_CHANGE_NOTIFY
api_location:
- Mountmgr.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOCTL\_MOUNTMGR\_CHANGE\_NOTIFY control code

Clients send this IOCTL to the mount manager to be informed whenever there is a change in the mount manager's persistent symbolic link name database.

The mount manager maintains a counter called *EpicNumber* that records how many changes have occurred in its persistent name database since the last startup. Clients send a number to the mount manager with every change notification request IRP, and the mount manager responds in the following manner:

-   If the number supplied by the client is not equal to *EpicNumber*, the mount manager returns STATUS\_SUCCESS, indicating that changes have occurred since the client last compared its number with the mount manager's *EpicNumber*.

-   If the number supplied by the client is equal to *EpicNumber*, the mount manager interprets this as a request to be informed of the next change to the persistent name database, and it queues the change notification IRP and returns STATUS\_PENDING. Whenever a change occurs in the database, the mount manager completes all of the pending change notification IRPs, thereby informing clients of the change.

A client that only wants to be informed of the changes to a particular volume is advised to register for Plug and Play target device notification and watch for GUID\_IO\_VOLUME\_NAME\_CHANGE.

## Input Buffer

The mount manager client initializes the [**MOUNTMGR\_CHANGE\_NOTIFY\_INFO**](mountmgr-change-notify-info.md) structure, defined in *Mountmgr.h*, at the beginning of the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** in the I/O stack location of the IRP indicates the size, in bytes, of the input buffer, which must be greater than or equal to **sizeof**(MOUNTMGR\_CHANGE\_NOTIFY\_INFO).

## Output Buffer

The mount manager returns the current *EpicNumber* in the [**MOUNTMGR\_CHANGE\_NOTIFY\_INFO**](mountmgr-change-notify-info.md) structure, defined in *Mountmgr.h*, at the beginning of the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Status block

If the operation is successful, the **Status** field is set to STATUS\_SUCCESS and the **Information** field is set to **sizeof**(MOUNTMGR\_CHANGE\_NOTIFY\_INFO).

If **InputBufferLength** is less than **sizeof**(MOUNTMGR\_CHANGE\_NOTIFY\_INFO) or **OutputBufferLength** is less than **sizeof**(MOUNTMGR\_CHANGE\_NOTIFY\_INFO), the **Status** field is set to STATUS\_INVALID\_PARAMETER.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mountmgr.h (include Mountmgr.h)</dt> </dl> |



## See also

<dl> <dt>

[**MOUNTMGR\_CHANGE\_NOTIFY\_INFO**](mountmgr-change-notify-info.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_MOUNTMGR_CHANGE_NOTIFY%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






