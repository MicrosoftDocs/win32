---
description: CBaseReferenceClock.CBaseReferenceClock constructor - Constructor method.
ms.assetid: 0fbfdc68-e1df-449f-a7d1-739504db8a2f
title: CBaseReferenceClock.CBaseReferenceClock constructor (Refclock.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseReferenceClock.CBaseReferenceClock
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseReferenceClock.CBaseReferenceClock constructor

Constructor method.

## Syntax


```C++
CBaseReferenceClock(
   TCHAR       *pName,
   LPUNKNOWN   pUnk,
   HRESULT     *phr,
   CAMSchedule *pSched = NULL
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

Pointer to the owner of this object. If the object is aggregated, pass a pointer to the aggregating object's IUnknown interface. Otherwise, set this parameter to **NULL**.

</dd> <dt>

*phr* 
</dt> <dd>

Pointer to an **HRESULT** value. If an error occurs, the method returns an error code in this parameter. Do not set this parameter to **NULL**.

</dd> <dt>

*pSched* 
</dt> <dd>

Pointer to a [**CAMSchedule**](camschedule.md) object. If **NULL**, this method creates a new **CAMSchedule** object.

</dd> </dl>

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Refclock.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseReferenceClock Class**](cbasereferenceclock.md)
</dt> </dl>

 

 




