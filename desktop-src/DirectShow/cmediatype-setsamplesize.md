---
description: The SetSampleSize method specifies a fixed sample size, or specifies that samples have a variable size.
ms.assetid: b0f9dd7b-4ff9-4d11-9c13-b52d7b1549b5
title: CMediaType.SetSampleSize method (Mtype.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaType.SetSampleSize
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaType.SetSampleSize method

The `SetSampleSize` method specifies a fixed sample size, or specifies that samples have a variable size.

## Syntax


```C++
void SetSampleSize(
   ULONG sz
);
```



## Parameters

<dl> <dt>

*sz* 
</dt> <dd>

Sample size, in bytes, or zero.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

If value of *sz* is zero, the media type uses variable sample sizes. Otherwise, the sample size is fixed at *sz* bytes.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Mtype.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaType Class**](cmediatype.md)
</dt> </dl>

 

 




