---
description: The NonDelegatingAddRef method increments the reference count on the object. This method implements the INonDelegatingUnknown::NonDelegatingAddRef method.
ms.assetid: abb6ee51-8fb8-4307-b127-b3667260e35a
title: CUnknown.NonDelegatingAddRef method (Combase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CUnknown.NonDelegatingAddRef
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CUnknown.NonDelegatingAddRef method

The `NonDelegatingAddRef` method increments the reference count on the object. This method implements the **INonDelegatingUnknown::NonDelegatingAddRef** method.

## Syntax


```C++
ULONG NonDelegatingAddRef();
```



## Parameters

This method has no parameters.

## Return value

Returns the reference count.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Combase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




