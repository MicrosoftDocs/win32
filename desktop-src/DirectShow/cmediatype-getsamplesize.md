---
description: The GetSampleSize method retrieves the sample size.
ms.assetid: 5cc98556-cca6-46ca-ad33-cd40011ff6f4
title: CMediaType.GetSampleSize method (Mtype.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaType.GetSampleSize
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaType.GetSampleSize method

The `GetSampleSize` method retrieves the sample size.

## Syntax


```C++
ULONG GetSampleSize() const;
```



## Parameters

This method has no parameters.

## Return value

If the sample size is fixed, returns the sample size in bytes. Otherwise, returns zero.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Mtype.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaType Class**](cmediatype.md)
</dt> </dl>

 

 




