---
description: The GetMediaType method retrieves a preferred media type.
ms.assetid: 85605885-adb5-4f13-91af-48bf74684eca
title: CSourceStream.GetMediaType method (Source.h) (2)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSourceStream.GetMediaType
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CSourceStream.GetMediaType method (Source.h)

The `GetMediaType` method retrieves a preferred media type.

## Syntax


```C++
virtual HRESULT GetMediaType(
   CMediaType *pMediaType
);
```



## Parameters

<dl> <dt>

*pMediaType* 
</dt> <dd>

Pointer to a [**CMediaType**](cmediatype.md) object that receives the media type.

</dd> </dl>

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                                            | Description                      |
|--------------------------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                   | Success.<br/>              |
| <dl> <dt>**VFW\_S\_NO\_MORE\_ITEMS**</dt> </dl> | Index out of range.<br/>   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>           | Index less than zero.<br/> |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl>           | Unexpected error.<br/>     |



 

## Remarks

There are two versions of this method. One version overrides the [**CBasePin::GetMediaType**](cbasepin-getmediatype.md) method and takes an index value as a parameter. The other version is designed to retrieve a single media type, so it lacks the index parameter.

The single-parameter method returns E\_UNEXPECTED. The two-parameter method verifies that the *iPosition* parameter is zero and then calls the single-parameter version. Depending on the number of media types the pin supports, you must override one of these methods:

-   If the pin supports exactly one media type, override the single-parameter version. Fill in the media type that the pin supports.
-   If the pin supports more than one media type, override the two-parameter version. Also override the [**CSourceStream::CheckMediaType**](csourcestream-checkmediatype.md) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Source.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSourceStream Class**](csourcestream.md)
</dt> </dl>

 

 




