---
title: MOUNTMGR\_DRIVE\_LETTER\_TARGET structure
description: The MOUNTMGR\_DRIVE\_LETTER\_TARGET structure is used by a mount manager client with an IOCTL\_MOUNTMGR\_NEXT\_DRIVE\_LETTER request to furnish a nonpersistent target device name to the mount manager.
ms.assetid: 3bbfd3f8-9530-4c9f-99e3-a1fcbb956b51
keywords:
- MOUNTMGR_DRIVE_LETTER_TARGET structure Storage Devices
- PMOUNTMGR_DRIVE_LETTER_TARGET structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MOUNTMGR_DRIVE_LETTER_TARGET
api_location:
- mountmgr.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MOUNTMGR\_DRIVE\_LETTER\_TARGET structure

The MOUNTMGR\_DRIVE\_LETTER\_TARGET structure is used by a mount manager client with an [**IOCTL\_MOUNTMGR\_NEXT\_DRIVE\_LETTER**](ioctl-mountmgr-next-drive-letter.md) request to furnish a nonpersistent target device name to the mount manager.

## Syntax


```C++
typedef struct _MOUNTMGR_DRIVE_LETTER_TARGET {
  USHORT DeviceNameLength;
  WCHAR  DeviceName[1];
} MOUNTMGR_DRIVE_LETTER_TARGET, *PMOUNTMGR_DRIVE_LETTER_TARGET;
```



## Members

<dl> <dt>

**DeviceNameLength**
</dt> <dd>

Contains the length, in bytes, of device name.

</dd> <dt>

**DeviceName**
</dt> <dd>

Contains the nonpersistent target device name.

</dd> </dl>

## Remarks

The mount manager responds to the IOCTL\_MOUNTMGR\_NEXT\_DRIVE\_LETTER request by furnishing the client with a drive letter for the target device.

Nonpersistent target names must contain the full path of a target object name in the system object tree. For example: "\\Device\\HarddiskVolume1". For a discussion of the difference between drive letters and nonpersistent target device names, see [Supporting Mount Manager Requests in a Storage Class Driver](https://msdn.microsoft.com/library/windows/hardware/ff567603).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mountmgr.h (include Mountmgr.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_MOUNTMGR\_NEXT\_DRIVE\_LETTER**](ioctl-mountmgr-next-drive-letter.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MOUNTMGR_DRIVE_LETTER_TARGET%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






