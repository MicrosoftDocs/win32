---
description: The SetMediaType method sets the media type for the sample. This method implements the IMediaSample::SetMediaType method.
ms.assetid: 4423cc1e-d6e1-49e7-9cc1-1a1d71a3497b
title: CMediaSample.SetMediaType method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaSample.SetMediaType
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaSample.SetMediaType method

The `SetMediaType` method sets the media type for the sample. This method implements the [**IMediaSample::SetMediaType**](/windows/desktop/api/Strmif/nf-strmif-imediasample-setmediatype) method.

## Syntax


```C++
HRESULT SetMediaType(
   AM_MEDIA_TYPE *pMediaType
);
```



## Parameters

<dl> <dt>

*pMediaType* 
</dt> <dd>

Pointer to an [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) structure.

</dd> </dl>

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                                   | Description                    |
|-----------------------------------------------------------------------------------------------|--------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Success<br/>             |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory<br/> |



 

## Remarks

This method sets the [**CMediaSample::m\_pMediaType**](cmediasample-m-pmediatype.md) member variable, which specifies the media type, and the [**CMediaSample::m\_dwFlags**](cmediasample-m-dwflags.md) member variable, which specifies whether the media type has changed.

This method makes a copy of the AM\_MEDIA\_TYPE structure.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaSample Class**](cmediasample.md)
</dt> </dl>

 

 




