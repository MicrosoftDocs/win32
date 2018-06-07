---
title: TapeClassLiDiv routine
description: The TapeClassLiDiv routine performs a division of the two indicated integers.
ms.assetid: 13c449c6-6e2b-434e-8948-62c8af237173
keywords:
- TapeClassLiDiv routine Storage Devices
topic_type:
- apiref
api_name:
- TapeClassLiDiv
api_location:
- Tape.lib
- Tape.dll
api_type:
- LibDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# TapeClassLiDiv routine

The **TapeClassLiDiv** routine performs a division of the two indicated integers.

## Syntax


```C++
LARGE_INTEGER TapeClassLiDiv(
  _In_ LARGE_INTEGER Dividend,
  _In_ LARGE_INTEGER Divisor
);
```



## Parameters

<dl> <dt>

*Dividend* \[in\]
</dt> <dd>

Contains the dividend.

</dd> <dt>

*Divisor* \[in\]
</dt> <dd>

Contains the divisor.

</dd> </dl>

## Return value

**TapeClassLiDiv** returns the result of the division.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Minitape.h (include Minitape.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Tape.lib</dt> </dl>                        |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20TapeClassLiDiv%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





