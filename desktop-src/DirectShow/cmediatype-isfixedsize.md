---
description: The IsFixedSize method determines if the samples have a fixed size or a variable size.
ms.assetid: bd49f01a-21bb-48a2-aa9e-94ea0d2dbab3
title: CMediaType.IsFixedSize method (Mtype.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaType.IsFixedSize
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaType.IsFixedSize method

The `IsFixedSize` method determines if the samples have a fixed size or a variable size.

## Syntax


```C++
BOOL IsFixedSize() const;
```



## Parameters

This method has no parameters.

## Return value

Returns the value of the **bFixedSizeSamples** member.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Mtype.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaType Class**](cmediatype.md)
</dt> </dl>

 

 




