---
description: The SetVariableSize method specifies that samples do not have a fixed size.
ms.assetid: 2a207cdb-f8e6-44aa-8bf6-868267aeb42d
title: CMediaType.SetVariableSize method (Mtype.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaType.SetVariableSize
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaType.SetVariableSize method

The `SetVariableSize` method specifies that samples do not have a fixed size.

## Syntax


```C++
void SetVariableSize();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

This method sets the **bFixedSizeSamples** member to **FALSE**. Subsequent calls to the [**CMediaType::GetSampleSize**](cmediatype-getsamplesize.md) method return zero.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Mtype.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaType Class**](cmediatype.md)
</dt> </dl>

 

 




