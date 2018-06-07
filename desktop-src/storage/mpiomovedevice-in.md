---
title: MPIOMoveDevice\_IN structure
description: The MPIOMoveDevice\_IN structure is used to set the active path on the device.
ms.assetid: 2652874f-70d0-4eff-a46d-778a68d55cab
keywords:
- MPIOMoveDevice_IN structure Storage Devices
- PMPIOMoveDevice_IN structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MPIOMoveDevice_IN
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

# MPIOMoveDevice\_IN structure

The MPIOMoveDevice\_IN structure is used to set the active path on the device.

## Syntax


```C++
typedef struct _MPIOMoveDevice_IN {
  ULONG     DiskOrdinal;
  ULONG     Flags;
  ULONGLONG PathID;
} MPIOMoveDevice_IN, *PMPIOMoveDevice_IN;
```



## Members

<dl> <dt>

**DiskOrdinal**
</dt> <dd>

A 32-bitfield that specifies the MPIO disk ordinal value.

</dd> <dt>

**Flags**
</dt> <dd>

A 32-bitfield that specifies the flags that are associated with the device move operation.

</dd> <dt>

**PathID**
</dt> <dd>

A 64-bitfield that specifies the path that is associated with the device.

</dd> </dl>

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mpiowmi.h (include Mpiowmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MPIOMoveDevice_IN%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





