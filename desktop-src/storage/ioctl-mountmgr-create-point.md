---
title: IOCTL\_MOUNTMGR\_CREATE\_POINT control code
description: The mount manager clients can use this IOCTL to request that the mount manager create a persistent symbolic link name for the indicated volume.
ms.assetid: 580af31d-4122-48fe-a9da-097787f87620
keywords:
- IOCTL_MOUNTMGR_CREATE_POINT control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_MOUNTMGR_CREATE_POINT
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

# IOCTL\_MOUNTMGR\_CREATE\_POINT control code

The mount manager clients can use this IOCTL to request that the mount manager create a persistent symbolic link name for the indicated volume. For a discussion of the various sorts of persistent symbolic links managed by the mount manager, see [Supporting Mount Manager Requests in a Storage Class Driver](https://msdn.microsoft.com/library/windows/hardware/ff567603).

The input to this request is the persistent symbolic link name to be created and a name that is already valid for purposes of identifying the volume. The name given for purposes of identifying the volume can be of any type: a unique volume name, a symbolic link name, or a nonpersistent device name. If the new persistent name is not already in use, the call will succeed and the mount manager database will be modified to reflect that the new persistent name belongs to the volume. If the mount manager database already contains the new persistent name but the volume that owns that name is not in the system, this call will overwrite ownership of the given persistent name.

The mount manager allows the creation of a new persistent symbolic link name even if it has not yet been notified of the given volume in the MOUNTDEV\_MOUNTED\_DEVICE\_GUID device interface notification. In such a case, the mount manager simply creates the symbolic link and updates the mount manager database.

The mount manager enforces a policy of at most one persistent drive letter per volume. If an **IOCTL\_MOUNTMGR\_CREATE\_POINT** request is sent with a drive letter, the request will fail if there is already a drive letter assigned to the volume, unless the mount manager has not yet been notified of the volume by means of the MOUNTDEV\_MOUNTED\_DEVICE\_GUID device interface notification. In the latter case, the call succeeds and the mount manager purges the mount manager database of any other drive letters previously assigned to the volume.

If IOCTL\_MOUNTMGR\_CREATE\_POINT specifies a drive letter, the drive letter must be upper case.

Note that a client can discover whether the mount manager has received the MOUNTDEV\_MOUNTED\_DEVICE\_GUID device interface notification for its volume by querying the mount manager with [**IOCTL\_MOUNTMGR\_QUERY\_POINTS**](ioctl-mountmgr-query-points.md).

In this pseudocode sample, a mount manager client uses IOCTL\_MOUNTMGR\_CREATE\_POINT to send the mount manager a device object name and its corresponding symbolic link:


```
    // The persistent symbolic link is a drive letter in
    // this case:
    wsprintf(dosBuffer, L"\\DosDevices\\%C:", DriveLetter);
    RtlInitUnicodeString(&amp;dosName, dosBuffer);
    // The nonpersistent volume (device) object name is
    // formed using the volume number as a suffix
    wsprintf(ntBuffer, L"\\Device\\HarddiskVolume%D", 
                       Extension->VolumeNumber);
    RtlInitUnicodeString(&amp;ntName, ntBuffer);
    createPointSize = sizeof(MOUNTMGR_CREATE_POINT_INPUT) +
                      dosName.Length + ntName.Length;
    // Allocate a header with length and offset information
    createPoint = (PMOUNTMGR_CREATE_POINT_INPUT)
                  ExAllocatePool(PagedPool, 
                  createPointSize);
    createPoint->SymbolicLinkNameOffset = 
                  sizeof(MOUNTMGR_CREATE_POINT_INPUT);
    createPoint->SymbolicLinkNameLength = dosName.Length;
    createPoint->DeviceNameOffset = 
        createPoint -> SymbolicLinkNameOffset +
        createPoint -> SymbolicLinkNameLength;
    createPoint->DeviceNameLength = ntName.Length;
    RtlCopyMemory((PCHAR) createPoint + 
                  createPoint -> SymbolicLinkNameOffset,
                  dosName.Buffer, dosName.Length);
    RtlCopyMemory((PCHAR) createPoint + 
                  createPoint->DeviceNameOffset,
                  ntName.Buffer, ntName.Length);
    // Use the name of the mount manager device object
    // defined in mountmgr.h (MOUNTMGR_DEVICE_NAME) to
    // obtain a pointer to the mount manager.
    RtlInitUnicodeString(&amp;name, MOUNTMGR_DEVICE_NAME);
    status = IoGetDeviceObjectPointer(&amp;name,
                              FILE_READ_ATTRIBUTES, 
                              &amp;fileObject, &amp;deviceObject);
    KeInitializeEvent(&amp;event, NotificationEvent, FALSE);
    irp = IoBuildDeviceIoControlRequest(
            IOCTL_MOUNTMGR_CREATE_POINT,
            deviceObject, createPoint, createPointSize, 
            NULL, 0, FALSE, &amp;event, &amp;ioStatus);
    // Send the irp to the mount manager requesting
    // that a new mount point (persistent symbolic link)
    // be created for the indicated volume.
    status = IoCallDriver(deviceObject, irp);
```



## Input Buffer

The mount point manager places a header, defined as the structure [**MOUNTMGR\_CREATE\_POINT\_INPUT**](mountmgr-create-point-input.md) in *Mountmgr.h*, at the beginning of the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**. The mount manager inserts the newly-assigned persistent symbolic link name at the address pointed to by the *SymbolicLinkNameOffset* member of this structure, and it inserts the nonpersistent device name at the address pointed to by the *DeviceNameOffset* member of this structure.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** in the I/O stack location of the IRP indicates the size, in bytes, of the input buffer, which must be greater than or equal to **sizeof**(MOUNTMGR\_CREATE\_POINT\_INPUT).

## Output Buffer

None

## Output Buffer Length

None

## Status block

If the operation is successful, the **Status** field is set to STATUS\_SUCCESS.

If **InputBufferLength** is less than **sizeof**(MOUNTMGR\_CREATE\_POINT\_INPUT), the **Status** field is set to STATUS\_INVALID\_PARAMETER.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mountmgr.h (include Mountmgr.h)</dt> </dl> |



## See also

<dl> <dt>

[**MOUNTMGR\_CREATE\_POINT\_INPUT**](mountmgr-create-point-input.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_MOUNTMGR_CREATE_POINT%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






