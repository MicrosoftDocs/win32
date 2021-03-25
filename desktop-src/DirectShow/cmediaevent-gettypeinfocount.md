---
description: Retrieves the number of type-information interfaces provided by an object.
ms.assetid: e16bc324-bb49-4df2-afeb-2c2cd1620693
title: CMediaEvent.GetTypeInfoCount method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaEvent.GetTypeInfoCount
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaEvent.GetTypeInfoCount method

Retrieves the number of type-information interfaces provided by an object.

## Syntax


```C++
HRESULT GetTypeInfoCount(
   UINT *pctinfo
);
```



## Parameters

<dl> <dt>

*pctinfo* 
</dt> <dd>

Pointer to number of type-information interfaces that the object provides. If the object provides type information, this number is 1; otherwise, the number is 0.

</dd> </dl>

## Return value

Returns E\_POINTER if *pctinfo* is invalid; otherwise, returns S\_OK.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaEvent Class**](cmediaevent.md)
</dt> </dl>

 

 




