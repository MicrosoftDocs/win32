---
title: ENUM\_PDO\_RESULTS structure
description: This structure describes a result set of Physical Device Objects (PDOs) that are enumerated with IOCTL\_EHSTOR\_DEVICE\_ENUMERATE\_PDOS.
ms.assetid: 80553c9e-3e80-4219-8cc0-2bd4dd6fa76b
keywords:
- ENUM_PDO_RESULTS structure Storage Devices
- PENUM_PDO_RESULTS structure pointer Storage Devices
topic_type:
- apiref
api_name:
- ENUM_PDO_RESULTS
api_location:
- EhStorIoctl.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ENUM\_PDO\_RESULTS structure

This structure describes a result set of Physical Device Objects (PDOs) that are enumerated with [**IOCTL\_EHSTOR\_DEVICE\_ENUMERATE\_PDOS**](ioctl-ehstor-device-enumerate-pdos.md).

## Syntax


```C++
typedef struct _ENUM_PDO_RESULTS {
  ULONG          cEntries;
  ENUM_PDO_ENTRY rgEntries[ANYSIZE_ARRAY];
} ENUM_PDO_RESULTS, *PENUM_PDO_RESULTS;
```



## Members

<dl> <dt>

**cEntries**
</dt> <dd>

This member indicates the number of entries in the array of ENUM\_PDO\_ENTRY structures.

</dd> <dt>

**rgEntries**
</dt> <dd>

This member contains the array of ENUM\_PDO\_ENTRY structures.

</dd> </dl>

## Remarks

## Requirements



|                   |                                                                                                                  |
|-------------------|------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>EhStorIoctl.h (include EhStorIoctl.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_EHSTOR\_DEVICE\_ENUMERATE\_PDOS**](ioctl-ehstor-device-enumerate-pdos.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ENUM_PDO_RESULTS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






