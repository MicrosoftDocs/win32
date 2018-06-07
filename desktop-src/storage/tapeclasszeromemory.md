---
title: TapeClassZeroMemory routine
description: The TapeClassZeroMemory routine fills a buffer with zeros.
ms.assetid: a1f15890-ded8-4aba-8b67-6f1fb1490178
keywords:
- TapeClassZeroMemory routine Storage Devices
topic_type:
- apiref
api_name:
- TapeClassZeroMemory
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

# TapeClassZeroMemory routine

The **TapeClassZeroMemory** routine fills a buffer with zeros.

## Syntax


```C++
VOID TapeClassZeroMemory(
  _Inout_ PVOID Buffer,
  _In_    ULONG BufferSize
);
```



## Parameters

<dl> <dt>

*Buffer* \[in, out\]
</dt> <dd>

Pointer to the buffer that needs to be cleared.

</dd> <dt>

*BufferSize* \[in\]
</dt> <dd>

Specifies the size of the buffer, in bytes.

</dd> </dl>

## Return value

None

## Remarks

A tape miniclass driver calls **TapeClassZeroMemory** to zero a buffer in a portable way. A miniclass driver must use **TapeClassZeroMemory** to clear the TAPE\_INIT\_DATA\_EX structure and CDBs before it uses them.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Minitape.h (include Minitape.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Tape.lib</dt> </dl>                        |



## See also

<dl> <dt>

[**DriverEntry of Tape Miniclass Driver**](driverentry-of-tape-miniclass-driver.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20TapeClassZeroMemory%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






