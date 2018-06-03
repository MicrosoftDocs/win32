---
title: ClearMpioDiskHealthCounters\_IN structure
description: The ClearMpioDiskHealthCounters\_IN structure is used to provide an input parameter to the ClearMpioDiskHealthCounters method.
ms.assetid: 1af28545-f43f-47a2-b6a2-64fd7a408687
keywords:
- ClearMpioDiskHealthCounters_IN structure Storage Devices
- PClearMpioDiskHealthCounters_IN structure pointer Storage Devices
topic_type:
- apiref
api_name:
- ClearMpioDiskHealthCounters_IN
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

# ClearMpioDiskHealthCounters\_IN structure

The ClearMpioDiskHealthCounters\_IN structure is used to provide an input parameter to the ClearMpioDiskHealthCounters method.

## Syntax


```C++
typedef struct _ClearMpioDiskHealthCounters_IN {
  ULONG DiskOrdinal;
} ClearMpioDiskHealthCounters_IN, *PClearMpioDiskHealthCounters_IN;
```



## Members

<dl> <dt>

**DiskOrdinal**
</dt> <dd>

A 32-bitfield that represents the MPIO disk ordinal value.

</dd> </dl>

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mpiowmi.h (include Mpiowmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ClearMpioDiskHealthCounters_IN%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





