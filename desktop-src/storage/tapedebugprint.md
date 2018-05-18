---
title: TapeDebugPrint routine
description: The TapeDebugPrint routine prints the indicated string.
ms.assetid: 'd06e4308-f1a9-4acd-bc25-b3fd53129064'
keywords: ["TapeDebugPrint routine Storage Devices"]
topic_type:
- apiref
api_name:
- TapeDebugPrint
api_location:
- Tape.lib
- Tape.dll
api_type:
- LibDef
---

# TapeDebugPrint routine

The **TapeDebugPrint** routine prints the indicated string.

## Syntax


```C++
VOID TapeDebugPrint(
   ULONG  DebugPrintLevel,
   PCCHAR DebugMessage
);
```



## Parameters

<dl> <dt>

*DebugPrintLevel* 
</dt> <dd>

Determines whether the string is printed or not. If this parameter has a value less than or equal to the tape class global variable **TapeClassDebug**, **TapeDebugPrint** prints the message, otherwise nothing is printed. If this parameter has a value of zero, **TapeClassDebug** always prints the message.

</dd> <dt>

*DebugMessage* 
</dt> <dd>

Pointer to the string to be printed.

</dd> </dl>

## Return value

None

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Minitape.h (include Minitape.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Tape.lib</dt> </dl>                        |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20TapeDebugPrint%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





