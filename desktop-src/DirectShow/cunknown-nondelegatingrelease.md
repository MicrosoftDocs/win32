---
Description: Decrements the reference count on the object. This method implements the INonDelegatingUnknownNonDelegatingRelease method.
ms.assetid: 58610f7d-5524-450f-a0f8-b299944abc78
title: CUnknown.NonDelegatingRelease method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Combase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




