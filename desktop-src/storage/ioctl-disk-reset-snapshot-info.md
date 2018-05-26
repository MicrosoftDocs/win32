---
title: IOCTL\_DISK\_RESET\_SNAPSHOT\_INFO control code
description: Clears all volume shadow copy service (VSS) hardware-based snapshot information from the disk.
ms.assetid: b22b00de-4711-4896-a21c-33fbc7b1d64e
keywords:
- IOCTL_DISK_RESET_SNAPSHOT_INFO control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_DISK_RESET_SNAPSHOT_INFO
api_location:
- Ntdddisk.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOCTL\_DISK\_RESET\_SNAPSHOT\_INFO control code

Clears all volume shadow copy service (VSS) hardware-based snapshot information from the disk. A snapshot is also known as a shadow copy. This request is available in Windows Vista and later versions of the Windows operating systems. The caller must be running at IRQL = PASSIVE\_LEVEL.

## Input Buffer

None.

## Input Buffer Length

None.

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

The **Information** member is set to zero. The **Status** member is set to STATUS\_SUCCESS if the operation was successful. Otherwise, the **Status** member is set to the appropriate error code.

## Remarks

This I/O control code can be issued from either a kernel-mode driver or a user-mode application. When this I/O control code is issued from a kernel-mode driver, the caller provides an I/O Request Packet (IRP) that contains an IO\_STATUS\_BLOCK data structure. This data structure is used to return error information to the caller. When this I/O control code is issued from a user-mode application with the **DeviceIocontrol** routine, the caller can obtain error information by calling the **GetLastError** routine.

The disk whose handle is used when this IOCTL is issued might be in the offline state when the IOCTL is issued. If the disk is put in the offline state by using the disk manager Microsoft Management Console (MMC) snap-in, the disk will have its read-only attribute set, which will cause this IOCTL to fail. However, if the disk partition utility (Diskpart.exe) is used to put the disk in the offline state, the read-only attribute for the disk is not set. For this reason, it is best to use the disk partition utility to put a disk in the offline state.

> [!Note]  
> A side effect of using this IOCTL is that Disk Management tools may report an additional partition of the type "UNKNOWN" on GPT disks. This 256 kilobyte partition is created by the IOCTL operation and is a snapshot partition used in the restore process. This partition is expected and can be ignored by system administrators.

 

## Requirements



|                    |                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows Vista.<br/>                                                          |
| Header<br/>  | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |
| IRQL<br/>    | PASSIVE\_LEVEL<br/>                                                                                  |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_DISK_RESET_SNAPSHOT_INFO%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





