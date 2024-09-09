---
description: The GetMediaType method retrieves a preferred media type. This method uses the *iPosition* and *pMediaType* parameters.
ms.assetid: c5c5f498-a9a3-4ce7-8cf5-941397aa649d
title: CSourceStream.GetMediaType method (Source.h) - iPosition and pMediaType parameters
ms.topic: reference
ms.date: 4/26/2023
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
ms.custom: UpdateFrequency5
---

# CSourceStream.GetMediaType method (Source.h) - iPosition and pMediaType parameters

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **GetMediaType** method retrieves a preferred media type.

## Syntax


```C++
virtual HRESULT GetMediaType(
   int        iPosition,
   CMediaType *pMediaType
);
```



## Parameters

<dl> <dt>

*iPosition* 
</dt> <dd>

Zero-based index value.

</dd> <dt>

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
| Header  | Source.h (include Streams.h)                                                                                    |
| Library | Strmbase.lib (retail builds); Strmbasd.lib (debug builds) |

## See also

<dl> <dt>

[**CSourceStream Class**](csourcestream.md)
</dt> </dl>

 

 




