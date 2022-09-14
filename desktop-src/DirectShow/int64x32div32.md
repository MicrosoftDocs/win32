---
description: The Int64x32Div32 function implements the formula ((a\*b)+rnd)/c where a is a 64-bit value and b, c, and rnd are 32-bit values.
ms.assetid: 566ac194-5b15-43b7-aa7c-0c18c6f69691
title: Int64x32Div32 function (Wxutil.h)
ms.topic: reference
ms.date: 05/31/2018
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
---

# Int64x32Div32 function

The `Int64x32Div32` function implements the formula `((a*b)+rnd)/c` where *a* is a 64-bit value and *b*, *c*, and *rnd* are 32-bit values.

## Syntax


```C++
LONGLONG WINAPI Int64x32Div32(
   LONGLONG a,
   LONG     b,
   LONG     c,
   LONG     rnd
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

Time stamps and seek times are 64-bit values, so this function is useful for performing conversions on 32-bit systems. For example, in MPEG-1 the system clock reference is 90-kHz, or 90,000 ticks per second. The formula to convert this to reference time (100-nanosecond units) is


```C++
(timestamp * 1000) / 9
```



which can be calculated as `Int64x32Div32(timestamp, 1000, 9, 0)`. Use the *rnd* parameter as a rounding factor.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Miscellaneous Helper Functions](miscellaneous-helper-functions.md)
</dt> <dt>

[**llMulDiv**](llmuldiv.md)
</dt> </dl>

 

 




