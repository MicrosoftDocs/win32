---
description: The SetSyncPoint method specifies whether the beginning of this sample is a synchronization point. This method implements the IMediaSample::SetSyncPoint method.
ms.assetid: 48fc5145-7cce-4e76-860d-45a0d5b43b67
title: CMediaSample.SetSyncPoint method (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaSample.SetSyncPoint
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CMediaSample.SetSyncPoint method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `SetSyncPoint` method specifies whether the beginning of this sample is a synchronization point. This method implements the [**IMediaSample::SetSyncPoint**](/windows/desktop/api/Strmif/nf-strmif-imediasample-setsyncpoint) method.

## Syntax


```C++
HRESULT SetSyncPoint(
   BOOL bIsSyncPoint
);
```



## Parameters

<dl> <dt>

*bIsSyncPoint* 
</dt> <dd>

Boolean value that specifies whether this is a synchronization point. If **TRUE**, this is a synchronization point.

</dd> </dl>

## Return value

Returns S\_OK.

## Remarks

This method updates the [**CMediaSample::m\_dwFlags**](cmediasample-m-dwflags.md) member variable, which specifies the synchronization-point property.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaSample Class**](cmediasample.md)
</dt> </dl>

 

 




