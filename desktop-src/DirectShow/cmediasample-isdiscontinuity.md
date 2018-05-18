---
Description: 'The IsDiscontinuity method determines if this sample represents a break in the data stream. This method implements the IMediaSample::IsDiscontinuity method.'
ms.assetid: '125b4a86-bd26-4539-a9ab-281f1aed1836'
title: 'CMediaSample.IsDiscontinuity method'
---

# CMediaSample.IsDiscontinuity method

The `IsDiscontinuity` method determines if this sample represents a break in the data stream. This method implements the [**IMediaSample::IsDiscontinuity**](imediasample-isdiscontinuity.md) method.

## Syntax


```C++
HRESULT IsDiscontinuity();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK if the sample is a break in the data stream, and S\_FALSE otherwise.

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

 

 




