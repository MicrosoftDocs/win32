---
description: The llMulDiv function implements the formula ((a\*b)+rnd)/c where each term is a 64-bit value.
ms.assetid: cd5073b9-27c7-42ee-8487-2d4ea29f77d4
title: llMulDiv function (Wxutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Int64x32Div32
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# llMulDiv function

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `llMulDiv` function implements the formula `((a*b)+rnd)/c` where each term is a 64-bit value.

Time stamps and seek times are 64-bit values, so this function is useful for performing conversions on 32-bit systems. For example, the formula for bytes-per-second is


```C++
(Number of Bytes * Reference Time) / 10,000,000
```



which can be calculated as `llMulDiv(nBytes, rtTime, 10000000, 0)`. Use the *rnd* parameter as a rounding factor.

## Syntax


```C++
LONGLONG WINAPI Int64x32Div32(
   LONGLONG a,
   LONGLONG b,
   LONGLONG c,
   LONGLONG rnd
);
```



## Parameters

<dl> <dt>

*a* 
</dt> <dd>

Multiplicand.

</dd> <dt>

*b* 
</dt> <dd>

Multiplier.

</dd> <dt>

*c* 
</dt> <dd>

Divisor.

</dd> <dt>

*rnd* 
</dt> <dd>

Rounding factor.

</dd> </dl>

## Return value

Returns either the `(a * b + rnd)/c` calculation or one of the following values.



| Return code                                                                                       | Description                                                              |
|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| <dl> <dt>**0x7FFFFFFFFFFFFFFF**</dt> </dl> | Overflow occurred because the result is too large (positive).<br/> |
| <dl> <dt>**0x8000000000000000**</dt> </dl> | Overflow occurred because the result is too large (negative).<br/> |



 

## Remarks

Rounding on the division is toward zero. Division by zero is counted as an overflow condition.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Miscellaneous Helper Functions](miscellaneous-helper-functions.md)
</dt> <dt>

[**Int64x32Div32**](int64x32div32.md)
</dt> </dl>

 

 




