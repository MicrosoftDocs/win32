---
description: The GetStopPosition method retrieves the time at which the playback will stop, relative to the duration of the stream. This method implements the IMediaSeeking::GetStopPosition method.
ms.assetid: 11486371-da0a-4b83-956b-ef6b92721e74
title: CPosPassThru.GetStopPosition method (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPosPassThru.GetStopPosition
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CPosPassThru.GetStopPosition method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `GetStopPosition` method retrieves the time at which the playback will stop, relative to the duration of the stream. This method implements the [**IMediaSeeking::GetStopPosition**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-getstopposition) method.

## Syntax


```C++
HRESULT GetStopPosition(
   LONGLONG *pStop
);
```



## Parameters

<dl> <dt>

*pStop* 
</dt> <dd>

Pointer to a variable that receives the stop time, in units of the current time format.

</dd> </dl>

## Return value

Returns the **HRESULT** value from the connected pin.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPosPassThru Class**](cpospassthru.md)
</dt> </dl>

 

 




