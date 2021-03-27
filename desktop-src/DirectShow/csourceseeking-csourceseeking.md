---
description: Constructor method.
ms.assetid: a51d90c9-4046-42dc-b7cf-51b904c5f57a
title: CSourceSeeking.CSourceSeeking constructor (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSourceSeeking.CSourceSeeking
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CSourceSeeking.CSourceSeeking constructor

Constructor method.

## Syntax


```C++
CSourceSeeking(
   const TCHAR     *pName,
         LPUNKNOWN pUnk,
         HRESULT   *phr,
         CCritSec  *pLock
);
```



## Parameters

<dl> <dt>

*pName* 
</dt> <dd>

Pointer to a string containing the name of the object. For more information, see [**CBaseObject**](cbaseobject.md).

</dd> <dt>

*pUnk* 
</dt> <dd>

Pointer to the owner of this object. If the object is aggregated, pass a pointer to the aggregating object's **IUnknown** interface. Otherwise, set this parameter to **NULL**.

</dd> <dt>

*phr* 
</dt> <dd>

Pointer to an **HRESULT** value. Ignored.

</dd> <dt>

*pLock* 
</dt> <dd>

Pointer to a [**CCritSec**](ccritsec.md) object. In your derived class, declare a **CCritSec** member variable and use the address of it for this parameter. The `CSourceSeeking` class uses this critical section to synchronize access to the start and stop times, duration, and playback rate. Whenever you access those variables in your derived class, hold this lock.

</dd> </dl>

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSourceSeeking Class**](csourceseeking.md)
</dt> </dl>

 

 




