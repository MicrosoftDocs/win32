---
description: The IsPreroll method determines if this sample is a preroll sample. A preroll sample should not be displayed. This method implements the IMediaSample::IsPreroll method.
ms.assetid: fbcf7aab-473c-49c1-9a8f-4a619f4e28f4
title: CMediaSample.IsPreroll method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaSample.IsPreroll
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaSample.IsPreroll method

The `IsPreroll` method determines if this sample is a preroll sample. A preroll sample should not be displayed. This method implements the [**IMediaSample::IsPreroll**](/windows/desktop/api/Strmif/nf-strmif-imediasample-ispreroll) method.

## Syntax


```C++
HRESULT IsPreroll();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK if the sample is a preroll sample, and S\_FALSE otherwise.

## Remarks

The [**CMediaSample::m\_dwFlags**](cmediasample-m-dwflags.md) member variable specifies this property.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaSample Class**](cmediasample.md)
</dt> </dl>

 

 




