---
description: The REMIND macro generates a reminder at compile time. This macro generates a string that includes the parameter string, the name of the source file, and the line number.
ms.assetid: 12043df5-ed68-4980-91aa-7598d8ab1951
title: REMIND (Wxdebug.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- REMIND
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# REMIND

The `REMIND` macro generates a reminder at compile time. This macro generates a string that includes the parameter string, the name of the source file, and the line number.

``` syntax
REMIND(strLiteral);
```

## Parameters

<dl> <dt>

<span id="strLiteral"></span><span id="strliteral"></span><span id="STRLITERAL"></span>*strLiteral*
</dt> <dd>

Text string.

</dd> </dl>

## Remarks

This macro is useful for generating compile-time warnings:


```C++
#pragma message (REMIND("TO DO: Add support for IDispatch."))
```



## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxdebug.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Debug Output Functions](debug-output-functions.md)
</dt> </dl>

 

 




