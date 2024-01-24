---
description: This method is not currently implemented and returns E\_NOTIMPL.
ms.assetid: 1004d7e1-d1e9-4217-bbbb-a25f46c7112f
title: CDeferredCommand.Confidence method (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CDeferredCommand.Confidence
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CDeferredCommand.Confidence method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This method is not currently implemented and returns E\_NOTIMPL.

## Syntax


```C++
HRESULT Confidence(
   LONG *pConfidence
);
```



## Parameters

<dl> <dt>

*pConfidence* 
</dt> <dd>

Pointer to the confidence level.

</dd> </dl>

## Return value

Returns E\_NOTIMPL.

## Remarks

For information about implementing this method, see [**IDeferredCommand::Confidence**](/windows/desktop/api/Control/nf-control-ideferredcommand-confidence).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDeferredCommand Class**](cdeferredcommand.md)
</dt> </dl>

 

 




