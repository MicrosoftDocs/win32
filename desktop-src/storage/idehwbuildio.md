---
title: IdeHwBuildIo routine
description: The IdeHwBuildIo miniport driver routine is called one time for every incoming I/O request.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: 057fb78f-6f1c-4b16-b9fa-6fcff299a90d
keywords:
- IdeHwBuildIo routine Storage Devices
- IDE_HW_BUILDIO
topic_type:
- apiref
api_name:
- IdeHwBuildIo
api_location:
- irb.h
api_type:
- UserDefined
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IdeHwBuildIo routine

The ***IdeHwBuildIo*** miniport driver routine is called one time for every incoming I/O request.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
IDE_HW_BUILDIO IdeHwBuildIo;

BOOLEAN IdeHwBuildIo(
  _In_ PVOID              ChannelExtension,
  _In_ PIDE_REQUEST_BLOCK Irb
)
{ ... }
```



## Parameters

<dl> <dt>

*ChannelExtension* \[in\]
</dt> <dd>

A pointer to the miniport driver channel extension.

</dd> <dt>

*Irb* \[in\]
</dt> <dd>

A pointer to a structure of type [**IDE\_REQUEST\_BLOCK**](ide-request-block.md) that defines the Integrated Device Electronics (IDE) input/output request block (IRB) to process.

</dd> </dl>

## Return value

***IdeHwBuildIo*** returns **TRUE** to acknowledge the receipt of the [**IDE\_REQUEST\_BLOCK**](ide-request-block.md) structure. The port driver ignores a return value of **FALSE**.

## Remarks

Miniport drivers provide an ***AtaHwBuildlo*** routine that performs unsynchronized I/O processing with interrupts enabled. After ***IdeHwBuildIo*** completes all unsynchronized processing of a request, it returns to the port driver, and the port driver passes the request to the miniport driver's [**IdeHwStartIo**](idehwstartio.md) routine, which performs the tasks that require synchronization.

The miniport driver must observe certain restrictions while it executes the ***IdeHwBuildIo*** routine. The miniport driver calls ***IdeHwBuildIo*** without holding any locks. In particular, the miniport driver must not touch any shared data in its channel extension, nor can it call any of the routines exported by the ATA port driver.

If the miniport driver must complete a request while it executes the ***IdeHwBuildIo*** routine, it must assign the appropriate completion status value to the **IrbStatus** member of the [**IDE\_REQUEST\_BLOCK**](ide-request-block.md) structure pointed to by the *Irb* parameter. The miniport driver must not set **IrbStatus** to a value of IRB\_STATUS\_PENDING.

The miniport driver can use the ***IdeHwBuildIo*** routine to indicate to the port driver how an IRB should be handled. For example, the miniport driver can request that the port driver map the buffer at *DataBuffer* by setting the **IrbFlags** member of the IRB to the appropriate value. The miniport driver should not request that the buffer that is associated with a request be mapped unless the request is some type of data transfer.

The ***IdeHwBuildIo*** routine resembles Storport's [**HwStorBuildIo**](hwstorbuildio.md) routine in functionality. For more information about the ***HwStorBuildIo*** routine, see [Unsynchronized HwStorBuildIo Routine](https://msdn.microsoft.com/library/windows/hardware/ff567985).

***IdeHwBuildIo*** is an optional routine.

## Requirements



|                            |                                                                                                  |
|----------------------------|--------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>               |
| Header<br/>          | <dl> <dt>Irb.h (include Irb.h)</dt> </dl> |



## See also

<dl> <dt>

[**IdeHwStartIo**](idehwstartio.md)
</dt> <dt>

[**IDE\_REQUEST\_BLOCK**](ide-request-block.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IdeHwBuildIo%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






