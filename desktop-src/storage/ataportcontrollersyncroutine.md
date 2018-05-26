---
title: AtaPortControllerSyncRoutine routine
description: The AtaPortControllerSyncRoutine routine provides synchronized access to data structures that are shared across all channels on a controller.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: 6b39e89e-21cc-404f-b9fc-6cad0b5c8d22
keywords:
- AtaPortControllerSyncRoutine routine Storage Devices
topic_type:
- apiref
api_name:
- AtaPortControllerSyncRoutine
api_location:
- irb.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AtaPortControllerSyncRoutine routine

The **AtaPortControllerSyncRoutine** routine provides synchronized access to data structures that are shared across all channels on a controller.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
BOOLEAN __inline AtaPortControllerSyncRoutine(
  _In_ PVOID      ChannelExtension,
  _In_ IDE_HW_DPC ControllerSyncRoutine
);
```



## Parameters

<dl> <dt>

*ChannelExtension* \[in\]
</dt> <dd>

A pointer to the channel extension.

</dd> <dt>

*ControllerSyncRoutine* \[in\]
</dt> <dd>

A pointer to the routine to call.

</dd> </dl>

## Return value

None

## Remarks

The miniport driver uses this routine to synchronize access to data structures that are shared across channels on a controller. The miniport driver, however, should use this routine very sparingly.

The *ControllerSyncRoutine* function pointer is declared in *Irb.h* as follows:


```
typedef
VOID
(*IDE_HW_DPC) (
  IN PVOID ChannelExtension
  );
```



## Requirements



|                            |                                                                                                           |
|----------------------------|-----------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                        |
| Header<br/>          | <dl> <dt>Irb.h (include Ata.h or Irb.h)</dt> </dl> |



## See also

<dl> <dt>

[**AtaPortRequestSynchronizedRoutine**](ataportrequestsynchronizedroutine.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20AtaPortControllerSyncRoutine%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






