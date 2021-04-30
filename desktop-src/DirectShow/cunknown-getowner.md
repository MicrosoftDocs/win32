---
description: The GetOwner method retrieves a pointer to the IUnknown interface of the owning component. For an aggregated component, the owner is the outer component. Otherwise, the component owns itself.
ms.assetid: 7d8af9d1-52c0-4f2b-9d05-6ddff85ab508
title: CUnknown.GetOwner method (Combase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CUnknown.GetOwner
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CUnknown.GetOwner method

The `GetOwner` method retrieves a pointer to the **IUnknown** interface of the owning component. For an aggregated component, the owner is the outer component. Otherwise, the component owns itself.

## Syntax


```C++
LPUNKNOWN GetOwner();
```



## Parameters

This method has no parameters.

## Return value

Returns a pointer to the controlling **IUnknown** interface.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Combase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




