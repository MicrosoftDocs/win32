---
description: The GetActualDataLength method retrieves the length of the valid data in the buffer. This method implements the IMediaSample::GetActualDataLength method.
ms.assetid: bdb8c2b9-7be4-494b-bb96-34a9936d4a2f
title: CMediaSample.GetActualDataLength method (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaSample.GetActualDataLength
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CMediaSample.GetActualDataLength method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `GetActualDataLength` method retrieves the length of the valid data in the buffer. This method implements the [**IMediaSample::GetActualDataLength**](/windows/win32/api/strmif/nf-strmif-imediasample-getactualdatalength) method.

## Syntax


```C++
LONG GetActualDataLength();
```



## Parameters

This method has no parameters.

## Return value

Returns the length of the valid data, in bytes.

## Remarks

The [**CMediaSample::m\_lActual**](cmediasample-m-lactual.md) member variable specifies this property.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaSample Class**](cmediasample.md)
</dt> </dl>

 

