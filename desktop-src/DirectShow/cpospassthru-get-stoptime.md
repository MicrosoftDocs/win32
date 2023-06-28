---
description: The get\_StopTime method retrieves the time at which the playback will stop, relative to the duration of the stream. This method implements the IMediaPosition::get\_StopTime method.
ms.assetid: 0ca3f047-ac43-419e-a1ed-b406f89f7af7
title: CPosPassThru.get_StopTime method (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPosPassThru.get_StopTime
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CPosPassThru.get\_StopTime method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `get_StopTime` method retrieves the time at which the playback will stop, relative to the duration of the stream. This method implements the [**IMediaPosition::get\_StopTime**](/windows/desktop/api/Control/nf-control-imediaposition-get_stoptime) method.

## Syntax


```C++
HRESULT get_StopTime(
   REFTIME *pllTime
);
```



## Parameters

<dl> <dt>

*pllTime* 
</dt> <dd>

Pointer to a variable that receives the stop time, in seconds.

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

 

 




