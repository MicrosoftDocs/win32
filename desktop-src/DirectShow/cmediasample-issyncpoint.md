---
Description: 'The IsSyncPoint method determines if the beginning of the sample is a synchronization point. This method implements the IMediaSample::IsSyncPoint method.'
ms.assetid: 'e57f78f4-7bb9-4e23-bcb4-55ad7ab5482c'
title: 'CMediaSample.IsSyncPoint method'
---

# CMediaSample.IsSyncPoint method

The `IsSyncPoint` method determines if the beginning of the sample is a synchronization point. This method implements the [**IMediaSample::IsSyncPoint**](imediasample-issyncpoint.md) method.

## Syntax


```C++
HRESULT IsSyncPoint();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK if the sample is a synchronization point, or S\_FALSE otherwise.

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

 

 




