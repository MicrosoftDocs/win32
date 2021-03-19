---
description: Constructor method.
ms.assetid: 91290f58-a77b-447f-aa2a-bbee067f5a98
title: CBaseMediaFilter.CBaseMediaFilter constructor (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseMediaFilter.CBaseMediaFilter
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseMediaFilter.CBaseMediaFilter constructor

Constructor method.

## Syntax


```C++
CBaseMediaFilter(
   const TCHAR     *pName,
         LPUNKNOWN pUnk,
         CCritSec  *pLock,
         REFCLSID  clsid
);
```



## Parameters

<dl> <dt>

*pName* 
</dt> <dd>

Pointer to a string containing the name of the object.

</dd> <dt>

*pUnk* 
</dt> <dd>

Pointer to the owner of this object. If the object is aggregated, pass a pointer to the aggregating object's **IUnknown** interface. Otherwise, set this parameter to **NULL**.

</dd> <dt>

*pLock* 
</dt> <dd>

Pointer to a [**CCritSec**](ccritsec.md) lock, used to serialize state changes.

</dd> <dt>

*clsid* 
</dt> <dd>

Class identifier of the object.

</dd> </dl>

## Remarks

If another object contains or aggregates the `CBaseMediaFilter` object, the **CCritSec** lock might be external to the `CBaseMediaFilter` object. In that case, pass a pointer to the lock in *pLock*.

Otherwise, you can:

-   Derive a class that inherits both `CBaseMediaFilter` and **CCritSec**. For *pLock*, pass the this pointer.
-   Derive a class that inherits `CBaseMediaFilter` and contains a **CCritSec** member variable. For *pLock*, pass the address of that variable.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseMediaFilter Class**](cbasemediafilter.md)
</dt> </dl>

 

 




