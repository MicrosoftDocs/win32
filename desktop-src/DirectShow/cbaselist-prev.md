---
description: The Prev method retrieves the previous position in the list.
ms.assetid: 537c3019-373a-4974-a42e-72150da72767
title: CBaseList.Prev method (Wxlist.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseList.Prev
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseList.Prev method

The `Prev` method retrieves the previous position in the list.

## Syntax


```C++
POSITION Prev(
   POSITION pos
);
```



## Parameters

<dl> <dt>

*pos* 
</dt> <dd>

POSITION value.

</dd> </dl>

## Return value

Returns the position indicator that is previous to the position specified in *pos*.

## Remarks

If *pos* is the first position in the list, the method returns **NULL**. If *pos* is **NULL**, the method returns the last position in the list.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxlist.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseList Class**](cbaselist.md)
</dt> </dl>

 

 




