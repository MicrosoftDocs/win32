---
description: The GetTime method retrieves the stream times at which this sample should begin and finish. This method implements the IMediaSample::GetTime method.
ms.assetid: ddb0df1c-707d-405d-9e73-0d5a59f487b6
title: CMediaSample.GetTime method (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaSample.GetTime
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CMediaSample.GetTime method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `GetTime` method retrieves the stream times at which this sample should begin and finish. This method implements the [**IMediaSample::GetTime**](/windows/desktop/api/Strmif/nf-strmif-imediasample-gettime) method.

## Syntax


```C++
HRESULT GetTime(
   REFERENCE_TIME *pTimeStart,
   REFERENCE_TIME *pTimeEnd
);
```



## Parameters

<dl> <dt>

*pTimeStart* 
</dt> <dd>

Pointer to a variable that receives the beginning stream time, in 100-nanosecond units.

</dd> <dt>

*pTimeEnd* 
</dt> <dd>

Pointer to a variable that receives the ending stream time, in 100-nanosecond units. If the sample has no stop time, the value is set to the start time plus one.

</dd> </dl>

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                                                   | Description                                                 |
|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                          | Success.<br/>                                         |
| <dl> <dt>**VFW\_S\_NO\_STOP\_TIME**</dt> </dl>         | Sample has a valid start time, but no stop time.<br/> |
| <dl> <dt>**VFW\_E\_SAMPLE\_TIME\_NOT\_SET**</dt> </dl> | Sample does not have valid time stamps.<br/>          |



 

## Remarks

The [**CMediaSample::m\_Start**](cmediasample-m-start.md) and [**CMediaSample::m\_End**](cmediasample-m-end.md) member variables specify the time stamps. The [**CMediaSample::m\_dwFlags**](cmediasample-m-dwflags.md) member variable specifies whether the time stamps are valid.

For information about time stamps, see [Time and Clocks in DirectShow](time-and-clocks-in-directshow.md).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaSample Class**](cmediasample.md)
</dt> </dl>

 

 




