---
Description: Destructor method.
ms.assetid: 92375e95-adfb-414b-abbb-e827db2186ac
title: CMediaType.~CMediaType destructor
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CMediaType.~CMediaType destructor

Destructor method.

## Syntax


```C++
~CMediaType();
```



## Remarks

The destructor calls the [**FreeMediaType**](freemediatype.md) function on itself.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Mtype.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaType Class**](cmediatype.md)
</dt> </dl>

 

 




