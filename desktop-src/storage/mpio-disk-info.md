---
title: MPIO\_DISK\_INFO structure
description: The MPIO\_DISK\_INFO structure allows applications to query the system for the top level view of its disk topology. The request must be directed to the MPIO control object by using its WMI instance name.
ms.assetid: edefb7f5-f423-48cc-81c9-16153c228d45
keywords:
- MPIO_DISK_INFO structure Storage Devices
- PMPIO_DISK_INFO structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MPIO_DISK_INFO
api_location:
- mpiowmi.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# MPIO\_DISK\_INFO structure

The MPIO\_DISK\_INFO structure allows applications to query the system for the top level view of its disk topology. The request must be directed to the MPIO control object by using its WMI instance name.

## Syntax


```C++
typedef struct _MPIO_DISK_INFO {
  ULONG           NumberDrives;
  MPIO_DRIVE_INFO DriveInfo[1];
} MPIO_DISK_INFO, *PMPIO_DISK_INFO;
```



## Members

<dl> <dt>

**NumberDrives**
</dt> <dd>

An unsigned 32-bitfield that represents the number of multi-path disks in the system.

</dd> <dt>

**DriveInfo**
</dt> <dd>

An array that returns the information representing each multi-path LUN (pseudo-LUN) in the system. The number of elements in the array is given by *NumberDrives* and each element represents an instance of an MPIO\_DRIVE\_INFO structure.

</dd> </dl>

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mpiowmi.h (include Mpiowmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MPIO_DISK_INFO%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





