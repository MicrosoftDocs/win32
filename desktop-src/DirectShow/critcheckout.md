---
description: Returns FALSE if the current thread is the owner of the specified critical section.
ms.assetid: 1a2cb56c-2806-4bb2-b904-985af332b290
title: CritCheckOut function (Wxutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CritCheckOut
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CritCheckOut function

Returns **FALSE** if the current thread is the owner of the specified critical section.

## Syntax


```C++
BOOL WINAPI CritCheckOut(
   CCritSec *pcCrit
);
```



## Parameters

<dl> <dt>

*pcCrit* 
</dt> <dd>

Pointer to a [**CCritSec**](ccritsec.md) critical section.

</dd> </dl>

## Return value

In debug builds, returns **FALSE** if the current thread is the owner of this critical section, or **TRUE** otherwise. In retail builds, always returns **TRUE**.

## Remarks

This function is the inverse of the [**CritCheckIn**](critcheckin.md) function. If **CritCheckIn** returns **TRUE**, **CritCheckOut** returns **FALSE**, and vice versa.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Critical Section Debugging Functions](critical-section-debugging-functions.md)
</dt> </dl>

 

 




