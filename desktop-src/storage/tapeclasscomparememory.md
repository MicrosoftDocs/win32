---
title: TapeClassCompareMemory routine
description: The TapeClassCompareMemory routine compares two memory buffers and returns the number of bytes that are equivalent.
ms.assetid: dfff350c-ff76-49d3-b4ba-a5a51fabd419
keywords:
- TapeClassCompareMemory routine Storage Devices
topic_type:
- apiref
api_name:
- TapeClassCompareMemory
api_location:
- Tape.lib
- Tape.dll
api_type:
- LibDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TapeClassCompareMemory routine

The **TapeClassCompareMemory** routine compares two memory buffers and returns the number of bytes that are equivalent.

## Syntax


```C++
ULONG TapeClassCompareMemory(
  _Inout_ PVOID Source1,
  _Inout_ PVOID Source2,
  _In_    ULONG Length
);
```



## Parameters

<dl> <dt>

*Source1* \[in, out\]
</dt> <dd>

Pointer to the first buffer to be compared.

</dd> <dt>

*Source2* \[in, out\]
</dt> <dd>

Pointer to the second buffer to be compared.

</dd> <dt>

*Length* \[in\]
</dt> <dd>

Specifies the number of bytes to be compared.

</dd> </dl>

## Return value

**TapeClassCompareMemory** returns the number of bytes that are equivalent.

## Remarks

A tape miniclass driver uses **TapeClassCompareMemory** to compare memory in a portable way. For example, a miniclass driver uses **TapeClassCompareMemory** in its TapeMiniVerifyInquiry routine to determine whether a given product ID matches one of the devices the driver supports.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Minitape.h (include Minitape.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Tape.lib</dt> </dl>                        |



## See also

<dl> <dt>

[**TapeMiniVerifyInquiry**](tapeminiverifyinquiry.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20TapeClassCompareMemory%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






