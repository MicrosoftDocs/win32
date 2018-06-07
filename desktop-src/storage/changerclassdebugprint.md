---
title: ChangerClassDebugPrint function
description: The ChangerClassDebugPrint function prints debugging information.
ms.assetid: 452377f1-a926-4f43-8168-bea11622902e
keywords:
- ChangerClassDebugPrint function Storage Devices
topic_type:
- apiref
api_name:
- ChangerClassDebugPrint
api_location:
- Mcd.lib
- Mcd.dll
api_type:
- LibDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ChangerClassDebugPrint function

The **ChangerClassDebugPrint** function prints debugging information.

## Syntax


```C++
VOID ChangerClassDebugPrint(
   ULONG  DebugPrintLevel,
   PCCHAR DebugMessage
);
```



## Parameters

<dl> <dt>

*DebugPrintLevel* 
</dt> <dd>

Indicates how verbose debug information should be. Caller must assign this parameter an integer value between zero and three, where three specifies the highest level of verbosity and zero the lowest.

</dd> <dt>

*DebugMessage* 
</dt> <dd>

Caller can specify a message to be included with the debugging information that is printed by assigning a printable ASCII character string to this parameter.

</dd> </dl>

## Return value

None

## Requirements



|                            |                                                                                                                |
|----------------------------|----------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                             |
| Header<br/>          | <dl> <dt>Mcd.h (include Mcd.h or Ntddchgr.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Mcd.lib</dt> </dl>                             |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ChangerClassDebugPrint%20function%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





