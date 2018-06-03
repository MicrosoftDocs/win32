---
title: MOUNTMGR\_DRIVE\_LETTER\_INFORMATION structure
description: The MOUNTMGR\_DRIVE\_LETTER\_INFORMATION structure is used by the mount manager to furnish a drive letter to a client that has requested a driver letter by means of an IOCTL\_MOUNTMGR\_NEXT\_DRIVE\_LETTER request.
ms.assetid: ad8dc740-c297-43e7-beb9-d93019955fd3
keywords:
- MOUNTMGR_DRIVE_LETTER_INFORMATION structure Storage Devices
- PMOUNTMGR_DRIVE_LETTER_INFORMATION structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MOUNTMGR_DRIVE_LETTER_INFORMATION
api_location:
- mountmgr.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# MOUNTMGR\_DRIVE\_LETTER\_INFORMATION structure

The MOUNTMGR\_DRIVE\_LETTER\_INFORMATION structure is used by the mount manager to furnish a drive letter to a client that has requested a driver letter by means of an [**IOCTL\_MOUNTMGR\_NEXT\_DRIVE\_LETTER**](ioctl-mountmgr-next-drive-letter.md) request.

## Syntax


```C++
typedef struct _MOUNTMGR_DRIVE_LETTER_INFORMATION {
  BOOLEAN DriveLetterWasAssigned;
  UCHAR   CurrentDriveLetter;
} MOUNTMGR_DRIVE_LETTER_INFORMATION, *PMOUNTMGR_DRIVE_LETTER_INFORMATION;
```



## Members

<dl> <dt>

**DriveLetterWasAssigned**
</dt> <dd>

Indicates when **TRUE** that member **CurrentDriveLetter** contains a drive letter. When **FALSE**, a driver letter was not assigned to the device.

</dd> <dt>

**CurrentDriveLetter**
</dt> <dd>

Contains either an existing or a newly assigned drive letter in the form of a single ASCII character (for example, "D") if **DriveLetterWasAssigned** is **TRUE**.

</dd> </dl>

## Remarks

For a general discussion of the mount manager and how it communicates with its clients, see [Supporting Mount Manager Requests in a Storage Class Driver](https://msdn.microsoft.com/library/windows/hardware/ff567603).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mountmgr.h (include Mountmgr.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_MOUNTMGR\_NEXT\_DRIVE\_LETTER**](ioctl-mountmgr-next-drive-letter.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MOUNTMGR_DRIVE_LETTER_INFORMATION%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






