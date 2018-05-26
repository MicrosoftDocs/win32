---
Description: The pStateLock method retrieves a pointer to the filters critical section object.
ms.assetid: 10a2e74b-a5aa-4d68-958e-d86f4b78037e
title: CSource.pStateLock method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CSource.pStateLock method

The **pStateLock** method retrieves a pointer to the filter's critical section object.

> [!Note]  
> Although named like a member variable, **pStateLock** is a method.

 

## Syntax


```C++
CCritSec* pStateLock();
```



## Parameters

This method has no parameters.

## Return value

Returns a pointer to the [**CSource::m\_cStateLock**](csource-m-cstatelock.md) member variable.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Source.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSource Class**](csource.md)
</dt> </dl>

 

 




