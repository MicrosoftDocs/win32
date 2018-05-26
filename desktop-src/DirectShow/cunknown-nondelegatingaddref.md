---
Description: The NonDelegatingAddRef method increments the reference count on the object. This method implements the INonDelegatingUnknownNonDelegatingAddRef method.
ms.assetid: abb6ee51-8fb8-4307-b127-b3667260e35a
title: CUnknown.NonDelegatingAddRef method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Combase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




