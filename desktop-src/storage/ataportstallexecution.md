---
title: AtaPortStallExecution function
description: The AtaPortStallExecution stalls in the miniport driver.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: 5dae484f-fb79-4291-bae5-dba0be7f9b97
keywords:
- AtaPortStallExecution function Storage Devices
topic_type:
- apiref
api_name:
- AtaPortStallExecution
api_location:
- ataport.lib
- ataport.dll
- pciidex.lib
- pciidex.dll
api_type:
- LibDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AtaPortStallExecution function

The **AtaPortStallExecution** stalls in the miniport driver.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
VOID AtaPortStallExecution(
  _In_ ULONG Delay
);
```



## Parameters

<dl> <dt>

*Delay* \[in\]
</dt> <dd>

Specifies the delay interval, in microseconds.

</dd> </dl>

## Return value

None

## Remarks

Miniport drivers should rarely call the **AtaPortStallExecution** routine. The total stall time in any miniport driver routine must always be less than one millisecond. Because this call ties up a processor, the processor does no useful work while it stalls in the driver.

Typically, a miniport driver should call **AtaPortStallExecution** only if the driver must wait for some sort of state change on the HBA that is unable to cause an interrupt, or if the driver must delay for a very short interval between accesses to the HBA.

Miniport drivers should use the [**AtaPortRequestTimer**](ataportrequesttimer.md) routine for delays longer than 1 millisecond.

## Requirements



|                            |                                                                                                                                                           |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                                                                        |
| Header<br/>          | <dl> <dt>Irb.h (include Ata.h or Irb.h)</dt> </dl>                                                 |
| Library<br/>         | <dl> <dt>Ataport.lib; </dt> <dt>Pciidex.lib</dt> </dl> |



## See also

<dl> <dt>

[**AtaPortRequestTimer**](ataportrequesttimer.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20AtaPortStallExecution%20function%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






