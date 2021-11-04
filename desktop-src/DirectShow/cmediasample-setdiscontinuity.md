---
description: The SetDiscontinuity method specifies whether this sample represents a break in the data stream. This method implements the IMediaSample::SetDiscontinuity method.
ms.assetid: 29072130-1ec7-4b5b-8a43-5308b1365527
title: CMediaSample.SetDiscontinuity method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaSample.SetDiscontinuity
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaSample.SetDiscontinuity method

The `SetDiscontinuity` method specifies whether this sample represents a break in the data stream. This method implements the [**IMediaSample::SetDiscontinuity**](/windows/desktop/api/Strmif/nf-strmif-imediasample-setdiscontinuity) method.

## Syntax


```C++
HRESULT SetDiscontinuity(
   BOOL bDiscont
);
```



## Parameters

<dl> <dt>

*bDiscont* 
</dt> <dd>

Boolean value that specifies whether this sample is a discontinuity. If **TRUE**, the media sample is discontinuous with the previous sample.

</dd> </dl>

## Return value

Returns S\_OK.

## Remarks

This method updates the [**CMediaSample::m\_dwFlags**](cmediasample-m-dwflags.md) member variable, which specifies the discontinuity property.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaSample Class**](cmediasample.md)
</dt> </dl>

 

 




