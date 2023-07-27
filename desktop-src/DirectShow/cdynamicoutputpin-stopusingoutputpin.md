---
description: The StopUsingOutputPin method releases access to the pin after a streaming operation.
ms.assetid: f0dbf2c0-1f1b-41bc-84d2-dc9f37bf725e
title: CDynamicOutputPin.StopUsingOutputPin method
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CDynamicOutputPin.StopUsingOutputPin
api_type: 
- COM
api_location: 
ms.custom: UpdateFrequency5
---

# CDynamicOutputPin.StopUsingOutputPin method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `StopUsingOutputPin` method releases access to the pin after a streaming operation.

## Syntax


```C++
virtual void StopUsingOutputPin();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## See also

<dl> <dt>

[**StartUsingOutputPin**](cdynamicoutputpin-startusingoutputpin.md)
</dt> <dt>

[**CDynamicOutputPin Class**](cdynamicoutputpin.md)
</dt> </dl>

 

 



