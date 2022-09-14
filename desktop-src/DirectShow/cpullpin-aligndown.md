---
description: The AlignDown method truncates a value to a specified alignment boundary.
ms.assetid: f0efdedb-67ec-49d6-92a8-54485aa04e15
title: CPullPin.AlignDown method (Pullpin.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPullPin.AlignDown
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CPullPin.AlignDown method

The `AlignDown` method truncates a value to a specified alignment boundary.

## Syntax


```C++
LONGLONG AlignDown(
   LONGLONG ll,
   LONG     lAlign
);
```



## Parameters

<dl> <dt>

*ll* 
</dt> <dd>

Specifies the number to align.

</dd> <dt>

*lAlign* 
</dt> <dd>

Specifies the alignment boundary.

</dd> </dl>

## Return value

Returns the aligned result.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Pullpin.h</dt> </dl>                                                                                                       |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPullPin Class**](cpullpin.md)
</dt> </dl>

 

 




