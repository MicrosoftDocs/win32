---
title: ScsiPortMoveMemory routine
description: The ScsiPortMoveMemory routine copies data from one location to another.Note The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future.
ms.assetid: c4ed9551-3dc8-4f76-9bcb-26030f76c244
keywords:
- ScsiPortMoveMemory routine Storage Devices
topic_type:
- apiref
api_name:
- ScsiPortMoveMemory
api_location:
- storport.lib
- storport.dll
api_type:
- LibDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ScsiPortMoveMemory routine

The **ScsiPortMoveMemory** routine copies data from one location to another.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
VOID ScsiPortMoveMemory(
  _In_ PVOID WriteBuffer,
  _In_ PVOID ReadBuffer,
  _In_ ULONG Length
);
```



## Parameters

<dl> <dt>

*WriteBuffer* \[in\]
</dt> <dd>

Pointer to the destination buffer.

</dd> <dt>

*ReadBuffer* \[in\]
</dt> <dd>

Pointer to the source buffer.

</dd> <dt>

*Length* \[in\]
</dt> <dd>

Specifies how many bytes to transfer from *ReadBuffer* to *WriteBuffer*.

</dd> </dl>

## Return value

None

## Remarks

**ScsiPortMoveMemory** can be called if a miniport driver needs to copy data from one system-allocated area to another. For example, a miniport driver might call **ScsiPortMoveMemory** to copy pertinent SRB values into the driver's SRB extension.

The (*ReadBuffer* + *Length*) can overlap the area pointed to by *WriteBuffer*.

Each of the given buffer areas must be at least **sizeof**(*Length*).

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Srb.h</dt> </dl>                                                        |
| Library<br/>         | <dl> <dt>Storport.lib</dt> </dl>                                                 |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ScsiPortMoveMemory%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





