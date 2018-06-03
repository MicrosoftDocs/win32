---
title: MPIO\_DRIVE\_INFO structure
description: The MPIO\_DRIVE\_INFO structure represents a multi-path disk in the system.
ms.assetid: 38d79fae-9701-4e92-bf73-4732e02c17ab
keywords:
- MPIO_DRIVE_INFO structure Storage Devices
- PMPIO_DRIVE_INFO structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MPIO_DRIVE_INFO
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

# MPIO\_DRIVE\_INFO structure

The MPIO\_DRIVE\_INFO structure represents a multi-path disk in the system.

## Syntax


```C++
typedef struct _MPIO_DRIVE_INFO {
  ULONG NumberPaths;
  WCHAR Name[63 + 1];
  WCHAR SerialNumber[63 + 1];
  WCHAR DsmName[63 + 1];
} MPIO_DRIVE_INFO, *PMPIO_DRIVE_INFO;
```



## Members

<dl> <dt>

**NumberPaths**
</dt> <dd>

An unsigned 32-bitfield that represents the number of paths to the LUN.

</dd> <dt>

**Name**
</dt> <dd>

A string field (of maximum length 63 characters) that returns the device name that was created by MPIO for the LUN.

</dd> <dt>

**SerialNumber**
</dt> <dd>

A string field (of maximum length 63 characters) that returns the serial number that was created for the LUN by either the DSM or by MPIO itself.

</dd> <dt>

**DsmName**
</dt> <dd>

A string field (of maximum length 63 characters) that returns the friendly name of the controlling DSM for the device.

</dd> </dl>

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mpiowmi.h (include Mpiowmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MPIO_DRIVE_INFO%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





