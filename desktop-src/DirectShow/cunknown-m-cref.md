---
Description: Reference count.
ms.assetid: be619a85-ca73-4cee-9df7-20e7be21853b
title: CUnknownm\_cRef member
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CUnknown::m\_cRef member

Reference count.

## Syntax


```C++
LONG m_cRef;
```



## Remarks

Use this member variable if you override the [**NonDelegatingAddRef**](cunknown-nondelegatingaddref.md) or [**NonDelegatingRelease**](cunknown-nondelegatingrelease.md) method.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Combase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




