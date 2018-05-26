---
title: MEMORY\_REGION structure
description: The MEMORY\_REGION structure describes a region of physically contiguous memory.
ms.assetid: b8dbc3d4-7a70-4ec6-b7b0-2b0877fb9722
keywords:
- MEMORY_REGION structure Storage Devices
- PMEMORY_REGION structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MEMORY_REGION
api_location:
- storport.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MEMORY\_REGION structure

The MEMORY\_REGION structure describes a region of physically contiguous memory.

## Syntax


```C++
typedef struct _MEMORY_REGION {
  PUCHAR           VirtualBase;
  PHYSICAL_ADDRESS PhysicalBase;
  ULONG            Length;
} MEMORY_REGION, *PMEMORY_REGION;
```



## Members

<dl> <dt>

**VirtualBase**
</dt> <dd>

The beginning virtual address of the memory region.

</dd> <dt>

**PhysicalBase**
</dt> <dd>

The beginning physical address of the memory region.

</dd> <dt>

**Length**
</dt> <dd>

The size, in bytes, of the memory region.

</dd> </dl>

## Remarks

The **DumpRegion** member of the [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md) structure holds a MEMORY\_REGION structure that describes a region of physically contiguous memory that a miniport driver can use during a crash dump.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Storport.h (include Storport.h)</dt> </dl> |



## See also

<dl> <dt>

[**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MEMORY_REGION%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






