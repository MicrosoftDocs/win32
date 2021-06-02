---
description: Decrements the reference count on the object. This method implements the INonDelegatingUnknown::NonDelegatingRelease method.
ms.assetid: 58610f7d-5524-450f-a0f8-b299944abc78
title: CUnknown.NonDelegatingRelease method (Combase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CUnknown.NonDelegatingRelease
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CUnknown.NonDelegatingRelease method

Decrements the reference count on the object. This method implements the **INonDelegatingUnknown::NonDelegatingRelease** method.

## Syntax


```C++
ULONG NonDelegatingRelease();
```



## Parameters

This method has no parameters.

## Return value

Returns the reference count.

## Remarks

When the reference count reaches zero, the object deletes itself.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Combase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




