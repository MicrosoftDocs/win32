---
description: CBaseObject.~CBaseObject destructor - Destructor method.
ms.assetid: 3714d030-f0bd-4826-a3c5-fc206bb88561
title: CBaseObject.~CBaseObject destructor (Combase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseObject.~CBaseObject
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseObject.~CBaseObject destructor

Destructor method.

## Syntax


```C++
~CBaseObject();
```



## Remarks

This method decrements the active-object count. (See [**CBaseObject::ObjectsActive**](cbaseobject-objectsactive.md).)

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Combase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseObject Class**](cbaseobject.md)
</dt> </dl>

 

 




