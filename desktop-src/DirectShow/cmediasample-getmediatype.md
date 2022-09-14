---
description: The GetMediaType method retrieves the media type, if the media type differs from the previous sample. This method implements the IMediaSample::GetMediaType method.
ms.assetid: a7850381-d448-4bf6-b059-d734fb3e8e22
title: CMediaSample.GetMediaType method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaSample.GetMediaType
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaSample.GetMediaType method

The `GetMediaType` method retrieves the media type, if the media type differs from the previous sample. This method implements the [**IMediaSample::GetMediaType**](/windows/desktop/api/Strmif/nf-strmif-imediasample-getmediatype) method.

## Syntax


```C++
HRESULT GetMediaType(
   AM_MEDIA_TYPE **ppMediaType
);
```



## Parameters

<dl> <dt>

*ppMediaType* 
</dt> <dd>

Address of a variable that receives a pointer to an [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) structure. If the media type has not changed from the previous sample, *\*ppMediaType* is set to **NULL**.

</dd> </dl>

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                                   | Description                                                         |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl>       | The media type has not changed from the previous sample.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>          | Success.<br/>                                                 |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory.<br/>                                     |



 

## Remarks

When you are done with the media type, free the memory block by calling the [**DeleteMediaType**](deletemediatype.md) utility function.

The [**CMediaSample::m\_pMediaType**](cmediasample-m-pmediatype.md) member variable specifies the media type. The [**CMediaSample::m\_dwFlags**](cmediasample-m-dwflags.md) member variable specifies whether the media type has changed.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaSample Class**](cmediasample.md)
</dt> </dl>

 

 




