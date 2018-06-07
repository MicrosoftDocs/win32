---
title: IDE\_ACCESS\_RANGE structure
description: The IDE\_ACCESS\_RANGE structure contains the address ranges allocated for an IDE controller.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: e81441a2-0659-4d32-97f4-415abef6c87a
keywords:
- IDE_ACCESS_RANGE structure Storage Devices
- PIDE_ACCESS_RANGE structure pointer Storage Devices
topic_type:
- apiref
api_name:
- IDE_ACCESS_RANGE
api_location:
- irb.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# IDE\_ACCESS\_RANGE structure

The IDE\_ACCESS\_RANGE structure contains the address ranges allocated for an IDE controller.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef struct _IDE_ACCESS_RANGE {
  IDE_PHYSICAL_ADDRESS RangeStart;
  IDE_PHYSICAL_ADDRESS PhysicalRangeStart;
  ULONG                RangeLength;
  BOOLEAN              InMemory;
  UCHAR                Bar;
} IDE_ACCESS_RANGE, *PIDE_ACCESS_RANGE;
```



## Members

<dl> <dt>

**RangeStart**
</dt> <dd>

Contains the logical starting address of the address range.

</dd> <dt>

**PhysicalRangeStart**
</dt> <dd>

Contains the physical starting address of the address range.

</dd> <dt>

**RangeLength**
</dt> <dd>

Contains the size, in bytes, of the range.

</dd> <dt>

**InMemory**
</dt> <dd>

Flag that indicates if this is a memory mapped resource. If cleared, this is an I/O port resource.

</dd> <dt>

**Bar**
</dt> <dd>

The number of the PCI Base Address Range that this resource was found in.

</dd> </dl>

## Requirements



|                   |                                                                                                  |
|-------------------|--------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Irb.h (include Irb.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IDE_ACCESS_RANGE%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





