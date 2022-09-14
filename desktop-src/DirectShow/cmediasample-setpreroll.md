---
description: The SetPreroll method specifies whether this sample is a preroll sample. A preroll sample should not be displayed. This method implements the IMediaSample::SetPreroll method.
ms.assetid: 2887e627-5999-407a-88d3-811c803c9a43
title: CMediaSample.SetPreroll method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaSample.SetPreroll
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaSample.SetPreroll method

The `SetPreroll` method specifies whether this sample is a preroll sample. A preroll sample should not be displayed. This method implements the [**IMediaSample::SetPreroll**](/windows/desktop/api/Strmif/nf-strmif-imediasample-setpreroll) method.

## Syntax


```C++
HRESULT SetPreroll(
   BOOL bIsPreroll
);
```



## Parameters

<dl> <dt>

*bIsPreroll* 
</dt> <dd>

Boolean value that specifies whether this is a preroll sample. If **TRUE**, this is a preroll sample.

</dd> </dl>

## Return value

Returns S\_OK.

## Remarks

This method updates the [**CMediaSample::m\_dwFlags**](cmediasample-m-dwflags.md) member variable, which specifies the preroll property.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaSample Class**](cmediasample.md)
</dt> </dl>

 

 




