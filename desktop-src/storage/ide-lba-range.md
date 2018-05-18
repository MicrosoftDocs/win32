---
title: IDE\_LBA\_RANGE structure
description: The IDE\_LBA\_RANGE structure is used by the port driver to provide the miniport driver with a range of logical blocks.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: '2d823d9c-7328-44e2-9ba2-22967471ef68'
keywords: ["IDE_LBA_RANGE structure Storage Devices", "PIDE_LBA_RANGE structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- IDE_LBA_RANGE
api_location:
- irb.h
api_type:
- HeaderDef
---

# IDE\_LBA\_RANGE structure

The IDE\_LBA\_RANGE structure is used by the port driver to provide the miniport driver with a range of logical blocks.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef struct _IDE_LBA_RANGE {
  ULONGLONG StartSector  :48;
  ULONGLONG SectorCount  :16;
} IDE_LBA_RANGE, *PIDE_LBA_RANGE;
```



## Members

<dl> <dt>

**StartSector**
</dt> <dd>

Contains the starting sector of the LBA range.

</dd> <dt>

**SectorCount**
</dt> <dd>

Contains the sector count of the LBA range.

</dd> </dl>

## Remarks

## Requirements



|                   |                                                                                                  |
|-------------------|--------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Irb.h (include Irb.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IDE_LBA_RANGE%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





