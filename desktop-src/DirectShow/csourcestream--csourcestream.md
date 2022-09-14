---
description: CSourceStream.~CSourceStream destructor - Destructor method.
ms.assetid: 678085c2-5999-4e62-8749-99b783787cc6
title: CSourceStream.~CSourceStream destructor (Source.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSourceStream.~CSourceStream
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CSourceStream.~CSourceStream destructor

Destructor method.

## Syntax


```C++
~CSourceStream();
```



## Remarks

The destructor automatically removes the pin from the owning filter, by calling [**CSource::RemovePin**](csource-removepin.md).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Source.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSourceStream Class**](csourcestream.md)
</dt> </dl>

 

 




