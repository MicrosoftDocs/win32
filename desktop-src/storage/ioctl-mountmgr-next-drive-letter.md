---
title: IOCTL\_MOUNTMGR\_NEXT\_DRIVE\_LETTER control code
description: This IOCTL checks to see if the given volume has a drive letter.
ms.assetid: 7e3c5718-180c-435d-89ea-30a5cac325b2
keywords:
- IOCTL_MOUNTMGR_NEXT_DRIVE_LETTER control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_MOUNTMGR_NEXT_DRIVE_LETTER
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

# IOCTL\_MOUNTMGR\_NEXT\_DRIVE\_LETTER control code

This IOCTL checks to see if the given volume has a drive letter. If it already has a drive letter, or if the volume has a special mount manager database entry indicating that it does not require a drive letter, this routine returns the current drive letter (if there is one) and does nothing. If the given volume does not have a drive letter and does not have a special mount manager database entry indicating that it does not require a drive letter, the next available drive letter is assigned to the volume. If the volume's nonpersistent device name begins with "\\Device\\Floppy", the mount manager will check for available drive letters starting with the letter "A." If the volume name begins with "\\Device\\CdRom" the mount manager will check for available drive letters starting with drive letter "D." In all other cases, the mount manager starts with drive letter "C."

## Input Buffer

The mount manager client initializes the [**MOUNTMGR\_DRIVE\_LETTER\_TARGET**](mountmgr-drive-letter-target.md) structure, defined in *Mountmgr.h*, at the beginning of the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**. The client must insert the name of the target volume at the address pointed to by the *DeviceName\[\]* member of this structure. The target volume name is the name of the nonpersistent device object associated with the volume (for example, "\\Device\\HarddiskVolume1").

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** in the I/O stack location of the IRP indicates the size, in bytes, of the input buffer, which must be greater than or equal to **sizeof**(MOUNTMGR\_DRIVE\_LETTER\_TARGET).

## Output Buffer

The mount manager inserts either the current drive letter or the newly assigned drive letter (see previous discussion) in the [**MOUNTMGR\_DRIVE\_LETTER\_INFORMATION**](mountmgr-drive-letter-information.md) structure, defined in *Mountmgr.h*, at the beginning of the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Output Buffer Length

**Parameters.DeviceIoControl.OutputBufferLength** in the I/O stack location of the IRP indicates the size, in bytes, of the output buffer, which must be greater than or equal to **sizeof**(MOUNTMGR\_DRIVE\_LETTER\_INFORMATION).

## Status block

If the operation is successful , the **Status** field is set to STATUS\_SUCCESS.

If **InputBufferLength** is less than **sizeof**(MOUNTMGR\_DRIVE\_LETTER\_TARGET) or if **OutputBufferLength** is less than **sizeof**(MOUNTMGR\_DRIVE\_LETTER\_INFORMATION), the **Status** field is set to STATUS\_INVALID\_PARAMETER.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mountmgr.h (include Mountmgr.h)</dt> </dl> |



## See also

<dl> <dt>

[**MOUNTMGR\_DRIVE\_LETTER\_TARGET**](mountmgr-drive-letter-target.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_MOUNTMGR_NEXT_DRIVE_LETTER%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






