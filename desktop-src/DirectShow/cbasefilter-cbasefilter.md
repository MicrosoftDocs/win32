---
description: Constructor method.
ms.assetid: 705a075e-3f0f-4e7d-94b6-3458f87b6718
title: CBaseFilter.CBaseFilter(const TCHAR*, LPUNKNOWN, CCritSec*, REFCLSID, HRESULT*) constructor (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseFilter.CBaseFilter
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseFilter.CBaseFilter(const TCHAR\*, LPUNKNOWN, CCritSec\*, REFCLSID, HRESULT\*) constructor

Constructor method.

## Syntax


```C++
CBaseFilter(
   const TCHAR     *pName,
         LPUNKNOWN pUnk,
         CCritSec  *pLock,
         REFCLSID  clsid,
         HRESULT   *phr
);
```



## Parameters

<dl> <dt>

*pName* 
</dt> <dd>

Pointer to a string containing the name of the filter, for debugging purposes.

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

Class identifier (CLSID) of the filter.

</dd> <dt>

*phr* 
</dt> <dd>

Pointer to an **HRESULT** value. The constructor ignores this parameter.

</dd> </dl>

## Remarks

For the critical section object, you would typically do one of the following:

-   Derive a class that inherits both **CBaseFilter** and **CCritSec**. For *pLock*, pass the `this` pointer.
-   Derive a class that inherits **CBaseFilter** and contains a **CCritSec** member variable. For *pLock*, pass the address of that variable.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseFilter Class**](cbasefilter.md)
</dt> </dl>

 

 




