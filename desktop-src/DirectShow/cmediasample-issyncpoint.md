---
description: The IsSyncPoint method determines if the beginning of the sample is a synchronization point. This method implements the IMediaSample::IsSyncPoint method.
ms.assetid: e57f78f4-7bb9-4e23-bcb4-55ad7ab5482c
title: CMediaSample.IsSyncPoint method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaSample.IsSyncPoint
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaSample.IsSyncPoint method

The `IsSyncPoint` method determines if the beginning of the sample is a synchronization point. This method implements the [**IMediaSample::IsSyncPoint**](/windows/desktop/api/Strmif/nf-strmif-imediasample-issyncpoint) method.

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



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaSample Class**](cmediasample.md)
</dt> </dl>

 

 




