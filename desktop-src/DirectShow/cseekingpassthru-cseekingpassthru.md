---
description: CSeekingPassThru.CSeekingPassThru constructor - Constructor method.
ms.assetid: e31253fc-b365-4414-9dee-906d4c41d16e
title: CSeekingPassThru.CSeekingPassThru constructor (Seekpt.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSeekingPassThru.CSeekingPassThru
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CSeekingPassThru.CSeekingPassThru constructor

Constructor method.

## Syntax


```C++
CSeekingPassThru(
   const TCHAR     *pName,
         LPUNKNOWN pUnk,
         HRESULT   *phr
);
```



## Parameters

<dl> <dt>

*pName* 
</dt> <dd>

String containing the name of the object. See [**CBaseObject**](cbaseobject.md) for more information.

</dd> <dt>

*pUnk* 
</dt> <dd>

Pointer to the owner of this object. If the object is aggregated, pass a pointer to the aggregating object's **IUnknown** interface. Otherwise, set this parameter to **NULL**.

</dd> <dt>

*phr* 
</dt> <dd>

Pointer to an **HRESULT** value. Ignored.

</dd> </dl>

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Seekpt.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSeekingPassThru Class**](cseekingpassthru.md)
</dt> </dl>

 

 




