---
description: The InitMediaType method initializes the media type.
ms.assetid: 141ced68-11ed-4567-b2e1-82c040d3b4a4
title: CMediaType.InitMediaType method (Mtype.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaType.InitMediaType
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaType.InitMediaType method

The `InitMediaType` method initializes the media type.

## Syntax


```C++
void InitMediaType();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

This method zeroes the object's memory, sets the fixed-sample-size property to **TRUE**, and sets the sample size to 1.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Mtype.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaType Class**](cmediatype.md)
</dt> </dl>

 

 




