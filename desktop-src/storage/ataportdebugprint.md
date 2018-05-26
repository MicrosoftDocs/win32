---
title: AtaPortDebugPrint routine
description: The AtaPortDebugPrint routine passes a message string to the kernel debugger for the debugger to print.
ms.assetid: 2a93d30f-4aa0-46b9-b9c7-cc15c62f3053
keywords:
- AtaPortDebugPrint routine Storage Devices
topic_type:
- apiref
api_name:
- AtaPortDebugPrint
api_location:
- ataport.lib
- ataport.dll
- pciidex.lib
- pciidex.dll
api_type:
- LibDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AtaPortDebugPrint routine

The **AtaPortDebugPrint** routine passes a message string to the kernel debugger for the debugger to print.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
VOID AtaPortDebugPrint(
   ULONG  DebugPrintLevel,
   PCCHAR DebugMessage
);
```



## Parameters

<dl> <dt>

*DebugPrintLevel* 
</dt> <dd>

Determines how much debug information to display.

</dd> <dt>

*DebugMessage* 
</dt> <dd>

A pointer to the debug message to display.

</dd> </dl>

## Return value

None

## Remarks

The verbosity of debug output is determined by *DebugPrintLevel* and a port driver-specific mask. Use the **nt!kd\_idep\_mask** command to set the desired level of verbosity. For more information about the kernel debugger, see the [Using a Debugger](https://msdn.microsoft.com/library/windows/hardware/ff554094) topic

## Requirements



|                            |                                                                                                                                                           |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                                                                        |
| Header<br/>          | <dl> <dt>Irb.h (include Ata.h or Irb.h)</dt> </dl>                                                 |
| Library<br/>         | <dl> <dt>Ataport.lib; </dt> <dt>Pciidex.lib</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20AtaPortDebugPrint%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





