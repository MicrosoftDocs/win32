---
title: IDE\_MINIPORT\_RESOURCES structure
description: The IDE\_MINIPORT\_RESOURCES structure is used by the port driver to provide the miniport driver with resources.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: 867b6152-9846-484f-9eac-07d0f24d55df
keywords:
- IDE_MINIPORT_RESOURCES structure Storage Devices
- PIDE_MINIPORT_RESOURCES structure pointer Storage Devices
topic_type:
- apiref
api_name:
- IDE_MINIPORT_RESOURCES
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

# IDE\_MINIPORT\_RESOURCES structure

The IDE\_MINIPORT\_RESOURCES structure is used by the port driver to provide the miniport driver with resources.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef struct _IDE_MINIPORT_RESOURCES {
  ULONG             NumberOfAccessRanges;
  PIDE_ACCESS_RANGE IdeAccessRange;
} IDE_MINIPORT_RESOURCES, *PIDE_MINIPORT_RESOURCES;
```



## Members

<dl> <dt>

**NumberOfAccessRanges**
</dt> <dd>

Contains the number of access ranges pointed to by **IdeAccessRange**. Each is a range either of memory addresses or I/O port addresses.

</dd> <dt>

**IdeAccessRange**
</dt> <dd>

Pointer to the first address range in a series of contiguous address ranges defined by a structure of type [**IDE\_ACCESS\_RANGE**](ide-access-range.md). The value in the **NumberOfAccessRanges** member indicates how many address ranges are provided. The port driver populates each **IDE\_ACCESS\_RANGE** structure with the address ranges allocated for the controller.

</dd> </dl>

## Remarks

The port driver passes this structure to the miniport driver's [**IdeHwControl**](idehwcontrol.md) routine.

## Requirements



|                   |                                                                                                  |
|-------------------|--------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Irb.h (include Irb.h)</dt> </dl> |



## See also

<dl> <dt>

[**IDE\_ACCESS\_RANGE**](ide-access-range.md)
</dt> <dt>

[**IdeHwControl**](idehwcontrol.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IDE_MINIPORT_RESOURCES%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






