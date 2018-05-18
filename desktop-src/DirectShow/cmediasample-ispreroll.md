---
Description: 'The IsPreroll method determines if this sample is a preroll sample. A preroll sample should not be displayed. This method implements the IMediaSample::IsPreroll method.'
ms.assetid: 'fbcf7aab-473c-49c1-9a8f-4a619f4e28f4'
title: 'CMediaSample.IsPreroll method'
---

# CMediaSample.IsPreroll method

The `IsPreroll` method determines if this sample is a preroll sample. A preroll sample should not be displayed. This method implements the [**IMediaSample::IsPreroll**](imediasample-ispreroll.md) method.

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



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaSample Class**](cmediasample.md)
</dt> </dl>

 

 




