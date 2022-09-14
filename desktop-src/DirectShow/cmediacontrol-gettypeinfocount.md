---
description: CMediaControl.GetTypeInfoCount method - Retrieves the number of type-information interfaces provided by an object.
ms.assetid: 29575325-8f97-4f39-8272-86a917d9144f
title: CMediaControl.GetTypeInfoCount method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaControl.GetTypeInfoCount
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaControl.GetTypeInfoCount method

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

Pointer to the number of type-information interfaces that the object provides. If the object provides type information, this number is 1; otherwise, the number is 0.

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

[**CMediaControl Class**](cmediacontrol.md)
</dt> </dl>

 

 




