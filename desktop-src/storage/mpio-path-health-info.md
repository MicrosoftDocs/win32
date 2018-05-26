---
title: MPIO\_PATH\_HEALTH\_INFO structure
description: The MPIO\_PATH\_HEALTH\_INFO structure is used to query the available health information for every path that is exposed to the system.
ms.assetid: efb49852-3c0a-4dab-9d50-c103ba4a136b
keywords:
- MPIO_PATH_HEALTH_INFO structure Storage Devices
- PMPIO_PATH_HEALTH_INFO structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MPIO_PATH_HEALTH_INFO
api_location:
- mpiowmi.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MPIO\_PATH\_HEALTH\_INFO structure

The MPIO\_PATH\_HEALTH\_INFO structure is used to query the available health information for every path that is exposed to the system.

## Syntax


```C++
typedef struct _MPIO_PATH_HEALTH_INFO {
  ULONG                  NumberPathPackets;
  ULONG                  Reserved;
  MPIO_PATH_HEALTH_CLASS PathHealthPackets[1];
} MPIO_PATH_HEALTH_INFO, *PMPIO_PATH_HEALTH_INFO;
```



## Members

<dl> <dt>

**NumberPathPackets**
</dt> <dd>

An unsigned 32-bitfield that returns the number of health packets available that correspond to the number of available paths under MPIO control.

</dd> <dt>

**Reserved**
</dt> <dd>

Should be zero.

</dd> <dt>

**PathHealthPackets**
</dt> <dd>

A field that contains an array with health information about all the available paths under MPIO control. The number of elements of the array is given by NumberPathPackets and each element of the array is an instance of the MPIO\_PATH\_HEALTH\_CLASS structure.

</dd> </dl>

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mpiowmi.h (include Mpiowmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MPIO_PATH_HEALTH_INFO%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





