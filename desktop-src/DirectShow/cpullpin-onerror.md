---
description: The OnError method is called if an error occurs during streaming. The derived class must implement this method.
ms.assetid: 0f135cab-611c-4464-9605-360a30de7eb3
title: CPullPin.OnError method (Pullpin.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPullPin.OnError
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CPullPin.OnError method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `OnError` method is called if an error occurs during streaming. The derived class must implement this method.

## Syntax


```C++
virtual void OnError(
   HRESULT hr
) = 0;
```



## Parameters

<dl> <dt>

*hr* 
</dt> <dd>

Specifies the **HRESULT** value returned by the method that failed.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The object calls this method whenever an error occurs that halts the data-pulling thread. The filter can use this method to recover from streaming errors gracefully. In most cases, the error is returned from the upstream filter, so the upstream filter is responsible for reporting it to the Filter Graph Manager. If the error occurs inside the [**CPullPin::Receive**](cpullpin-receive.md) method, your filter should send an [**EC\_ERRORABORT**](ec-errorabort.md) event. (See [**IMediaEventSink::Notify**](/windows/desktop/api/Strmif/nf-strmif-imediaeventsink-notify).)

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Pullpin.h</dt> </dl>                                                                                                       |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPullPin Class**](cpullpin.md)
</dt> </dl>

 

 




